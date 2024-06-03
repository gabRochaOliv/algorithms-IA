import networkx as nx
import itertools

def grafo_hanoi(discos):

    grafo = nx.Graph()    
    permutacoes = list(itertools.product(list(range(1, 4)), repeat=discos))

    for permutacao in permutacoes:
        a, b, c, d, e = permutacao
        aux = 1
        while aux < discos-1:

            if aux != a:
                grafo.add_edge((a, b, c, d, e), (aux, b, c, d, e))

            if aux != b and b != a and aux != a:
                grafo.add_edge((a, b, c, d, e), (a, aux, c, d, e))

            if aux != c and  c != a and c != b and aux != a and aux != b:
                grafo.add_edge((a, b, c, d, e), (a, b, aux, d, e))

            if aux != d and d != a and d != b and d != c and aux != a and aux != b and aux != c:
                grafo.add_edge((a, b, c, d, e), (a, b, c, aux, e))

            if aux != e and e != a and e != b and e != c and e != d and aux != a and aux != b and aux != c and aux != d:
                grafo.add_edge((a, b, c, d, e), (a, b, c, d, aux))
            
            aux += 1
            
    return grafo

def busca_em_largura(grafo, inicio, fim, contador=0):
    fila = [inicio]
    visitados = [inicio]
    pais = {}
    encontrado = False

    while fila:
        no = fila.pop(0)

        if no == fim:
            caminho = [fim]

            while fim != inicio:
                contador += 1
                caminho.insert(0, pais[fim])
                fim = pais[fim]
            
            encontrado = True
            print("Caminho por extensão: ", caminho, "\nTotal de buscas: ", contador, "\n\n")
    
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)
                pais[vizinho] = no

    if not encontrado:
        print("Caminho por extensão não encontrado\n")

def busca_em_profundidade(grafo, inicio, fim, visitados, pais={}):
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            visitados.append(vizinho)
            pais[vizinho] = inicio
            if vizinho == fim:
                return pais
            res = busca_em_profundidade(grafo, vizinho, fim, visitados, pais)
            if res:
                global contador
                contador += 1
                return res
    return False

def busca_em_profundidade_limitada(grafo, inicio, fim, visitados, limite, pais={}, profundidade=0):
    if profundidade == limite:
        return False

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            visitados.append(vizinho)
            pais[vizinho] = inicio
            if vizinho == fim:
                return pais
            res = busca_em_profundidade_limitada(grafo, vizinho, fim, visitados, limite, pais, profundidade+1)
            if res:
                global contador
                contador += 1
                return res
            visitados.remove(vizinho)
    return False

def busca_iterativa(grafo, inicio, fim, limite):
    for i in range(limite):
        res = busca_em_profundidade_limitada(grafo, inicio, fim, [inicio], i)
        if res:
            return res
    return False

def main():
    grafo = nx.to_dict_of_lists(grafo_hanoi(5))
    inicio = (1, 1, 1, 1, 1)
    fim = (3, 3, 3, 3, 3)
    
    busca_em_largura(grafo, inicio, fim)

    global contador
    contador = 0
    res = busca_em_profundidade(grafo, inicio, fim, [inicio])
    if not res:
        print("Caminho por profundidade não encontrado\n")
    caminho = [fim]
    while inicio != fim:
        caminho.insert(0, res[fim])
        fim = res[fim]

    print("Caminho por profundidade: ", caminho, "Total de buscas: ", contador, "\n\n")

    contador = 0

    # res = busca_iterativa(grafo, inicio, fim, 20)
    # if not res:
    #    print("Cidade não encontrada, pois o limite foi excedido")
    #    exit()
    # caminho = [fim]
    # while inicio != fim:
    #    caminho.insert(0, res[fim])
    #    fim = res[fim]

    # print("Caminho por iteração: ", caminho, "Total de buscas: ", contador, "\n\n")

main()
