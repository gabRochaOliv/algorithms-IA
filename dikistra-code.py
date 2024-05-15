grafo = {
    'Oradea': {'Sibiu': 151, 'Zerind': 71,},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75 },
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Dobreta': 75, 'Lugoj': 70},
    'Dobreta': { 'Craiova': 120, 'Mehadia': 75},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97, },
    'Bucharest': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101,  'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Eforie': 86,   'Urziceni': 98,},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142,},
    'Iasi': {'Neamt': 87, 'Vaslui': 92,},
    'Neamt': {'Iasi': 87}
}

#como é que ele percorre o grafo

def dks(grafo, inicio, fim):
    fila = [inicio]

    visitados = [inicio]

    custo = {inicio: 0} #diferencial comparado ao breadth

    pais = {}

    encontrado = False

    caminho = {inicio: [inicio]}

    while fila:
        no = fila.pop(0)

        if no == fim:
            print("O menor caminho de {} para {} é: {}".format(inicio, fim, ' -> '.join(caminho[no])))
            print("O custo foi: ", custo[no])
            encontrado=True
            break

        for vizinho in grafo[no]:

            if vizinho not in visitados:

                if vizinho not in custo or custo[vizinho] > custo[no] + grafo[no][vizinho]:

                    custo[vizinho] = custo[no] + grafo[no][vizinho]

                    caminho[vizinho] = caminho[no] + [vizinho]

                    fila.append(vizinho)
                fila = sorted(fila, key=lambda x: custo[x])

    if not encontrado:
        print("Caminho não encontrado")

inicio = input("Digite a cidade de origem: ")
fim = input("Digite a cidade de destino: ")
contagem = 0
for no in grafo:
    if no == inicio or no == fim:
        contagem += 1
if contagem == 2:
    dks(grafo, inicio, fim)
else:
    print("Cidade não encontrada")
