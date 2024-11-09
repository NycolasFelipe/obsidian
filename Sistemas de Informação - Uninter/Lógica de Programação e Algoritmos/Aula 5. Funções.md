Ao longo desta etapa você irá aprender um recurso bastante utilizado e aplicado em qualquer linguagem de programação, o de modularização de códigos.  
Iremos investigar em linguagem Python como criamos funções. Com elas, poderemos criar rotinas em nossos códigos que irão atender por um nome, deixando nosso código mais legível, simples, e útil.

##### Funções

==Funções são rotinas de códigos que podem ser executadas quando tem seu nome invocado dentro do programa==. Funções trabalham com o conceito de abstração e têm como finalidade abstrair comandos complexos em uma única chamada. Existem funções que são pré-definidas pela linguagem de programação, como a função `print`. Toda e qualquer função contém dentro de si um algoritmo que serve para resolver uma tarefa menor dentro do programa.

O motivo pelo qual utilizamos funções é para ==facilitar o desenvolvimento de nossos códigos, bem como deixá-los mais portáveis==. Porém, não existem funções predefinidas para resolver todo e qualquer problema que tenhamos em nossos algoritmos. Sendo assim, podemos criar nossas próprias rotinas (funções) para solucionar nossos problemas particulares. ==O ato de criar rotinas é também conhecido como modularização de código (criar módulos).==

A sintaxe de uma função é definida por três partes: **nome, parâmetros e corpo**, o qual agrupa uma sequência de linhas que representa algum comportamento. No código abaixo, temos um exemplo de **declaração de função em Python**:

```python
def hello(meu_nome):
	print("Olá", meu_nome)
```

Para executar a função, de forma semelhante ao que ocorre em outras linguagens, devemos simplesmente chamar seu nome e passar os parâmetros esperados entre parênteses, conforme o código a seguir.

```python
>>> hello('Fabio')
Olá Fabio
>>> meu_nome
'Fabio'
```

**Parâmetros nomeados**
As funções em Python tem suporte a parâmetros nomeados. O exemplo a seguir mostra um caso onde podemos usar nomes nos parâmetros da função.

```python
def calculo_imc(peso, altura):
    print(peso / altura ** 2)

calculo_imc(75, 1.68)
```

Observe que quando chamamos a função calculo_imc, não há uma identificação do que cada valor representa dentro daquela função. Nesse mesmo exemplo usando essa funcionalidade, conseguimos ver melhor como podemos dar nome aos parâmetros.

```python
def calculo_imc(peso, altura):
    print(peso / altura ** 2)

calculo_imc(peso = 75, altura = 1.68)
```

**Parâmetros opcionais**
É possível escrever funções definidas pelos programadores com argumentos opcionais, também. Por exemplo, aqui está uma função que exibe as palavras mais comuns em um histograma:

```python
def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep='\\t')
```

O primeiro parâmetro é necessário; o segundo é opcional. O valor padrão de num é 10.

```python
print_most_common(hist)
print_most_common(hist, 20)
```


##### Escopo de variáveis

==O escopo de uma variável se refere ao local onde uma variável é definida e onde ela pode ser acessada==. Em Python, existem quatro tipos de escopos: local, enclosing, global e built-in.

**Escopo local**
 Uma variável definida dentro de uma função é chamada de variável local. Ela só pode ser acessada dentro dessa função.
 
```python
def funcao():
  x = 10  # Variável local
  print(x)

funcao()  # Saída: 10
print(x)  # Erro: x não está definido
```

**Escopo enclosing**
Se uma função está dentro de outra função (função aninhada), a função interna tem acesso às variáveis da função externa. Este é o escopo enclosing.

```python
def funcao_externa():
  x = 10  # Variável da função externa

  def funcao_interna():
    print(x)  # Acesso à variável da função externa
  
  funcao_interna()  # Saída: 10
funcao_externa()
```

**Escopo global**
Uma variável definida fora de todas as funções é uma variável global e pode ser acessada em qualquer lugar do programa.

```python
x = 10  # Variável global

def funcao():
  print(x)  # Acesso à variável global

funcao()  # Saída: 10
print(x)  # Saída: 10
```

**Escopo built-in**
São nomes pré-definidos no módulo builtins do Python. Eles são sempre acessíveis.
```python
print(len('Python')) # len é uma função built-in
```

Lembre-se, Python segue a regra **LEGB** para resolver os nomes das variáveis. ==Primeiro, verifica o escopo Local, depois o Enclosing, depois o Global e finalmente o Built-in.==


##### Retorno de valores em funções

Em Python, ==o comando **return** é usado para encerrar a execução de uma função e enviar um valor de volta para o chamador==. Quando uma função é chamada e encontra o comando **return**, ela retorna imediatamente ao local de chamada, levando consigo o valor especificado. Isso ==permite que o valor seja utilizado ou armazenado para uso posterior no programa.==

**Função simples**
Vamos começar com um exemplo básico de uma função que utiliza o **return** para retornar a soma de dois números.

```python
def somar(a, b):
	resultado = a + b
	return resultado

# Chamada da função e impressão do resultado
resultado_soma = somar(3, 5)
print("A soma é:", resultado_soma)
```

Neste exemplo, a função **somar** retorna o resultado da adição de **a** e **b**. O valor retornado é então impresso no console.

**Decisões com return**
O return pode ser usado para interromper a execução da função antes do final, dependendo de certas condições.

```python
def calcular_desconto(total, cupom):
  if cupom == "DESC10":
      desconto = total * 0.1
      return desconto
  else:
      return 0

# Chamada da função e impressão do desconto
desconto_final = calcular_desconto(100, "DESC10")
print("Desconto aplicado:", desconto_final)
```

Neste caso, se o cupom for "DESC10", a função retorna um desconto de 10%, caso contrário, retorna 0.

**Múltiplos valores com return**
==O return também pode ser utilizado para retornar múltiplos valores em forma de tupla.==

```python
def calcular_media_notas(notas):
	quantidade = len(notas)
	soma = sum(notas)
	media = soma / quantidade
	return quantidade, soma, media

# Chamada da função e desempacotamento dos valores retornados
qtd, soma, media = calcular_media_notas([8, 9, 7, 10, 8])
print(f"Quantidade de notas: {qtd}, Soma: {soma}, Média: {media}")
```

Aqui, a função retorna três valores, que são desempacotados na chamada da função para serem utilizados individualmente.

##### Tratamento de exceções

O tratamento eficiente de erros é um aspecto fundamental no desenvolvimento de software, especialmente em uma linguagem versátil como Python.

**Entendendo Erros e Exceções**
Antes de mergulhar nas técnicas de tratamento de erros, é crucial entender os tipos comuns de erros em Python:

1. **SyntaxError**: Erros de sintaxe ocorrem quando o código não segue a gramática da linguagem.
2. **NameError**: Surge quando uma variável ou função não é reconhecida.
3. **TypeError**: Acontece ao aplicar uma operação a um tipo inapropriado de objeto.
4. **IndexError e KeyError**: Relacionados ao acesso de elementos em coleções, como listas e dicionários, com chaves ou índices inexistentes.
5. **ValueError**: Ocorre quando uma função recebe um argumento correto em tipo, mas inadequado em valor.
6. **AttributeError**: Surge ao tentar acessar um atributo ou método inexistente.
7. **ZeroDivisionError**: Erro ao dividir um número por zero.

**Utilizando Try e Except**
O método mais básico em Python para o tratamento de exceções é o uso dos blocos `try` e `except`.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
```

**Tratando Múltiplas Exceções**
Para garantir que seu código esteja preparado para lidar com diferentes tipos de erros, você pode definir múltiplos blocos `except`.

```python
try:
    # código
except ZeroDivisionError:
    # tratamento para ZeroDivisionError
except TypeError:
    # tratamento para TypeError
```

**Blocos Else e Finally**
- **Else**: Executado se nenhuma exceção for capturada no bloco `try`.
- **Finally**: Sempre executado, independentemente de uma exceção ocorrer ou não.

```python
try:
    # código
except TipoDeErro:
    # tratamento da exceção
else:
    # executado se não houver exceção
finally:
    # sempre executado
```

**Levantando Exceções**
Python permite que você também levante suas próprias exceções usando `raise`.

```python
if condicao_inadequada:
    raise ValueError("Descrição do erro")
```

**Criando Exceções Personalizadas**
Para situações específicas, pode ser útil criar exceções personalizadas.

```python
class MinhaExcecao(Exception):
    pass

raise MinhaExcecao("Erro específico")
```

==O tratamento adequado de erros e exceções em Python é essencial para o desenvolvimento de software de qualidade==. Ao adotar estas práticas, você não só aumenta a robustez e a confiabilidade do seu código, mas também facilita a manutenção e a compreensão por outros desenvolvedores.



##### Funções Lambda

A linguagem Python permite que criemos ==funções mais simples, sem nome, chamadas de funções lambda==. Elas podem ser escritas em uma só linha de código e dentro do programa principal. Uma função lambda é utilizada quando o código da função é muito simples ou utilizado poucas vezes, e é um recurso existente em diversas outras linguagens de programação. Vejamos um exemplo.

```python
res = lambda x: x * x
print(res(3))
# output: 9
```

```python
soma = lambda x, y: x + y
print(soma(3, 5))
# output: 8
```



##### Fontes

[DevMedia: Funções em Python](https://www.devmedia.com.br/funcoes-em-python/37340)
[Pense em Python: 13.5 - Parâmetros opcionais](https://pense-python.caravela.club/13-estudo-de-caso-selecao-de-estrutura-de-dados/05-parametros-opcionais.html)
[Heitor Bisneto: Escopo de Variáveis em Python](https://medium.com/@BisnetoDev/escopo-de-vari%C3%A1veis-em-python-8ba90bc99005)
[Dio: Desvendando o Poder do 'return' em Python](https://www.dio.me/articles/desvendando-o-poder-do-return-em-python-uma-jornada-pela-manipulacao-de-funcoes)
[Rocketseat: Tratamento de Erros em Python na prática](https://blog.rocketseat.com.br/tratamento-de-erros-em-python-na-pratica/)
