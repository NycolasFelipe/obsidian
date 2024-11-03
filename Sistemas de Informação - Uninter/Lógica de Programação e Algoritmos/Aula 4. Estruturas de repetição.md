Ao longo desta etapa você irá aprender a criar códigos com repetição de instruções, também chamado de códigos iterativos. Ou seja, algumas partes dos nossos algoritmos poderão ser repetidas diversas vezes, até que uma determinada condição seja satisfeita e finalize o bloco de repetição.

As estruturas de repetição são recursos das linguagens de programação responsáveis por executar um bloco de código repetidamente através de determinadas condições especificas.

O Python contém dois tipos de estruturas de repetição: `for` e `while`.

##### Loops utilizando **for**

O `for` é utilizado para **percorrer** ou **iterar** sobre uma sequência de dados (seja esse uma lista, uma tupla, uma string), executando um **conjunto de instruções** em cada item.

Sua sintaxe básica é: `for <nome variável> in <iterável>`. Vamos entender:
- `<nome variável>` é o nome da variável que vai receber os elemento de `<iterável>`.
- `<iterável>` é o container de dados sobre o qual vamos iterar, podendo ser: uma lista, uma tupla, uma string, um dicionário, entre outros.

Exemplo:
```python
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)
```

Existe outra forma de se utilizar o `for` que é utilizando a estrutura `for/else`. 

Adicionar o `else` ao final do `for` nos possibilita executar um bloco de código após o iterável ter sido **completamente** percorrido.

Exemplo:
```python
for item in sequencia:
    print(item)
else:
    print('Todos os items foram exibidos com sucesso')
```

**Percorrendo dicionários**
Podemos também percorrer os dicionários do Python. Para isso, podemos fazer da seguinte maneira:

```python
notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}

for chave, valor in notas.items():
    print(f"{chave}: {valor}")

# Resultado:
# Potuguês: 7
# Matemática: 9
# Lógica: 7
# Algoritmo: 7
```

**Percorrendo strings**
Também podemos percorrer strings, pois elas também são um tipo iterável:

```python
for caractere in 'Python':
    print(caractere)
    
# Resultado:
# P
# y
# t
# h
# o
# n
```


##### Loops utilizando **while**

O `while` é uma estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado enquanto determinada condição for satisfeita. 

Sua sintaxe básica é:

```python
while <condição>:
    # Bloco a ser executado
```

Aqui, `<condição>` é uma expressão que pode ser reduzida a `True` ou `False`, podendo ser:
- A verificação do valor de uma variável;
- Determinada estrutura de dados alcançar um tamanho;
- O retorno de uma função se igualar a determinado valor;
- Algum valor externo ser alterado (por exemplo um valor armazenado em Banco de Dados).

Exemplo:

```python
contador = 0

while contador < 3:
    print(f'Valor do contador é {contador}')
    contador += 1

# Resultado:
# Valor do contador é 1
# Valor do contador é 2
# Valor do contador é 3
```


##### Auxiliadores

Existem 3 comandos que nos auxiliam quando queremos alterar o fluxo de uma estrutura de repetição. São eles: `break`, `continue` e `pass`.

Esses auxiliares não funcionam diretamente com o `while`, e por isso encaixar eles no bloco principal do while pode ser tanto quanto inútil, já que a condição especificada encerra o loop.

**Break**
É usado para finalizar um loop, isto é, é usado para parar sua execução. Geralmente vem acompanhado de alguma condição para isso, com um `if`.

Exemplo:

```python
# Exemplo com for
for num in range(10):
    # Se o número for igual a = 5, devemos parar o loop
    if num == 5:
        # Break faz o loop finalizar
        break
    else:
        print(num)

# Exemplo com while
num = 0
while num < 5:
    num += 1
    if num == 3:
        break
        
    print(num)
```

**Continue**
Funciona de maneira similar ao `break`, contudo ao invés de encerrar o loop ele pula todo código que estiver abaixo dele (dentro do loop) partindo para a próxima iteração.

Exemplo:

```python
for num in range(5):
    if num == 3:
        print("Pular instruções restantes")
        # Executa o continue, pulando para o próximo laço
        continue
    else:
        print(num)
```

**Pass**
O `pass` nada mais é que uma forma de fazer um código que não realiza operação nenhuma.

Como os escopos de Classes, Funções, If/Else e loops `for`/`while` são definidos pela indentação do código (e não por chaves `{}` como geralmente se vê em outras linguagens de programação), ==usamos o `pass` para dizer ao Python que o bloco de código está vazio==.

Exemplo:

```python
for item in range(5000):
    pass

while False:
    pass

class Classe:
    pass

if True:
    pass
else:
    pass

def funcao():
    pass
```


##### Fonte

[Python Academy: Loops e Estruturas de Repetição no Python](https://pythonacademy.com.br/blog/estruturas-de-repeticao)
