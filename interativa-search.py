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
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Bucharest': ['Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi']
}

def ldfs(grafo, inicio, fim, visitados, limite, pais={}, profundidade=0):
    if profundidade == limite:
        return False

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            visitados.append(vizinho)
            pais[vizinho] = inicio
            if vizinho == fim:
                return pais
            res = ldfs(grafo, vizinho, fim, visitados, limite, pais, profundidade + 1)
            if res:
                return res
            visitados.remove(vizinho)
    return False

def ids(grafo, inicio, fim, limite):
    for i in range(limite):
        res = ldfs(grafo, inicio, fim, [inicio], i)
        if res:
            return res
    return False

inicio = input("Digite a cidade de origem: ")
fim = input("Digite a cidade de destino: ")
count = 0
for nodo in grafo:
    if nodo == inicio or nodo == fim:
        count += 1

if count == 2:
    res = ids(grafo, inicio, fim, 5)
    if not res:
        print("Cidade não encontrada, pois o limite foi excedido")
        exit()
    caminho = [fim]
    pai = res[fim]
    while inicio != fim:
        caminho.insert(0, res[fim])
        fim = res[fim]

    print("Caminho: ", caminho)
else:
    print("Cidade não encontrada")
