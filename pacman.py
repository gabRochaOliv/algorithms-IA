from collections import deque

def bfs(labirinto, inicio, fim):
    # Inicialização da fila BFS
    fila = deque([inicio])
    visitados = set()
    visitados.add(inicio)
    pais = {inicio: None}

    while fila:
        atual = fila.popleft()
        
        if atual == fim:
            # Reconstruir o caminho do fim até o início
            caminho = []
            while atual:
                caminho.insert(0, atual)
                atual = pais[atual]
            return caminho
        
        # Explorar os vizinhos (cima, baixo, esquerda, direita)
        x, y = atual
        vizinhos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for vizinho in vizinhos:
            vx, vy = vizinho
            if 0 <= vx < len(labirinto) and 0 <= vy < len(labirinto[0]):
                if labirinto[vx][vy] != '#' and vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)
                    pais[vizinho] = (x, y)
    
    return None  # Caminho não encontrado

def encontrar_posicoes(labirinto, item):
    posicoes = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == item:
                posicoes.append((i, j))
    return posicoes

def pacman_bfs(labirinto):
    inicio = encontrar_posicoes(labirinto, 'P')[0]
    bolinhas = encontrar_posicoes(labirinto, 'O')
    caminho_total = []

    for bolinha in bolinhas:
        caminho = bfs(labirinto, inicio, bolinha)
        if caminho:
            caminho_total.extend(caminho[1:])  # Evitar duplicação do ponto de início
            inicio = bolinha  # Atualizar posição inicial para a próxima busca
        else:
            print("Caminho não encontrado para uma das bolinhas.")
            return None
    
    return caminho_total

# Exemplo de labirinto 9x17
labirinto = [
    ['O', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
    ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '],
    [' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' '],
    [' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' '],
    [' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' '],
    [' ', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', 'O']
]

caminho_total = pacman_bfs(labirinto)
if caminho_total:
    print("Caminho completo do Pac-Man para coletar todas as bolinhas maiores:")
    print(caminho_total)
else:
    print("Não foi possível encontrar o caminho para coletar todas as bolinhas maiores.")
