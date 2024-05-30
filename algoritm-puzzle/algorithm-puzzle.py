import datetime
import itertools
import networkx as nx

grafo = nx.Graph()

def grafo_quebra_cabeca():
    # Gera todas as permutações possíveis dos números de 0 a 8
    permutacoes = list(itertools.permutations(list(range(9)), 9))
    
    for permutacao in permutacoes:
        a, b, c, d, e, f, g, h, i = permutacao

        # Verifica se todos os elementos são únicos
        if len(set((a, b, c, d, e, f, g, h, i))) == 9:
            # Verifica e cria arestas para cada posição
            # A
            if b == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (b, a, c, d, e, f, g, h, i))
            if d == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (d, b, c, a, e, f, g, h, i))
            
            # B
            if a == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (b, a, c, d, e, f, g, h, i))
            if c == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, c, b, d, e, f, g, h, i))
            if e == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, e, c, d, b, f, g, h, i))
            
            # C
            if b == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, c, b, d, e, f, g, h, i))
            if f == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, f, d, e, c, g, h, i))
            
            # D
            if a == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (d, b, c, a, e, f, g, h, i))
            if e == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, e, d, f, g, h, i))
            if g == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, g, e, f, d, h, i))
            
            # E
            if b == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, e, c, d, b, f, g, h, i))
            if d == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, e, d, f, g, h, i))
            if f == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, f, e, g, h, i))
            if h == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, h, f, g, e, i))
            
            # F
            if c == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, f, d, e, c, g, h, i))
            if e == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, f, e, g, h, i))
            if i == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, i, g, h, f))
            
            # G
            if d == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, g, e, f, d, h, i))
            if h == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, f, h, g, i))
            
            # H
            if e == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, h, f, g, e, i))
            if g == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, f, h, g, i))
            if i == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, f, g, i, h))
            
            # I
            if f == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, i, g, h, f))
            if h == 0:
                grafo.add_edge((a, b, c, d, e, f, g, h, i), (a, b, c, d, e, f, g, i, h))

    return grafo

def busca_largura(grafo, inicio, fim, contador=0):
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
            break  # Para sair do loop quando o caminho é encontrado
    
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)
                pais[vizinho] = no

    if not encontrado:
        print("Caminho por extensão não encontrado\n")

def principal():
    # Início da geração do grafo
    print("Início do grafo: ", datetime.datetime.now())
    grafo_quebra_cabeca()
    # Fim da geração do grafo
    print("Término do grafo: ", datetime.datetime.now())

    grafo_dict = nx.to_dict_of_lists(grafo)

    # Busca em extensão
    inicio = (8, 5, 4, 2, 7, 1, 3, 6, 0)
    fim = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    # Printa data e hora de início
    print("Início da busca: ", datetime.datetime.now())

    busca_largura(grafo_dict, inicio, fim)

    # Printa data e hora de término
    print("Término da busca: ", datetime.datetime.now())

# Executa a função principal
if __name__ == "__main__":
    principal()
