
# Breadth

Primeiramente vamos analisar o contexto para a construção do código: 
“ O usuário escolherá a cidade de origem e a cidade de destino e o algoritmo escolherá o caminho que passa pelo menor número de cidades entre a origem e destino usando a estratégia de Busca em extensão ”.
Como citado no contexto será necessário a criação de um grafo para que consigamos armazenar todas as cidades e suas possíveis cidades vizinhas, podendo seguir um padrão de:  

``` ‘cidade principal’ : [‘ 1ª cidade vizinha’,‘2ª cidade vizinha’], ```

para que fique dessa forma: 

```
grafo = {
    'Oradea': ['Sibiu', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Dobreta', 'Lugoj'],
    'Dobreta': ['Craiova', 'Mehadia'], 
    ...
    }

```

Após fazer o grafo, devemos pensar que será necessário adaptar uma estrutura de dados que seja capaz de fazer a ordenação de acordo com o contexto proposto. Para decidir qual estrutura usar vamos analisar novamente o contexto, “ [...] o algoritmo escolherá o caminho que passa pelo menor número de cidades entre a origem e destino [… ] “, ou seja, o algoritmo terá que percorrer todo o grafo, cidade a cidade em ordem até que chegue a cidade de destino, mais parecido com uma estrutura de uma fila, então vamos lá. Em estrutura de dados temos uma estrutura denominada fila, que faz exatamente a ordenação que precisamos e para sua criação, e para sua construção vamos precisar de uma função que contenha as possíveis posições de uma fila, dessa forma:

```
def busca_em_largura(grafo, inicio, fim):
    fila = [inicio]
    
    visitados =[inicio]

    pais = {}
    
    encontrado = False
```

Nesse trecho de código foi definido como parâmetro da função as seguintes variáveis: 

 ``` ( grafo, inicio, fim ) ```

A variável ```grafo``` que serviu para armazenar o grafo que fizemos lá em cima representando as conexões entre as cidades, uma variável de ```inicio```que representa a cidade de origem, a partir da qual começaremos a busca, e uma variável fim que representa a cidade de destino. Após essas atribuições criamos uma variável que vai armazenar o estado da nossa fila, chamado ```fila``` e logo após atribuímos a posição da fila a posição inicial, ou seja atribuímos a variável ```inicio```, dessa maneira: ```fila = [inicio]```. Em seguida criamos uma variável ```visitados``` que servirá para armazenar uma lista de cidades visitadas e iniciamos com a cidade de origem, para evitar revisitar cidades já exploradas. Criamos uma variável ``` pais``` que servirá como dicionário que seja capaz de  armazenar o caminho percorrido durante a busca, dessa forma cada cidade visitada terá um "pai", que é a cidade anterior no caminho e inicializamos uma variável booleana para indicar se o destino foi encontrado durante a busca denominada e inicializamos ela como False, dessa forma: ```encontrado = False```. Agora com as variáveis inicializadas começaremos as verificações para que essa fila funcione:

```
while fila:
        no = fila.pop(0)

        if no == fim:
            caminho = [fim]

            while fim != inicio:
                caminho.insert(0, pais[fim])
                fim = pais[fim]
            
            encontrado = True
            print("O menor caminho de {} para {} é: {}".format(inicio, fim, ' -> '.join(caminho)))

```

Para garantir que o programa continue executando enquanto tiver cidades para explorar, iniciamos um loop ```while fila```. Por padrão, tiramos o primeiro elemento da fila para explorar sua conexão com outras cidades ```no = fila.pop(0)``` criando uma variável ```no```que contém o nome da cidade que estamos prestes a explorar e verificar suas conexões com outras cidades no grafo e atribuímos a uma função já pré-definida na linguagem python que remove e retorna o primeiro elemento da lista fila (No contexto de uma busca em largura, isso significa que estamos retirando a próxima cidade a ser explorada da fila. A remoção do elemento na posição 0 garante que estamos processando as cidades na ordem em que foram adicionadas à fila). Seguimos verificando ```if no == fim```,  ou seja, se a cidade atual é a cidade de destino. Iniciamos uma lista chamada ```caminho``` com a cidade de destino ```caminho = [fim]``` porque, ao encontrarmos a cidade de destino durante a busca em largura, precisamos reconstruir o caminho percorrido até chegar a essa cidade. 

Em:  

```

while fim != inicio:
                caminho.insert(0, pais[fim])
                fim = pais[fim]

```
Inicialmente, temos a cidade de destino armazenada na variável ```fim```. Entramos em um loop ```while``` que continua enquanto ```fim``` for diferente de ```inicio```. Isso significa que continuaremos retrocedendo no caminho até chegarmos à cidade de origem. Em cada iteração do loop, inserimos o "pai" da cidade atual (representado por ```pais[fim]```) no início da lista ```caminho```. Isso é feito utilizando o método ```insert(0, pais[fim])```, que insere o elemento ```pais[fim]``` na posição 0 da lista ``` caminho```, empurrando os elementos existentes para a direita. Em seguida, atualizamos a cidade atual (fim) para seu "pai", ou seja, a cidade anterior no caminho. Isso nos permite continuar retrocedendo no ```caminho```até chegarmos à cidade de origem. O loop continua até que ```fim```seja igual a ```inicio```, ou seja, até que tenhamos retrocedido até a cidade de origem.

Em:

```
encontrado = True 
print("O menor caminho de {} para {} é: {}".format(inicio, fim, ' -> '.join(caminho)))


```

Criamos e definimos uma variável chamada ```encontrada``` como verdadeira (```True```), indicando que encontramos o caminho mais curto da cidade de origem para a cidade de destino. Em seguida, é impressa uma mensagem na tela utilizando ```print()```. Esta mensagem informa ao usuário o menor caminho encontrado da cidade de origem para a cidade de destino. O texto é formatado utilizando a função ```format()```, onde: ```{}``` são espaços reservados para os valores que serão inseridos na mensagem. inicio é substituído pelo nome da cidade de origem, ```fim ```é substituído pelo nome da cidade de destino. ``` ' -> '.join ```(caminho) junta os elementos da lista caminho em uma string, separando-os com ```' -> '```. Isso cria uma representação visual do caminho percorrido da cidade de origem à cidade de destino, mostrando todas as cidades intermediárias no meio.
```
 for vizinho in grafo[no]:
            if vizinho not in visitados:

                visitados.append(vizinho)

                fila.append(vizinho)

                pais[vizinho] = no

```

Nesse trecho criamos um``` for ```que seja capaz de iterar sobre todos os vizinhos da cidade atual (```no```). A variável ```vizinho```representa cada uma das cidades vizinhas à cidade atual. Na segunda linha, no bloco condicional é verificado se o vizinho atual ainda não foi visitado. Se a cidade vizinha ainda não estiver na lista de cidades visitadas (```visitados```), isso significa que ainda não exploramos essa cidade durante a busca. Portanto, este bloco de código é executado apenas se o ```vizinho``` não estiver na lista de ```visitados```, o que evita revisitar cidades que já foram exploradas. Se o vizinho ainda não foi visitado, as ações dentro deste bloco condicional serão executadas. Isso inclui adicionar o ```vizinho``` à lista de ```visitados```, à fila de exploração e registrar o "pai" do vizinho no dicionário ```pais```, conforme explicado anteriormente.

```

 if not encontrado:
        print("Caminho não encontrado")

```

Caso não seja encontrado um ```caminho``` válido até o destino, este bloco condicional verifica se a variável ```encontrado``` é falsa. Nesse caso, a mensagem "Caminho não encontrado" é impressa na tela para informar ao usuário que não há um caminho.
```
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

```

Nesta parte, estamos solicitando ao usuário que insira a cidade de origem e a cidade de destino, que serão armazenadas nas variáveis ```inicio``` e ```fim```, respectivamente, utilizando a função ```input()```. Em seguida, inicializamos a variável ```contador``` com o valor 0. Depois disso, entramos em um loop ```for``` que itera sobre todas as chaves (cidades) no grafo. Para cada cidade no no grafo, verificamos se ela é igual à cidade de origem (```inicio```) ou à cidade de destino (```fim```). Se a cidade for igual a uma das duas, incrementamos o ```contador``` em 1. Após percorrer todas as cidades no grafo, o ```contador``` conterá o número de cidades que correspondem à cidade de origem ou à cidade de destino. Se o contador for igual a 2, significa que tanto a cidade de origem quanto a cidade de destino foram encontradas no grafo.
```
if contador == 2:
    busca_em_largura(grafo, inicio, fim)
else:
    print("Cidade não encontrada")

```

Portanto, aqui estamos verificando se o ```contador``` é igual a 2. Se for, chamamos a função ```busca_em_largura(grafo, inicio, fim)```, passando o grafo e as cidades de origem e destino como argumentos. Caso contrário, imprimimos uma mensagem informando que uma das cidades não foi encontrada no grafo.
