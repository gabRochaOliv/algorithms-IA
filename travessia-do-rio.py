from collections import deque

# Função para verificar se um estado é válido
def estado_valido(estado):
    pai, mae, filho1, filho2, filha1, filha2, policial, prisioneira, jangada = estado
    
    # Regras
    if (pai != mae and (filho1 == mae or filho2 == mae)):
        return False
    if (pai != mae and (filha1 == pai or filha2 == pai)):
        return False
    if (policial != prisioneira and (prisioneira == pai or prisioneira == mae or prisioneira == filho1 or prisioneira == filho2 or prisioneira == filha1 or prisioneira == filha2)):
        return False
    return True

# Função para gerar novos estados a partir de um estado atual
def gerar_estados(estado):
    pai, mae, filho1, filho2, filha1, filha2, policial, prisioneira, jangada = estado
    novos_estados = []
    
    # Movimentos possíveis: todos que sabem manobrar a jangada (pai, mãe, policial) + uma pessoa (ou sozinhos)
    manobristas = [0, 1, 6]  # Índices de pai, mãe e policial
    todos = list(range(8))   # Todos os índices exceto a jangada

    # Tentar mover cada manobrista sozinho
    for i in manobristas:
        novo_estado = list(estado)
        if jangada == estado[i]:  # Se ambos estão na mesma margem
            novo_estado[i] = 'D' if estado[i] == 'E' else 'E'
            novo_estado[8] = 'D' if jangada == 'E' else 'E'
            if estado_valido(tuple(novo_estado)):
                novos_estados.append(tuple(novo_estado))
    
    # Tentar mover cada manobrista com outra pessoa
    for i in manobristas:
        for j in todos:
            if i != j and jangada == estado[i] == estado[j]:  # Se todos estão na mesma margem
                novo_estado = list(estado)
                novo_estado[i] = 'D' if estado[i] == 'E' else 'E'
                novo_estado[j] = 'D' if estado[j] == 'E' else 'E'
                novo_estado[8] = 'D' if jangada == 'E' else 'E'
                if estado_valido(tuple(novo_estado)):
                    novos_estados.append(tuple(novo_estado))

    return novos_estados

# Função BFS para encontrar a solução
def busca_em_largura(estado_inicial, estado_objetivo):
    fila = deque([estado_inicial])
    visitados = set([estado_inicial])
    pais = {estado_inicial: None}

    while fila:
        estado_atual = fila.popleft()
        
        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return caminho
        
        for estado in gerar_estados(estado_atual):
            if estado not in visitados:
                visitados.add(estado)
                fila.append(estado)
                pais[estado] = estado_atual
    
    return None

# Definindo os estados inicial e objetivo
estado_inicial = ('E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E')  # Todos na margem esquerda
estado_objetivo = ('D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D')  # Todos na margem direita

# Executando a busca
solucao = busca_em_largura(estado_inicial, estado_objetivo)
if solucao:
    for passo in solucao:
        print(passo)
else:
    print("Solução não encontrada")
