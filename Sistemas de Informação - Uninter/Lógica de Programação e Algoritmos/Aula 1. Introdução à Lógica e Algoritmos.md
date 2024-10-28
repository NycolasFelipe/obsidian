O objetivo desta abordagem é introduzir os principais conceitos inerentes à lógica de programação e algoritmos. Vamos iniciá-la compreendendo o que significam as palavras-chave do nosso estudo: lógica e algoritmos. 

Investigaremos um pouco do raciocínio lógico necessário para o desenvolvimento de programas computacionais, bem como iremos definir, em um contexto até mesmo fora da computação, o que são algoritmos.

##### Introdução à lógica e aos algoritmos

**O que é lógica?**
- Aristóteles - conceito de lógica (logos) - linguagem racional.
- Parte da filosofia que se ocupa das formas do pensamento e das operações intelectuais. (Michaelis, 2020).

Na computação, lógica pode ser entendida como ==a maneira pela qual instruções, assertivas e pressupostos são organizadas num algoritmo== para viabilizar a implantação de um programa (Michaelis, 2020).

**O que são algoritmos?**
Um algoritmo é dado como uma ==sequência de passos a serem realizados para que determinada tarefa seja concluída==, ou que um objetivo seja atingido.

##### Sistemas de computação

**Segunda Guerra Mundial:**
- Cálculo de mísseis.
- Mensagens codificadas.
- Computadores construídos com milhares de válvulas e relés, pesando toneladas e consumindo montantes gigantes de energia elétrica.
- ENIAC (Electronic Numerical Integrator and Computer).
- Percebeu-se a necessidade de mudar a maneira como computadores eram projetados, começando pela aritmética decimal para binária.
- ==John von Neumann== - matemático húngaro, propôs o primeiro computador de programa capaz de ser armazenado em memória.

**A máquina de von Neumann**

![[Pasted image 20241028144242.png]]

**O Bit**
- Base decimal - dígitos de 0 a 9.
- Base binária - dígitos 0 e 1.
- Todo e qualquer computador é binário.
- ==Binary digit== - a menor unidade de armazenamento de dados.

**Representações do bit**

![[Pasted image 20241028144656.png|400]]

**A palavra (word)**
- ==Binary digit== - menor unidade de armazenamento de dados.
- ==Palavra (word)== - menor unidade útil de manipulação de dados.

**O sistema operacional**
- Define quais softwares e quando serão executados.
- Gerencia o uso de memória.
- Abstrai o hardware para o usuário e para o desenvolvedor.

##### Representação de algoritmos

**Descrição narrativa**
- Usa linguagem natural.
- Não utilizada em algoritmos computacionais.

Exemplo:
```
1. Ler dois valores (x e y);
2. Verificar se x e y são iguais;
3. Se x for igual a y, mostrar a mensagem "Valores iguais!";
4. Se x for diferente de y, mostrar a mensagem "Valores diferentes!";
5. Fim.
```

**Pseudocódigo**
- Português estruturado.
- Representação mais próxima de um programa computacional, mas sem se preocupar com a linguagem de programação adotada.
- Regras definidas.
- Linguagem genérica.

Exemplo:
```
Algoritmo
Var
	x, y: inteiro
Início
	Ler(x, y)
	Se(x = y) então
		Mostrar("Valores iguais!")
	Senão
		Mostrar("Valores diferentes!")
	Fimse
Fim
```

**Fluxograma**
- Representação gráfica de um algoritmo.
- Usado para passar a ideia do seu código e organizar o raciocínio lógico.
- Simbologia gráfica padrão **ISO 5807:1985**.

Exemplo:

![[Pasted image 20241028145829.png]]

##### Linguagens de programação e compiladores

**Linguagens de programação**
Uma linguagem de programação é um conjunto de regras, com palavras-chaves, verbos, símbolos e sequências específicas. Chamamos todo esse conjunto de ==sintaxe da linguagem==.

Essa sintaxe da linguagem resulta em instruções compreendidas pelo computador e não geram ambiguidades.

**Software de compilação**
O software compilador (ou interpretador) é responsável por ==transformar o código que escrevemos== em linguagem de alto nível, ==em uma linguagem de máquina de baixo nível que é possível ser compreendida pelo hardware==.

Ilustração do processo de compilação:

![[Pasted image 20241028150530.png]]

**Compiladores e Interpretadores**
Compiladores são softwares que transformam um código-fonte em um arquivo binário.

Interpretadores não convertem o código somente uma única vez, mas continuam executando instrução por instrução à medida que o programa faz requisições.

Vantagens e desvantagens de cada tipo de tradutor:

![[Pasted image 20241028151015.png]]

##### Linguagem de programação Python

**O que torna o Python tão popular e utilizado?**
- Linguagem de propósito geral.
- Vasta quantidade de biblioteca existentes.
- Linguagem simples e intuitiva. Ótima para iniciantes.
- Linguagem multiplataforma.
- Comunidade ativa e atualizações constantes.

**Histórico da linguagem**
- Linguagem criada em 1982 por Guido van Rossum.
- Centrum Wiskunde & Informatica (CWI), Amsterdam.
- Inspiração: linguagem ABC.

**Exemplos de aplicações Python**
- Sistemas operacionais (Linux, macOS).
- RaspBerry Pi.
- Análise de dados e inteligência artificial.

**O Zen do Python, por Tim Peters**
- Bonito é melhor que feio.
- Explícito é melhor que implícito.
- Simples é melhor que complexo.
- Complexo é melhor que complicado.
- Plano é melhor que aglomerado.
- Legibilidade faz diferença.
- ==Agora é melhor que nunca.==