##### Entendendo o Diagrama de Classes
O diagrama de classe, conforme a UML, representa a ==estrutura estática de um sistema por meio de classes e seus relacionamentos==. Uma classe descreve objetos que compartilham estrutura e comportamento, como ALUNO ou PROFESSOR, refletindo elementos do mundo real. Esses diagramas podem abranger todo o sistema ou partes dele, dependendo da complexidade.  

A modelagem de classes está ligada aos princípios da orientação a objetos:  
- **Abstração**: ==foca em aspectos relevantes para um contexto específico==. Por exemplo, ao verificar a situação de um ALUNO, apenas a matrícula é essencial, ignorando dados como endereço.  
- **Encapsulamento**: ==separa a interface externa (métodos acessíveis) dos detalhes internos==. Um exemplo é o método *calcular média aluno*, que retorna o resultado sem expor o processo de cálculo.  
- **Herança**: ==permite que classes compartilhem atributos e métodos hierarquicamente==. A classe MEIO DE TRANSPORTE, por exemplo, pode ser "mãe" de AUTOMÓVEL e CAMINHÃO, que herdam características gerais e adicionam atributos específicos como placa.  

Um exemplo prático é o sistema escolar com classes ALUNO, TURMA e PROFESSOR. Alunos se matriculam em uma única turma, enquanto turmas contêm múltiplos alunos. Professores ministram aulas em uma ou mais turmas, e uma turma pode ter vários professores. ==Esses relacionamentos definem a dinâmica do sistema, refletindo necessidades reais do cliente==.  

###### 1.1 Diferença entre classe e objeto  
==Classe é um modelo abstrato (como a planta de uma casa), enquanto objeto é uma instância concreta (a casa construída)==. Por exemplo, a classe AUTOMÓVEL define características gerais, e objetos como um HONDA CIVIC (placa ABC9D99) são instâncias específicas. Na programação, a classe existe no código, enquanto o objeto é criado em memória durante a execução, com valores definidos para atributos e métodos.  

###### 1.2 Elementos de um diagrama de classe  
Um diagrama de classe inclui:  
- **Classes**: representam entidades do sistema (ex: ALUNO).  
- **Atributos e métodos**: descrevem características e ações das classes. Métodos devem estar alinhados à responsabilidade da classe (ex: *matricular aluno* pertence à classe ALUNO, não a PROFESSOR).  
- **Relacionamentos**: definem como as classes interagem (ex: um ALUNO está vinculado a uma TURMA).  

##### Classes, atributos e métodos
O diagrama de classes estrutura-se a partir de elementos que definem entidades do mundo real no software: ==classes, atributos e métodos==. Esses componentes ==refletem a organização orientada a objetos==, alinhando-se aos requisitos do sistema e ao domínio do problema (contexto específico do software).  

###### 2.1 Classes  
As ==classes são abstrações de objetos com características e comportamentos comuns==, como ALUNO ou AUTOMÓVEL. Para garantir clareza:  
- **Nomenclatura**: seguem padrões do domínio do problema (ex: *Colaborador* se a empresa usa esse termo) e são escritas como substantivos singulares com inicial maiúscula.  
- **Organização**: agregam atributos (características) e métodos (ações), definindo como os dados se comportam no sistema. Por exemplo, a classe ALUNO inclui atributos como *matrícula* e métodos como *consultarSituacao()*.  

###### 2.2 Atributos  
==Atributos representam características ou estados dos objetos==. Na classe ALUNO, por exemplo, *nome* (texto) e *matrícula* (número) são atributos. Eles possuem:  
- **Tipo**: define o formato dos dados (ex: *string* para nome, *integer* para matrícula).  
- **Visibilidade**: controla o acesso aos atributos:  
  - **+ público**: acessível em qualquer classe.  
  - **# protegido**: visível apenas em classes do mesmo pacote (grupo de classes relacionadas).  
  - **- privado**: restrito à própria classe.  
Exemplo: o atributo *cor* na classe AUTOMÓVEL pode ser público (+), permitindo que outras classes consultem essa informação.  

###### 2.3 Métodos  
==Métodos são operações que uma classe executa==, como *matricularAluno()* na classe ALUNO. Suas características incluem:  
- **Retorno**: podem ou não devolver um valor (ex: *calcularMedia()* retorna um número, enquanto *salvarDados()* não retorna nada).  
- **Parâmetros**: aceitam ou não argumentos (ex: *consultarCPF(int matricula)* recebe um número de matrícula).  
- **Visibilidade**: segue o mesmo padrão dos atributos (+ público, # protegido, - privado).  
Exemplo: o método privado *- getNome() : String* na classe ALUNO retorna o nome do aluno, mas só pode ser acessado internamente.  

##### Relacionamentos
Os relacionamentos em diagramas de classe ==definem como as classes se comunicam e compartilham informações==, refletindo a colaboração entre elas no software. Esses relacionamentos possuem características essenciais:  
- **Nome**: descreve a natureza do vínculo (ex: "trabalha para").  
- **Sentido e navegabilidade**: indicados por setas, mostram a direção da relação (ex: Pessoa → Empresa).  
- **Multiplicidade**: define quantas instâncias podem se relacionar (ex: uma TURMA tem 0..* alunos, um ALUNO pertence a 0..1 turma).  
- **Papéis**: cada classe assume funções específicas no contexto da relação (ex: na associação entre Pessoa e Empresa, "empregado" e "empregador").<br>
  ![[Pasted image 20250503193849.png|400]]

###### 3.1 Tipos de relacionamentos  
Os três principais tipos são:  

**Associação**  
==Representado por uma linha sólida, vincula objetos de classes diferentes==. Por exemplo, um ESTUDANTE pode competir em uma EQUIPE_FUTEBOL (multiplicidade 1) e participar de 0 a 8 DISCIPLINAS. Já uma DISCIPLINA exige pelo menos um aluno (1..*). Nesse caso, a classe ESTUDANTE assume papéis distintos: "jogador" na relação com EQUIPE_FUTEBOL e "aluno" com DISCIPLINA.<br>
![[Pasted image 20250503193911.png|400]]<br>
![[Pasted image 20250503193946.png|400]]
<br>

**Generalização**  
==Relacionamento hierárquico (herança), onde subclasses herdam atributos e métodos de uma superclasse==. Exemplo: VEÍCULO (superclasse) tem subclasses TERRESTRE e AÉREO. As subclasses compartilham características gerais (ex: marca) e adicionam específicas (ex: tipo de pneu para TERRESTRE). Representado por uma linha com seta vazia.<br>
![[Pasted image 20250503194208.png|500]]
<br>

**Dependência**  
==Indica que mudanças em uma classe afetam outra, representado por linha tracejada==. Por exemplo, a classe DEPENDENTE só existe enquanto houver um FUNCIONÁRIO associado. Se um objeto FUNCIONÁRIO for removido, seus DEPENDENTES também são invalidados. É uma relação frágil, comum em casos temporários ou contextuais.<br>
![[Pasted image 20250503194242.png|500]]
<br>
##### Técnicas de modelagem de diagrama de classes
A modelagem de diagramas de classe envolve etapas estruturadas para traduzir requisitos abstratos em uma representação visual clara.
<br>
![[Pasted image 20250503194553.png|600]]
<br>
![[Pasted image 20250503194811.png]]

##### Analisando um exemplo de diagrama de caso de uso
O estudo de caso analisa um sistema de vendas de livros online com programa de fidelidade. O objetivo é modelar as classes e relacionamentos para os casos de uso **"Utilizar Programa de Fidelidade"** (aplicar desconto de 10% em compras acima de R$500 anuais) e **"Atualizar Programa de Fidelidade"** (verificar elegibilidade do cliente).  

**Classes principais e atributos**  
- **CLIENTE**:  
  - Atributos: *Nome* (string), *CPF* (int), *Telefone* (int), *Endereço* (string).  
  - Responsabilidade: armazenar dados do cliente e vincular ao histórico de compras.  
- **FIDELIDADE**:  
  - Atributos: *StatusFidelidade* (boolean: "Sim"/"Não"), *CPF* (int).  
  - Responsabilidade: controlar elegibilidade para desconto com base no valor gasto no último ano.  
- **PEDIDO**:  
  - Atributos: *Número* (int), *CPF* (int), *DataPedido* (date), *ValorTotal* (float).  
  - Responsabilidade: registrar compras e calcular o valor total do pedido.  
- **PRODUTO_DO_PEDIDO**:  
  - Atributos: *NúmeroPedido* (int), *ProdutoID* (int), *Quantidade* (int), *ValorUnitário* (float).  
  - Responsabilidade: detalhar itens de cada pedido, evitando redundância de dados.  

**Relacionamentos e funcionalidades**  
- **CLIENTE ↔ FIDELIDADE** (1:1):  
  Cada cliente tem um registro único de fidelidade. O *CPF* em **FIDELIDADE** vincula-se ao cliente correspondente.  
- **CLIENTE ↔ PEDIDO** (1:N):  
  Um cliente pode ter múltiplos pedidos, mas cada pedido pertence a um único cliente.  
- **PEDIDO ↔ PRODUTO_DO_PEDIDO** (1:N):  
  Um pedido contém vários produtos, cada um com quantidade e preço específicos. O *ValorTotal* em **PEDIDO** é calculado somando os valores dos produtos.  

**Métodos e regras de negócio**  
- **PEDIDO.calcularValorTotal()**:  
  Soma os valores (*Quantidade × ValorUnitário*) de todos os produtos vinculados ao pedido.  
- **FIDELIDADE.atualizarStatus()**:  
  Verifica se o cliente atingiu R$500 em compras no último ano (acessando histórico de **PEDIDO**) e atualiza *StatusFidelidade*.  
- **UC01 (Utilizar Programa de Fidelidade)**:  
  Durante o checkout, o sistema consulta *StatusFidelidade* e aplica o desconto de 10% se elegível.  

**Exemplo de interação**  
Quando um cliente finaliza um pedido:  
1. **PRODUTO_DO_PEDIDO** registra os itens comprados.  
2. **PEDIDO** calcula o *ValorTotal* e vincula ao **CLIENTE**.  
3. **FIDELIDADE** é atualizado automaticamente (UC02), verificando se o gasto anual ultrapassou R$500.  
4. Na próxima compra, o sistema aplica o desconto (UC01) se *StatusFidelidade = "Sim"*.  

Este modelo prioriza a coesão entre classes, garantindo que cada uma gerencie apenas suas responsabilidades (ex: **FIDELIDADE** não armazena dados de pedidos). A prática de exercitar diferentes cenários (ex: clientes com múltiplos pedidos) ajuda a validar a robustez do diagrama.