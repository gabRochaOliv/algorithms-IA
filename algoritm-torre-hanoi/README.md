# Algoritmo de Busca em Grafo para o Problema das Torres de Hanói

## Introdução

Este algoritmo implementa estratégias de busca em grafo para resolver o Problema das Torres de Hanói. Ele inclui as seguintes estratégias de busca:

1. Busca em Largura
2. Busca em Profundidade
3. Busca em Profundidade Limitada
4. Busca Iterativa

## Código em Python

```python
import networkx as nx
import itertools

# Função para criar o grafo das Torres de Hanói
def grafo_hanoi(discos):
    # Implementação do grafo
    ...

# Função para busca em largura no grafo
def busca_em_largura(grafo, inicio, fim, contador=0):
    # Implementação da busca em largura
    ...

# Função para busca em profundidade no grafo
def busca_em_profundidade(grafo, inicio, fim, visitados, pais={}):
    # Implementação da busca em profundidade
    ...

# Função para busca em profundidade limitada no grafo
def busca_em_profundidade_limitada(grafo, inicio, fim, visitados, limite, pais={}, profundidade=0):
    # Implementação da busca em profundidade limitada
    ...

# Função para busca iterativa no grafo
def busca_iterativa(grafo, inicio, fim, limite):
    # Implementação da busca iterativa
    ...

# Função principal
def main():
    # Configurações iniciais
    ...


# Execução da função principal
main()
```
## Estratégia de redução 

A estratégia consiste em modelar o problema das Torres de Hanói como um grafo, onde cada nó representa um estado do jogo (ou seja, uma configuração dos discos nos pinos) e as arestas representam as transições entre esses estados (ou seja, os movimentos válidos permitidos pelo jogo).

### Modelagem do Grafo
A função ```grafo_hanoi(discos)``` é responsável por criar o grafo das Torres de Hanói. Ela gera todas as possíveis combinações de posições dos discos e adiciona arestas entre essas combinações de acordo com as regras do jogo.

### Busca em Largura
A função ```busca_em_largura(grafo, inicio, fim, contador)``` implementa o algoritmo de busca em largura no grafo. Começando do nó inicial (inicio), ela explora todos os seus vizinhos antes de passar para os vizinhos dos vizinhos. Isso permite encontrar uma solução ótima, ou seja, o caminho mínimo entre o nó inicial e o nó de destino (fim).

### Busca em Profundidade 
A função ```busca_em_profundidade(grafo, inicio, fim, visitados, pais={})``` implementa o algoritmo de busca em profundidade no grafo. Esta estratégia explora tão longe quanto possível ao longo de cada ramificação antes de fazer retrocesso. Isso pode ser útil para encontrar soluções rapidamente em problemas com muitas soluções possíveis.

### Busca em Profundidade Limitada 
A função ```busca_em_profundidade_limitada(grafo, inicio, fim, visitados, limite, pais={}, profundidade=0)``` é uma versão modificada da busca em profundidade que limita a profundidade máxima da busca. Isso é útil para evitar buscas infinitas em grafos que podem ter ciclos ou profundidade desconhecida.

### Busca Iterativa 
A função ```busca_iterativa(grafo, inicio, fim, limite)``` implementa a busca em profundidade limitada de forma iterativa. Ela aumenta progressivamente o limite de profundidade até encontrar o nó de destino ou atingir o limite máximo definido. Isso combina os benefícios da busca em profundidade com a garantia de terminação da busca em largura.
