grafo = {
    'Oradea': ['Sibiu', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Dobreta', 'Lugoj'],
    'Dobreta': ['Craiova', 'Mehadia'],
    'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
    'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Craiova', 'Pitesti', 'Sibiu'],
    'Fagaras': ['Bucareste', 'Sibiu'],
    'Pitesti': ['Bucareste', 'Craiova', 'Rimnicu Vilcea'],
    'Bucareste': ['Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'],
    'Giurgiu': ['Bucareste'],
    'Urziceni': ['Bucareste', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi']
}

def busca_em_largura(grafo, inicio, fim):
    fila = [inicio]
    
    visitados =[inicio]

    pais = {}
    
    encontrado = False

    while fila:
        no = fila.pop(0)

        if no == fim:
            caminho = [fim]

            while fim != inicio:
                caminho.insert(0, pais[fim])
                fim = pais[fim]
            
            encontrado = True
            print("O menor caminho de {} para {} é: {}".format(inicio, fim, ' -> '.join(caminho)))
            
        for vizinho in grafo[no]:
            if vizinho not in visitados:

                visitados.append(vizinho)

                fila.append(vizinho)

                pais[vizinho] = no

    if not encontrado:
        print("Caminho não encontrado")


inicio = input("Digite a cidade de origem: ")
fim = input("Digite a cidade de destino: ")
contador = 0
for no in grafo:
    if no == inicio or no == fim:
        contador += 1
if contador == 2:
    busca_em_largura(grafo, inicio, fim)
else:
    print("Cidade não encontrada")
