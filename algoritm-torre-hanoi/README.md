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
