Diagrama de Entidade e Relacionamento (DER) é uma representação gráfica do Modelo de Entidade e Relacionamento (MER). Enfim, isso evita excesso de abstração, trazendo para a realidade informações pertinentes de uma forma mais visual e, consequentemente, mais intuitiva.

Mas para um conhecimento pleno de como elaborar um Diagrama de Entidade e Relacionamento **é necessário conhecer as partes que compõem esse fluxo**.

##### O que é o MER ?
O **MER** (Modelo Entidade Relacionamento) é utilizado para descrever os objetos do mundo real através de entidades, com suas propriedades que são os atributos e os seus relacionamentos.

##### O que são entidades?
As entidades representam um **objeto** do mundo real e que possuem uma existência independente, como: pessoas, empresa, carro, casa, entre outras coisas que podem ser representadas por uma entidade. 

Podemos considerar que existem três tipos de entidades:
1. **As entidades fortes**, que não dependem de outras entidades para existirem.
2. **As entidades fracas**, dependem de outras entidades para existir, ou seja, elas não possuem existência própria ou não possuem atributos próprios para identificação, dependendo assim, dos atributos chave das entidades fortes. 
3. **As entidades associativas**, que são utilizadas quando existe a necessidade de associar uma entidade a um relacionamento.
##### O que são atributos?
Os atributos descrevem as propriedades das entidades. A entidade `pessoa` pode ter como atributo o `nome`, `data de nascimento`, `idade`, `endereço`. Como as entidades, também existem alguns tipos de atributos, que são: os atributos **simples**, atributos **compostos**, atributos **multivalorados**, atributos derivados e atributos **chave**. Agora veremos cada um deles:

**Atributo Simples**
Atributos simples são indivisíveis, ou seja, são atributos atômicos, um exemplo seria o atributo `CPF`, ele não pode ser dividido em partes menores para formar outros atributos, ele é indivisível.

**Atributo Composto**
Atributos Compostos podem ser divididos em partes menores, que representam outros atributos, como o atributo endereço, ele pode ser subdividido em atributos menores, como, por exemplo, `cidade`, `estado`, `rua`, `CEP`.

**Atributo Multivalorado**
Um atributo Multivalorado pode ter um ou **N** (vários) valores associados a ele, como, por exemplo, o atributo telefone de um cliente, ele pode ter um ou vários telefones.

**Atributo Derivado**
Atributos derivados dependem de outro atributo ou até mesmo outra entidade para existir, como, por exemplo, o atributo idade e o atributo data de nascimento, para descobrimos a idade de uma pessoa precisamos da sua data de nascimento, então, consideramos o atributo idade como derivado do atributo data de nascimento.

**Atributo Chave**
O atributo chave é utilizado para identificar de forma única uma entidade, ou seja, os valores associados a esse atributo são distintos dentre o conjunto de entidades. Como exemplo, podemos utilizar o `CPF` de uma pessoa, ele é único e pode ser utilizado como atributo chave, já que cada pessoa recebe um número de `CPF` distinto.

##### O que são relacionamentos?
**O relacionamento é a associação entre as entidades.** Confira um exemplo: 

O comprador precisa do vendedor para comprar o carro. Com base nisso, percebe-se a necessidade de um relacionamento. 

**Existem 3 principais tipos de relacionamento**: um-para-um, um-para-muitos (ou muitos-para-um, dependendo do sentido da relação) e muitos-para-muitos. 

1. **Um para um**: um carro terá um único comprador.
2. **Um para muitos**: um vendedor pode atender diversos clientes, porém um cliente concluirá a compra com apenas um único vendedor. 
3. **Muitos para muitos**: um grupo de vendedores comercializa muitos carros para muitos compradores.

A melhor maneira de identificar o tipo de relacionamento é por meio de perguntas.

Uma entidade interfere na outra? Como elas estão relacionadas? 

Definir isso antes de “colocar a mão na massa” é de extrema importância para um melhor desempenho da sua aplicação.

##### O DER (Diagrama Entidade-Relacionamento)
O **DER** (Diagrama Entidade-Relacionamento) é utilizado para representar em forma gráfica o que foi descrito no **MER** (Modelo Entidade Relacionamento).

##### Símbolos de relacionamento
![[Pasted image 20241215130753.png|400]]

##### Praticando um pouco
Exemplo de criação de um MER para o contexto de uma escola.

O primeiro passo na criação do banco de dados relacional é a **abstração**:
- A escola tem professores que ensinam uma disciplina cada e cada disciplina só pode ser ensinada por um professor. 
- Cada professor pode ter muitos alunos e cada aluno pode ter muitos professores. 
- Cada aluno só pode receber uma nota de uma disciplina da classe.
- As notas podem pertencer a mais de um aluno. 
  
Se eu extrair todos os substantivos deste parágrafo, terei: ==professores, disciplinas, alunos e notas==. Esses substantivos podem ser representados por linhas de dados chamadas entidades. Essas entidades também compartilham relacionamentos entre si.

Diagramas de relacionamento de entidade (ER) podem ser desenhados para mostrar entidades e seus relacionamentos entre si. Essas entidades podem ser representadas como quadrados, conforme mostrado abaixo.

![[Pasted image 20241215134852.png]]

Também preciso ==desenhar ligações de uma entidade para outra== para representar o relacionamento entre as duas entidades.

Como um professor só pode ensinar uma disciplina e uma disciplina só pode ser ensinada por um professor, disciplinas e professores compartilham um relacionamento um para um.

![[Pasted image 20241215134958.png|400]]

Como cada professor pode ter muitos alunos e cada aluno pode ter muitos professores, professores e alunos compartilham um relacionamento muitos para muitos.

![[Pasted image 20241215135109.png|400]]

Como cada aluno só pode receber uma nota por disciplina, enquanto as notas podem ser dadas a muitos alunos, alunos e notas compartilham um relacionamento de um para muitos.

![[Pasted image 20241215135133.png|400]]

Meu diagrama ER final é mostrado abaixo.
![[Pasted image 20241215135151.png]]

==Também é útil descrever o relacionamento entre as duas entidades==. A descrição de como as entidades interagem umas com as outras será ilustrada por um formato de diamante. A descrição de cada relacionamento de entidade para o diagrama é a seguinte. Professores ensinam disciplinas e têm alunos; alunos têm professores e recebem notas. O diagrama atualizado para refletir essas modificações é mostrado abaixo.

![[Pasted image 20241215135308.png]]

Outro tópico que quero abordar é a modalidade. A modalidade indica se o relacionamento é obrigatório ou opcional. Se uma entidade precisa ter um relacionamento com outra entidade, então haverá uma linha vertical através do link ao lado da entidade. Se uma entidade não precisa ter um relacionamento com outra entidade, então um 0 será colocado através da linha ao lado da entidade. Um diagrama ilustrando a modalidade é mostrado abaixo.

![[Pasted image 20241215135321.png||400]]

A entidade subjects não precisa ter um relacionamento com a entidade teachers ou pode ter no máximo um relacionamento com a entidade teachers. A entidade teachers precisa ter um e somente um relacionamento com a entidade subjects.

>**Disciplinas (subjects):** Uma disciplina pode não ter um professor associado (==por exemplo, uma nova disciplina ainda não foi atribuída a nenhum professor==) ou pode ter apenas um professor (um professor específico ensina aquela disciplina). Isso significa que uma disciplina pode estar "solta" ou vinculada a um único professor.
>
>**Professores (teachers):** Cada professor precisa estar associado a pelo menos uma disciplina. ==Ou seja, não existe um professor sem uma disciplina atribuída==. Além disso, um professor só pode estar associado a uma única disciplina.

![[Pasted image 20241215135638.png|400]]

A entidade do professor precisa ter pelo menos um ou muitos relacionamentos com a entidade do aluno, e a entidade do aluno precisa ter pelo menos um ou muitos relacionamentos com a entidade do professor.

![[Pasted image 20241215135716.png|400]]

A entidade students precisa ter um e somente um relacionamento com a entidade grades. A entidade grades não precisa ter um relacionamento com a entidade students ou pode ter muitos relacionamentos com a entidade students.

![[Pasted image 20241215135734.png|400]]

Atualizei o diagrama ER para mostrar não apenas os relacionamentos de uma entidade com outra, mas também a modalidade.

![[Pasted image 20241215135744.png]]

Cada entidade tem atributos que são características do substantivo que está sendo representado. Cada sujeito tem um nome. Cada aluno e professor pode ter um primeiro nome, sobrenome, número de telefone e endereço de e-mail. Cada nota pode ser de uma determinada letra. O diagrama ER foi atualizado com formas ovais para ilustrar os atributos das entidades. O diagrama ER abaixo agora exibe esses atributos.

![[Pasted image 20241215135806.png]]

**Mapeando o esquema para tabela**
O diagrama físico oferece uma visão clara e precisa de como os dados serão organizados e armazenados no banco de dados.

![[Pasted image 20241215141216.png]]

O diagrama físico **define quais tipos de dados podem ser inseridos em cada coluna** (e.g.: TEXT, INTEGER, etc) do banco de dados, além de outras regras. Além disso, as **restrições de coluna** (e.g.: NOT NULL (N), UNIQUE (U), etc.) e tabela trabalham em conjunto para garantir que os dados inseridos no banco de dados sejam **precisos, consistentes e livres de duplicidades**.

Agora, podemos subsituir nas colunas IDs o tipo UNIQUE para PRIMARY KEY. Dessa forma, **garantimos que o id além de único, também não poderá ser nulo** (NOT NULL e UNIQUE).

![[Pasted image 20241215141728.png]]

Agora precisamos implementar os relacionamentos que foram ilustrados nos diagramas de relacionamento de entidade. Uma chave estrangeira faz referência a uma linha em outra tabela. Podemos adicionar uma restrição de chave estrangeira (FK) a uma coluna e especificar qual coluna em outra tabela desejamos que ela faça referência. 

É uma prática recomendada fazer com que a **chave estrangeira faça referência à chave primária de outra tabela** porque a chave primária identifica exclusivamente uma linha de uma tabela. A restrição de chave estrangeira (FK) nos proíbe de adicionar quaisquer valores na coluna de chave estrangeira se não houver um valor de chave primária correspondente localizado na tabela à qual a chave estrangeira faz referência.

![[Pasted image 20241215141959.png]]

O diagrama acima demonstra um relacionamento um-para-um. A tabela subjects tem uma coluna que atua como uma chave primária e uma chave estrangeira que faz referência à coluna de chave primária da tabela teachers.

![[Pasted image 20241215143223.png]]

O diagrama acima demonstra um relacionamento muitos-para-muitos entre as tabelas teachers e students. ==Quando há um relacionamento muitos-para-muitos, é preciso haver uma tabela extra intermediária.== 

>**Entendendo Relacionamentos Muitos-para-Muitos**
>- **Um para muitos:** Um registro em uma tabela pode estar relacionado a muitos registros em outra tabela (por exemplo, um autor pode escrever muitos livros).
>- **Muitos para muitos:** Um registro em uma tabela pode estar relacionado a muitos registros em outra tabela, e vice-versa (por exemplo, um aluno pode ter muitos professores e um professor pode ter muitos alunos).
>
>**O Problema com Relacionamentos Diretos**
>- **Integridade referencial:** Em um banco de dados relacional, ==cada registro deve ter uma referência única para outro registro==. Um relacionamento direto muitos-para-muitos violaria essa regra, pois um único registro poderia ter múltiplas referências em ambas as direções.
>- **Redundância de dados:** Se tentássemos representar um relacionamento muitos-para-muitos diretamente nas tabelas existentes, acabaríamos com redundância de dados e inconsistências.
>
>  **A Solução: Tabela Intermediária**
>  - **Criando uma tabela extra:** ==Para resolver esse problema, cria-se uma tabela intermediária== (no nosso exemplo, students_teachers) que conecta as duas tabelas originais (students e teachers).
>  - **Chaves estrangeiras:** Nessa tabela intermediária, são incluídas chaves estrangeiras que fazem referência às chaves primárias das tabelas originais.
>  - **Chave primária:** A tabela intermediária também possui sua própria chave primária, que identifica de forma única cada associação entre um aluno e um professor.
>
> **Benefícios da Tabela Intermediária**
> - **Normalização:** A tabela intermediária ajuda a normalizar o banco de dados, reduzindo a redundância e melhorando a integridade dos dados.
> - **Flexibilidade:** Permite representar relacionamentos mais complexos entre entidades.
> - **Facilidade de consulta:** Facilita a realização de consultas que envolvem múltiplas tabelas relacionadas.


![[Pasted image 20241215143317.png]]

O diagrama acima demonstra um relacionamento um-para-muitos. A tabela students tem uma coluna de chave estrangeira que faz referência à coluna de chave primária id das tabelas grades.

![[Pasted image 20241215143337.png]]

O diagrama acima apresenta o diagrama físico final. ==O processo de criar tabelas distintas para cada conjunto de dados e relacioná-las usando chaves primárias e estrangeiras é conhecido como **normalização**==. A normalização minimiza a redundância de informações e garante a consistência dos dados. Com o diagrama físico concluído e o esquema do banco de dados relacional definido, é possível iniciar a implementação do próprio banco de dados.

##### Exemplo Prático de Tabela Intermediária em SQL

**Imagine um sistema de biblioteca.**
- **Tabela `livros`:** Contém informações sobre os livros (ID, título, autor).
- **Tabela `autores`:** Contém informações sobre os autores (ID, nome).
- **Tabela intermediária `livros_autores`:** Conecta livros e autores (ID, livro_id, autor_id).

**Por que uma tabela intermediária?** Um autor pode escrever vários livros, e um livro pode ter vários autores (por exemplo, no caso de coautorias).

**Exemplo de dados:**

**Tabela Livros**

| ID  | titulo             |
| --- | ------------------ |
| 1   | O Senhor dos Anéis |
| 2   | Harry Potter       |

**Tabela Autores**

| ID  | nome           |
| --- | -------------- |
| 1   | J.R.R. Tolkien |
| 2   | J.K. Rowling   |
| 3   | Outro Autor    |

**Tabela Livros_Autores (tabela de junção)**

|ID|livro_id|autor_id|
|---|---|---|
|1|1|1|
|2|2|2|
|3|1|3|

**Comando SQL para encontrar todos os livros escritos por J.R.R. Tolkien:**
SQL
```SQL
SELECT l.titulo
FROM livros l
INNER JOIN livros_autores la ON l.id = la.livro_id
INNER JOIN autores a ON la.autor_id = a.id
WHERE a.nome = 'J.R.R. Tolkien';
```

**Explicação:**

1. **`SELECT l.titulo`:** Seleciona o título do livro.
2. **`FROM livros l`:** Começa pela tabela de livros.
3. **`INNER JOIN livros_autores la ON l.id = la.livro_id`:** Une a tabela de livros com a tabela intermediária, relacionando os livros com suas associações.
4. **`INNER JOIN autores a ON la.autor_id = a.id`:** Une a tabela intermediária com a tabela de autores, relacionando as associações com os autores.
5. **`WHERE a.nome = 'J.R.R. Tolkien';`:** Filtra os resultados para mostrar apenas os livros do autor especificado.

**Resultado:**

| ID  | titulo             |
| --- | ------------------ |
| 1   | O Senhor dos Anéis |

##### Fontes
[Diagrama Entidade Relacionamento - modelo de banco de dados](https://www.youtube.com/@lucid_software_portugues)
[MER e DER: Definições, Banco de Dados e Exemplos](https://www.alura.com.br/artigos/mer-e-der-funcoes)
[Database Design: From Entity Relationship Diagrams to Physical Diagrams](https://medium.com/@ashleylynnrapone/database-design-from-entity-relationship-diagrams-to-physical-diagrams-16da210d01e9)
