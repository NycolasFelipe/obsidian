O objetivo desta abordagem é darmos continuidade aos nossos estudos de programação com linguagem Python.  
Ao longo deste conteúdo, você aprenderá a criar códigos que tomam decisões. Ou seja, dependendo de uma condição existente nele, as instruções executadas poderão ser distintas.

##### Estruturas condicionais

É muito comum na programação, precisarmos que determinado bloco de código seja executado apenas se determinada condição for satisfeita. Para esses casos, Python disponibiliza formas de se controlar o fluxo de execução de programas: são as chamadas ==estruturas condicionais IF/ELIF/ELSE==.

**Estrutura condicional if**
Sua sintaxe é bem simples, bastando utilizarmos `if` seguido pela `condicao` seguido por dois pontos. Veja o exemplo a seguir:

```python
valor = 10

if valor > 5:
    print('O valor é maior que 5.')

```

Neste caso, a condição está testando se o valor presente na variável `valor` é maior que 5. Caso isso aconteça, a linha de código abaixo será executada.

Como 10 é maior que 5 o bloco de código resulta em:

```text
O valor é maior que 5.
```

Caso você precise que um bloco de código seja sempre executado, basta adicionar `True` à condição:

```python
if True:
    print("Este bloco sempre irá ser executado.")
```

Resultado do código acima:

```text
Este bloco sempre irá ser executado.
```

**Estrutura condicional if/else**
Vimos na seção acima que o `if` executa um bloco de código se sua condição for atendida, mas e se ela não for atendida e você deseja realizar outra ação? Basta utilizarmos a estrutura condicional else.

Com ela, toda vez que uma condição não for atendida, o Python executará o bloco de código definido abaixo da cláusula `else`. Vamos esclarecer no exemplo abaixo:

```python
idade = 20

if idade < 17:
    print('A idade é MENOR que 17')
else:
    print('A idade é MAIOR que 17')

```

Neste caso, a condição testa se o valor da variável `idade` é menor que 17. Porém, como 17 é menor que 20, o bloco `else` é então executado, resultando em:

```text
A idade é MAIOR que 17
```

**Estrutura condicional if/elif/else**
O `elif` é utilizando quando mais de uma condição `if` precisa ser testada. Exemplo:

```python
linguagem = "Python"

if linguagem == "C++":
    print('C++ é uma linguagem de programação compilada.')
elif linguagem == "Python":
    print("Python é uma linguagem de programação de alto nível")
elif linguagem == "Java":
    print("Java é uma linguagem de programação amplamante utilizada no mercado")
else:
    print('Não é nenhuma das duas opções')
```

Neste exemplo, estamos verificando o valor da variável `linguagem` em diversos testes. Note que a saída abaixo é exatamente o resultado da execução do `elif`, já que a o valor da variável `linguagem` é igual à “Python”:

```text
Python é uma linguagem de programação de alto nível
```

**Estrutura condicional ternária (if em uma linha)**
Python provê uma forma concisa de se testar valores com apenas uma linha de código. São os chamados if-ternários, ou condições ternárias, ou operadores ternários. Veja um exemplo:

```python
velocidade = 75
resultado = 'Multado' if velocidade > 60 else 'Dentro do limite'
print(resultado)
```

Nesse caso, está sendo verificado se o valor da variável `velocidade` é maior que 60 e:
- Caso a condição seja verdadeira a variável `resultado` receberá o valor `Multado`;
- Caso a condição seja falsa, a variável `resultado` receberá o valor `Dentro do limite`.

Dessa forma, obtemos o resultado abaixo:

```text
Multado
```

**Estruturas de repetição com estruturas condicionais**
Podemos juntar as Estruturas de Repetição com as Estruturas Condicionais, que alias trabalham muito bem juntas. Veja um exemplo dessas estruturas trabalhando em conjunto:

```python
for numero in range(1, 5):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')
```

Resultado do código acima:

```text
O número 1 é impar
O número 2 é par
O número 3 é impar
O número 4 é par
```

**List Comprehensions com if**
Outro lugar onde podemos utilizar as Estruturas Condicionais são nas chamadas List Comprehensions do Python. 

Suponha que te peçam para escrever um código que retorne apenas os números pares de uma sequência de 0 a 10. Podemos fazer isso com apenas 1 linha de código:

```python
list_comp = [numero for numero in range(0, 11) if numero % 2 == 0]
```

Resultado do código acima:

```text
[0, 2, 4, 6, 8, 10]
```


##### Expressões lógicas e álgebra booleana

Os Operadores em Python possibilitam que o desenvolvedor consiga transcrever a lógica para código. 

Python disponibiliza uma série desses operadores para os desenvolvedores e é muito importante dominá-los. Veremos todos em detalhes agora.

**Operadores aritméticos**
Esses operadores são utilizados para criarmos expressões matemáticas comuns, como soma, subtração, multiplicação e divisão.

| Operador | Nome            | Função                                                                  |
| -------- | --------------- | ----------------------------------------------------------------------- |
| `+`      | Adição          | Realiza a soma de ambos operandos.                                      |
| `-`      | Subtração       | Realiza a subtração de ambos operandos.                                 |
| `*`      | Multiplicação   | Realiza a multiplicação de ambos operandos.                             |
| `/`      | Divisão         | Realiza a Divisão de ambos operandos.                                   |
| `//`     | Divisão inteira | Realiza a divisão entre operandos e a parte decimal de ambos operandos. |
| `%`      | Módulo          | Retorna o resto da divisão de ambos operandos.                          |
| `**`     | Exponenciação   | Retorna o resultado da elevação da potência pelo outro.                 |

**Operadores de comparação**
Como o nome já diz, esses Operadores são usados para comparar dois valores:

|Operador|Nome|Função|
|---|---|---|
|`==`|Igual a|Verifica se um valor é igual ao outro|
|`!=`|Diferente de|Verifica se um valor é diferente ao outro|
|`>`|Maior que|Verifica se um valor é maior que outro|
|`>=`|Maior ou igual|Verifica se um valor é maior ou igual ao outro|
|`<`|Menor que|Verifica se um valor é menor que outro|
|`<=`|Menor ou igual|Verifica se um valor é menor ou igual ao outro|

**Operadores de atribuição**
Esse operadores são utilizados no momento da atribuição de valores à variáveis e controlam como a atribuição será realizada.

Veja quais Operadores de Atribuição estão disponíveis em Python:

|Operador|Equivalente a|
|---|---|
|`=`|x = 1|
|`+=`|x = x + 1|
|`-=`|x = x - 1|
|`*=`|x = x * 1|
|`/=`|x = x / 1|
|`%=`|x = x % 1|

**Operadores lógicos**
Esses operadores nos possibilitam construir um tipo de teste muito útil e muito utilizado em qualquer programa Python: os testes lógicos.

Python nos disponibiliza três tipos de Operadores Lógicos: o `and`, o `or` e o `not`.

|Operador|Definição|
|---|---|
|`and`|Retorna True se ambas as afirmações forem verdadeiras|
|`or`|Retorna True se uma das afirmações for verdadeira|
|`not`|retorna Falso se o resultado for verdadeiro|
Exemplo da utilização de cada um:

```python
num1 = 7
num2 = 4

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')
```

**Operadores de identidade**
Estes operadores são utilizados para comparar objetos, verificando se os objetos testados referenciam o mesmo objeto (is) ou não (is not).

|Operador|Definição|
|---|---|
|`is`|Retorna `True` se ambas as variáveis são o mesmo objeto|
|`is not`|Retorna `True` se ambas as variáveis não forem o mesmo objeto|
Agora vamos aos exemplos de como utilizar cada operador de identidade mencionado acima:

```python
# Exemplo 1: Operador is
lista = [1, 2, 3]
outra_lista = [1, 2, 3]
recebe_lista = lista

# Retorna True, pois são o mesmo objeto
print(f"São o mesmo objeto? {lista is recebe_lista}")

# Retorna False, pois são objetos diferentes
print(f"São o mesmo objeto? {lista is outra_lista}")

# Exemplo 2: Operador is not
tupla = (1, 2, 3)
outra_tupla = (1, 2, 3)

print(f"Os objetos são diferentes? {outra_tupla is tupla}")
# Retorna True
```

**Operadores de associação**
Por último, temos os operadores de associação.

Eles servem para verificar se determinado objeto está associado ou pertence a determinada estrutura de dados.

|Operador|Função|
|---|---|
|`in`|Retorna `True` caso o valor seja encontrado na sequência|
|`not in`|Retorna `True` caso o valor não seja encontrado na sequência|
Exemplo da utilização de cada operador de associação mencionado acima:

```python
lista = ["Python", 'Academy', "Operadores", 'Condições']

# Verifica se existe a string dentro da lista
print('Python' in lista)  # Saída: True

# Verifica se não existe a string dentro da lista
print('SQL' not in lista) # Saída: True
```

##### Fonte

[Python Academy: Estruturas Condicionais no Python](https://pythonacademy.com.br/blog/estruturas-condicionais-no-python)
[Python Academy: Operadores Aritméticos e Lógicos em Python](https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python)
