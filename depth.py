

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

def dfs(grafo, inicio, fim, visitados, pais={}):
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            visitados.append(vizinho)
            pais[vizinho] = inicio
            if vizinho == fim:
                return pais
            res = dfs(grafo, vizinho, fim, visitados, pais)
            if res != False:
                return res
    return False


inicio = input("Digite a cidade de Origem: ")
fim = input("Digite a cidade Destino: ")
count = 0
for node in grafo:
    if(node == inicio or node == fim):
        count += 1
if count == 2:
    res = dfs(grafo, inicio, fim, [inicio])
    caminho = [fim]
    while inicio != fim:
        caminho.insert(0, res[fim])
        fim = res[fim]

    print("Caminho: ", caminho)
else:
    print("Cidade não encontrada")
