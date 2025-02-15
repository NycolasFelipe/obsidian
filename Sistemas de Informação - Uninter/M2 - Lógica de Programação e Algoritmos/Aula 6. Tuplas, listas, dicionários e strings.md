Ao longo desta abordagem, vamos aprender a trabalhar com variáveis compostas em Python, por meio dos três principais tipos existentes na linguagem: as tuplas, as listas e os dicionários.  
Vamos investigar em linguagem Python as caracteristicas e diferenças de cada uma, assim como criar e manipular todas elas. No último tópico, vamos aprender mais alguns recursos de manipulação de strings para consolidar o nosso conhecimento.

##### Tuplas

Em Python, as ==tuplas são uma das estruturas de dados fundamentais==, ao lado das listas. Enquanto ambas podem parecer semelhantes à primeira vista, elas têm características e usos distintos.

**O que são tuplas**
==São coleções ordenadas e imutáveis==. São definidas por parênteses `()` e podem conter elementos de diferentes tipos. Aqui, `minha_tupla` é uma tupla contendo um inteiro, uma string e um número de ponto flutuante.

```python
minha_tupla = (1, "hello", 3.14)
```

**Acessando elementos da tupla**
Similarmente às listas, os elementos da tupla são acessados através de índices. Este trecho acessa o primeiro elemento de `minha_tupla`.

```python
primeiro_elemento = minha_tupla[0]  # 1
```

**Imutabilidade das tuplas**
==A principal diferença entre tuplas e listas é que as tuplas são imutáveis==. Isso significa que, uma vez criadas, seus elementos não podem ser alterados.

Tentar alterar um elemento de uma tupla resulta em erro.

```python
minha_tupla[0] = 2  # Isto resultará em um erro
```

**Quando usar as tuplas?**
As tuplas são especialmente úteis em diversas situações na programação Python:

**Armazenamento de Dados Constantes:** Dados que não devem ser alterados após sua criação, como configurações de um sistema ou valores fixos de referência.

**Retorno Múltiplo de Funções:** Em Python, as funções podem retornar múltiplos valores em forma de tuplas.

```python
def get_min_max(numeros): 
	return min(numeros), max(numeros)
```

> Esta função retorna o valor mínimo e máximo de uma lista de números.

**Desempacotamento:** As tuplas permitem o desempacotamento, o que é útil na atribuição múltipla.

```python
a, b = (1, 2)
```

> Aqui, **a** recebe **1** e **b** recebe **2**.

**Uso como Chaves de Dicionários:** Devido à sua imutabilidade, as tuplas podem ser usadas como chaves em dicionários.

```python
dicionario = {(1, 2): "ponto", (3, 4): "outro ponto"}
```


**Métodos Disponíveis para Tuplas**
Apesar de sua imutabilidade, as tuplas oferecem alguns métodos úteis:

**count():** Conta quantas vezes um elemento aparece na tupla. Conta quantas vezes `1` aparece em `minha_tupla`.

```python
contador = minha_tupla.count(1)

```

**index():** Encontra o índice do primeiro elemento igual ao valor especificado. Encontra o índice de `"hello"` em `minha_tupla`.

```python
indice = minha_tupla.index("hello")
```

**Comparação entre Tuplas e Listas**

**Semelhanças:** Ambas são coleções ordenadas que podem conter diferentes tipos de elementos.

**Diferenças:**
- **Mutabilidade:** Listas são mutáveis, enquanto tuplas são imutáveis.
- **Performance:** Tuplas têm um tempo de processamento mais rápido.
- **Uso:** Listas são ideais para coleções que podem mudar ao longo do tempo. Tuplas são usadas para dados que não devem ser alterados.

**Conversão entre Tuplas e Listas**
É possível converter uma lista em uma tupla e vice-versa.

```python
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
lista_convertida = list(tupla_convertida)
```


##### Listas

As listas são estruturas de dados fundamentais em Python, usadas para armazenar sequências de itens.

**Criação de Listas em Python**
Uma lista é criada com colchetes `[]` e pode conter elementos de diferentes tipos. Aqui, `minha_lista` é uma lista que contém um inteiro, uma string e um número de ponto flutuante.

```python
minha_lista = [1, "Hello", 3.14]
```


**Acessando Elementos da Lista**
Elementos de uma lista são acessados através de índices, começando do zero.

Este código acessa o primeiro elemento de `minha_lista`, que é `1`.

```python
primeiro_elemento = minha_lista[0]  # 1
```

**Principais Métodos de Listas**

`append():` Adiciona um elemento ao final da lista. 
> Exemplo: Adiciona a string `"Python"` ao final de `minha_lista`.

```python
minha_lista.append("Python")
```

`extend()`: Adiciona elementos de outra lista ao final.
> Exemplo: Estende `minha_lista` adicionando elementos de `outra_lista`.

```python
outra_lista = [2, 4]
minha_lista.extend(outra_lista)
# ou também: minha_lista += outra_lista
```

`insert()`: Insere um elemento em uma posição específica.
>Exemplo: Insere a string `"world"` na posição 1 de `minha_lista`.

```python
minha_lista.insert(1, "world")
```

`remove()`: Remove o primeiro elemento igual ao valor especificado.
>Exemplo: Remove a primeira ocorrência de `"Hello"` de `minha_lista`.

```python
minha_lista.remove("Hello")
```

`pop()`: Remove e retorna o elemento de uma posição específica.
>Exemplo: Remove e retorna o elemento na posição 0, neste caso, `1`.

```python
removido = minha_lista.pop(0)
```

`clear()`: Remove todos os elementos da lista.
>Exemplo: Limpa todos os elementos de `minha_lista`.

```python
minha_lista.clear()
```

`index()`: Retorna o índice do primeiro elemento igual ao valor especificado.
>Exemplo: Retorna o índice de `3.14` em `minha_lista`.

```python
indice = minha_lista.index(3.14)
```

`count()`: Conta quantas vezes um elemento aparece na lista.
>Exemplo: Conta quantas vezes `"Python"` aparece em `minha_lista`.

```python
contador = minha_lista.count("Python")
```

`sort()`: Ordena os elementos da lista.
>Exemplo: Ordena a lista `numeros` em ordem crescente.

```python
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
```

`reverse()`: Inverte a ordem dos elementos na lista. Este código inverte a ordem dos elementos em `numeros`, reorganizando a lista na ordem inversa.

```python
numeros.reverse()
```


**Iterando sobre listas**
É possível percorrer cada elemento de uma lista utilizando um loop `for`. Aqui imprimimos cada elemento de `minha_lista`.

```python
for item in minha_lista:
    print(item)
```


**List comprehensions**
List comprehensions oferecem uma maneira concisa de criar listas a partir de listas existentes.

No exemplo no abaixo o código cria uma nova lista `quadrados` contendo os quadrados dos números de 0 a 9.

```python
quadrados = [x**2 for x in range(10)]
```


##### Dicionários
No mundo da programação Python, os dicionários, ou 'dicts', são ferramentas incrivelmente poderosas e flexíveis. Eles permitem armazenar e gerenciar dados de maneira organizada e acessível.

**O que são dicionários?**
==São coleções desordenadas de itens==. Enquanto outras coleções, como listas e tuplas, são indexadas por uma faixa de números, os ==dicionários são indexados por chaves, que podem ser de qualquer tipo imutável==. Cada par chave-valor em um dicionário é separado por vírgulas e todo o conjunto é colocado entre chaves `{}`.

Exemplo:
```python
meu_dict = {'nome': 'Alice', 'idade': 25}
```

**Criando dicionários:**
A criação de um dicionário é simples. Você pode iniciar um dicionário vazio ou com alguns pares chave-valor.

Exemplo:
```python
# Dicionário vazio
dict_vazio = {}

# Dicionário com dados iniciais
dict_preenchido = {'nome': 'Carlos', 'idade': 30}
```

**Acessando elementos em um dicionário:**
Você pode acessar o valor associado a uma chave específica usando a sintaxe de colchetes `[]`.

Exemplo:
```python
nome = dict_preenchido['nome']
print(nome)  # Saída: Carlos
```

> Se tentar acessar uma chave que não existe, um erro será gerado. Para evitar isso, use o método `get`.

Exemplo:
```python
profissao = dict_preenchido.get('profissao', 'Não especificado')
print(profissao)  # Saída: Não especificado
```

**Adicionando e modificando elementos**
Adicionar ou modificar elementos em um dicionário é simples: basta atribuir um novo valor a uma chave existente ou criar uma nova chave.

Exemplo:
```python
# Modificando um elemento existente
dict_preenchido['idade'] = 31

# Adicionando um novo elemento
dict_preenchido['profissao'] = 'Engenheiro'
```

**Removendo elementos de um dicionário:**
Utilize o método `pop` para remover um item pelo nome da chave ou a palavra-chave `del` para remover itens ou o dicionário inteiro.

Exemplo:
```python
# Removendo um elemento específico
idade = dict_preenchido.pop('idade')

# Removendo todo o dicionário
del dict_preenchido
```

**Métodos úteis em dicionários:**
Python oferece vários métodos úteis para trabalhar com dicionários, como `keys()`, `values()` e `items()`.

Exemplo:
```python
# Obtendo todas as chaves
chaves = dict_preenchido.keys()
print(chaves)  # Saída: dict_keys(['nome', 'profissao'])

# Obtendo todos os valores
valores = dict_preenchido.values()
print(valores)  # Saída: dict_values(['Carlos', 'Engenheiro'])
```

**Iteração em dicionários:**
Você pode iterar sobre um dicionário usando um loop `for`. Isso é útil para acessar cada par chave-valor.

Exemplo:
```python
for chave, valor in dict_preenchido.items():
    print(f"{chave}: {valor}")
```

**Dicionários aninhados:**
Dicionários aninhados são dicionários dentro de outros dicionários. Eles são úteis para representar dados mais complexos.

Exemplo:
```python
familia = {
    'pai': {'nome': 'Roberto', 'idade': 50},
    'mãe': {'nome': 'Marta', 'idade': 48}
}
```

Os dicionários são estruturas de dados extremamente versáteis e úteis em Python. Eles são ideais para armazenar dados de forma organizada e eficiente, facilitando o acesso e a manipulação dos dados.


##### Trabalhando com métodos em strings

**Métodos para validação de dados em strings**
![[Pasted image 20241109141802.png]]

**Métodos para uso com strings**
![[Pasted image 20241109141903.png]]

#### Fontes

[Rocketseat: Python: Como funcionam as Tuplas?](https://blog.rocketseat.com.br/como-funcionam-as-tuplas-no-python/)
[Rocketseat: Python: Listas e Seus Principais Métodos](https://blog.rocketseat.com.br/listas-no-python-e-seus-principais-metodos/)
[Rocketseat: # Como usar dicionários (dicts) no Python?](https://blog.rocketseat.com.br/como-usar-dicionarios-dicts-no-python/)