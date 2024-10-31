O objetivo desta abordagem é darmos nossos primeiros passos com a linguagem Python. Iremos começar a desenvolver nossos próprios algoritmos, enquanto aprendemos, de maneira dinâmica, os primeiros recursos dessa poderosa linguagem de programação.

##### Ciclo de processamento de dados

Todo e qualquer programa computacional é um algoritmo e contempla os três blocos apresentados a seguir.

**Entrada**
==É a maneira como as informações são inseridas no programa==. A entrada padrão adotada em programas computacionais é a inserção de dados via teclado. Porém, é possível que os dados cheguem ao programa de outra maneira, como conexão de rede, ou de outro programa executando na própria máquina.

**Processamento**
Representa a ==execução das instruções e envolve cálculos aritméticos, lógicos, alterações de dados etc==.; em suma, tudo que é executado de alguma maneira pela unidade central de processamento (CPU) e gravado ou buscado na memória.

**Saída**
Após o processamento das instruções, é necessário que o ==resultado do nosso programa seja disponibilizado ao usuário de alguma maneira==. A saída padrão adotada em um programa computacional é uma tela/display onde as informações podem ser exibidas. Porém, é possível que nossa saída seja o envio de dados via conexão de rede ou a impressão de um documento numa impressora.

O fluxo de execução de um algoritmo sempre se dá da esquerda para a direita. Primeiramente, obtemos os dados de entrada do programa, dados esses usados ao longo de toda a execução do algoritmo. Em seguida, com os dados obtidos, os processamos no hardware da máquina gerando uma saída, normalmente em um monitor/tela.

![[Pasted image 20241031131850.png]]

##### Operadores e operações matemáticas

Lista de operadores matemáticos em Python e em pseudocódigo:

| Python | Operação                          |
| ------ | --------------------------------- |
| +      | Adição                            |
| -      | Subtração                         |
| *      | Multiplicação                     |
| /      | Divisão (com as casas decimais)   |
| //     | Divisão (somente a parte inteira) |
| %      | Módulo/resto da divisão           |
| **     | Exponenciação ou potenciação      |

##### Variáveis, dados e seus tipos
Aprendemos anteriormente que um computador contém uma memória de acesso aleatório (RAM). Desse modo, ==todo e qualquer programa computacional==, quando em execução, ==recebe do sistema operacional um espaço, na memória, destinado à sua execução e armazena seus dados nessa região==. Porém, o que são os dados?

Sandra Puga e Gerson Risseti (2016, p. 18) definem um dado como sendo uma sequência de símbolos quantificados ou quantificáveis. ==Dados são valores fornecidos pela entrada do programa== e que podem ser obtidos via usuário, ou processamento, e que ==são manipulados ao longo de toda a execução do algoritmo==. Dados devem ser armazenados em variáveis.

Vamos imaginar a memória do computador como uma grande estante cheia de gavetas. Cada gaveta é representada por um nome de identificação, o qual chamamos de variável. ==Uma variável é, portanto, um nome dado a uma região da memória do programa==. Sempre que você evocar o nome de uma variável, seu respectivo bloco de memória será automaticamente carregado da RAM e manipulado pela CPU.

==Utilizamos variáveis em todos os nossos algoritmos, com o objetivo de armazenar os dados em processamento, ao longo de nosso programa==. As variáveis apresentam tipos, e cada tipo exibe características distintas de operação e manipulação. Iremos investigar um pouco mais esses tipos ao longo deste tópico. De acordo com nossa bibliografia, citamos três tipos de variáveis denominados de ==tipos primitivos de dados==:

**Numérico**
Serve para representar qualquer número, seja de valor inteiro, seja de valor com casas decimais (também chamado de _ponto flutuante_). Uma variável deve ser declarada como numérica quando operações aritméticas precisarem ser realizadas com ela.

**Caractere**
Serve para representar letras, caracteres especiais, acentuações e até mesmo números, quando esses números não servirem para operações aritméticas, por exemplo.

**Literal/booleano**
Serve para representar somente dois estados lógicos: verdadeiro ou falso (1 ou 0).

##### Regras para nomes de variáveis

Em Python, e na maioria das linguagens de programação, algumas regrinhas devem ser consideradas ao escolhermos os nomes para nossas variáveis, pois alguns símbolos e combinações não são aceitos. 

Exemplos de nomes de variáveis válidos e inválidos:

| Nome de variável | Permitido?                  | Explicação                                                                                                                                               |
| ---------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idade            | Sim                         | Nome formado somente por letras/caracteres não especiais.                                                                                                |
| v3               | Sim                         | Números são permitidos desde que não seja no início da palavra.                                                                                          |
| 3v               | **Não**                     | Não podemos iniciar o nome de uma variável com um número.                                                                                                |
| Maior_nota       | Sim (porém não recomendado) | Podemos utilizar caracteres maiúsculos traço sublinhado sem problemas. Porém a **PEP 8 recomenda que o nome de variáveis siga o padrão ==snake_case==**. |
| Maior nota       | **Não**                     | O uso de espaços não é permitido em nomes de variáveis.                                                                                                  |
| \_maior_         | Sim                         | Podemos usar traço sublinhado em qualquer parte do nome da variável.                                                                                     |
| \#maior          | **Não**                     | Caracteres especiais não são permitidos em nenhuma parte do nome da variável.                                                                            |
| adicao           | Sim                         | Nome formado somente por letras/caracteres não especiais.                                                                                                |
| Adição           | Parcialmente                | Somente o Python 3 permite caracteres com acentuação. É recomendado fortemente evitar a criação de variáveis com nomes desse formato.                    |

##### Variáveis numéricas

Uma variável é numérica quando ==armazena um número inteiro ou de ponto flutuante==. Um número inteiro é aquele que pertence ao conjunto de números naturais e inteiros, na matemática. 

Já números de ponto flutuante armazenam casas decimais. O termo ponto flutuante (float) é oriundo da vírgula (na programação e na língua inglesa, usamos ponto), que é capaz de deslocar-se pelo número (flutuando) e alterando o expoente do dado numérico. Exemplos: 100.02, -10.7, etc.

##### Variáveis lógicas

Uma variável do tipo lógico, também conhecido como booleana, realiza operações lógicas empregando a álgebra proposta por George Boole. ==Uma variável lógica armazena somente dois estados: verdadeiro (true) e falso (false)==. 

Na memória do programa, ambos os estados podem ser representados por um único bit. E essa é a grande vantagem desse tipo de variável, pois seu uso de memória no programa é ínfimo. O bit de valor 1 irá representar verdadeiro, e o bit de valor 0 representará falso. Com uma variável booleana, podemos realizar operações lógicas.

Lista de operadores relacionais em Python:

| Python | Operação           |
| ------ | ------------------ |
| ==     | Igual a            |
| >      | Maior que          |
| <      | Menor que          |
| >=     | Maior ou igual que |
| <=     | Menor ou igual que |
| !=     | Diferente de       |

##### Variáveis de cadeia de caracteres (strings)

É muito comum necessitarmos armazenar conjuntos de símbolos, como frases inteiras, em uma única variável. Muitas vezes, ainda precisamos envolver acentuação, pontuação, números e tabulação, tudo isso em uma só variável. Podemos representar e guardar tudo isso em uma variável denominada de cadeia de caracteres ou string.

==Cada símbolo que conhecemos é codificado e representado, dentro do computador, por uma sequência de bits que segue um padrão internacional==. O primeiro padrão foi criado na década de 1960 e é denominado de tabela da ==American Standard Code for Information Interchange (ASCII4)==. 

Esse padrão define a codificação para 128 símbolos (7 bits), dentre eles números, letras maiúsculas e minúsculas, mais alguns caracteres empregados em todas as línguas de maneira universal, como ponto de interrogação, assim como alguns símbolos de tabulação, como o recuo de parágrafo ou o espaço simples. Existe também uma versão da ASCII, chamada de estendida, com 8 bits.

Porém, rapidamente o padrão ==ASCII tornou-se obsoleto==, uma vez que muitos caracteres ficaram de fora e não podiam ser representados, já que 7 (ou 8) bits não era suficiente. Assim, ==criou-se uma extensão dele, chamada de Unicode==. Esse padrão, hoje, é capaz de suportar mais de 4 bilhões de símbolos (32 bits). ==O Unicode é capaz de representar todos os caracteres orientais, acentuações de todas as línguas, e até mesmo emojis têm codificação conforme esse padrão.==

O Python armazena cada caractere em um espaço de memória próprio, que pode ser acessado individualmente. Porém, todo o espaço da variável é um bloco alocado sequencialmente na memória destinada ao programa. Se pudéssemos tirar uma foto interna da memória do nosso programa, veríamos uma sequência de dados codificados em um padrão, como ASCII ou Unicode.

Representação de uma string com a frase "Ola, mundo!" e seu equivalente em ASCII:

| O   | l   | a   | ,   |     | m   | u   | n   | d   | o   | !   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 79  | 108 | 97  | 44  | 32  | 109 | 117 | 110 | 100 | 111 | 33  |

##### Manipulando strings

Strings apresentam um potencial bastante vasto a ser explorado na linguagem, pois podemos realizar operações como ==concatenação, composição e fatiamento== de strings, tudo isso de maneira nativa, com o Python.

**Concatenação**
Concatenar strings significa juntá-las ou somá-las. Vejamos o exemplo a seguir:

```php
s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'
print(s1)
#saída: Lógica de Programação e Algoritmos
```

Podemos repetir uma mesma string várias vezes, na concatenação, utilizando o símbolo de multiplicação (\*). Por exemplo:
```php
s1 = 'A' + '-' * 10 + 'B'
print(s1)
#saída: A----------B
```

**Composição**
Podemos criar uma mensagem que misture texto e dados numéricos. Podemos, por exemplo, colocar o valor de uma variável dentro de uma outra variável que seja do tipo string. Para isso, existem três maneiras distintas de fazermos composição.

**1. Composição por marcador de posição**
Utilizamos um símbolo de percentual (%), que vamos chamar de marcador de posição. Esse símbolo será colocado dentro de nosso texto, no local exato onde o valor de uma variável deve aparecer. Assim, ele irá marcar a posição da variável que irá substituir o símbolo de percentual.

```php
#exemplo 1
nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)
#saída: Você tirou 8.500000 na disciplina de Algoritmos
```

```php
#exemplo 2
nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)
#saída: Você tirou 8.50 na disciplina de Algoritmos
```
<br>
Lista de marcadores de posição:

| Marcadores | Tipo                       |
| ---------- | -------------------------- |
| %d ou %i   | Números inteiros           |
| %f         | Números de ponto flutuante |
| %s         | Strings                    |

**2. Composição moderna**
Nela, ao invés de % dentro do texto, usamos chaves; ao invés do percentual fora do texto, usamos .format. Não trabalhamos com tipos, nesse formato. E, caso necessário, as casas decimais podem ser informadas dentro das chaves. Veja o exemplo a seguir.

```php
#exemplo
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}'.format(nota,disciplina)
print(s1)
#saída: Você tirou 8.5 na disciplina de Algoritmos
```

**3. Composição com f-string**
As f-strings permitem que você insira expressões diretamente em literais de strings precedidas do caractere f. Dentro da string, você pode colocar expressões, entre chaves {} que serão avaliadas e substituídas pelos valores correspondentes, durante a execução do programa.

```php
#exemplo
nota = 8.5
disciplina = 'Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1)
#saída: Você tirou 8.5 na disciplina de Algoritmos
```


**Slicing (fatiamento)**
É possível manipularmos uma parte específica da cadeira de caracteres informando um intervalo de índices a ser lido, fatiando a string. Esse intervalo é informado ao chamarmos o nome da string e indicarmos os índices de início e de fim, separados por dois-pontos (:).

```php
#exemplo
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
#saída: Lógica
```

**Tamanho (`len`)**
Podemos descobrir quantos caracteres temos em uma string utilizando a função `len()`. Saber o tamanho de uma string pode ser bastante útil em diversas aplicações, especialmente quando precisamos validar dados.

```php
#exemplo
s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)
#saída: 34
```

##### Função de entrada e fluxo de execução do programa

**Função de entrada**
O comando de entrada de dados em Python é o `input()`. Sua construção é muito semelhante à função de saída `print()`. Utilizamos parênteses para delimitar uma mensagem que aparecerá na tela ao usuário, bem como usamos aspas simples para escrever a mensagem.

```php
#exemplo 1
idade = input("Qual sua idade? ")
print(idade)
#saída: Qual sua idade? 55
```

```php
nome = input("Qual seu nome?")
print(f"Olá {nome}, seja bem-vindo!")
#saidas:
# Qual seu nome? Nycolas
# Olá Nycolas, seja bem-vindo!
```

**Convertendo dados de entrada (casting)**
A função `input` sempre retorna um dado do tipo string. Isso significa que, caso precisemos de um dado numérico para ser utilizado posteriormente em algum cálculo, precisamos converter o resultado de input em um valor inteiro ou ponto flutuante. Para tal, basta colocarmos a função `int()` ou a função `float()`, respectivamente, antes do input.

```php
nota = float(input('Qual nota você recebeu na disciplina? '))
print(f'Você tirou nota {nota}.')
#saídas: 
#Qual nota você recebeu na disciplina? 8.9
#Você tirou nota 8.9
```

Chamamos de ==casting de variáveis==, em programação, ==quando existe a conversão de uma variável de um tipo de dado em outro==. Em muitas linguagens de programação, é possível converter uma variável de um tipo em outro, desde que essa conversão seja lógica e faça sentido, no contexto do programa.
