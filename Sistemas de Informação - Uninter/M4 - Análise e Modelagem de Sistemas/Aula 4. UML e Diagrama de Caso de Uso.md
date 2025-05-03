##### O que é UML
A **UML (Unified Modeling Language)** é uma ==linguagem padrão para modelagem de sistemas orientados a objetos==, mantida pelo **Object Management Group (OMG)**. Surgiu em 1994, desenvolvida por James Rumbaugh e Grady Booch na Rational Software, associada ao **Rational Unified Process (RUP)**, metodologia tradicional que organiza o ciclo de vida de desenvolvimento. A UML não é um método, mas uma ==notação visual para especificar, documentar e comunicar projetos de software==, facilitando a compreensão de estruturas e comportamentos do sistema.  

###### Modelos de UML  
==Modelos são abstrações da realidade==, simplificando sistemas complexos para análise e projeto. Eles permitem:  
- Visualizar interfaces e funcionamento do software.  
- Especificar estrutura (componentes e relações) e comportamento (interações e dinâmicas).  
- Documentar decisões técnicas e apoiar a comunicação entre equipes.  

A UML divide-se em dois tipos de diagramas:  
1. **Estruturais (estáticos)**:  
   - *Diagrama de classes*: Mostra classes, atributos, métodos e relações (herança, associação).  
   - *Diagrama de componentes*: Representa partes do software (códigos, bibliotecas).  
   - *Diagrama de implantação*: Modela hardware e ambientes (teste, produção).  
   - Outros: objetos, pacotes, estrutura de composição.  

2. **Comportamentais (dinâmicos)**:  
   - *Diagrama de casos de uso*: Detalha requisitos funcionais e interações com usuários (atores).  
   - *Diagrama de sequência*: Mostra interações temporais entre objetos.  
   - *Diagrama de atividades*: Fluxos de processos ou lógica de negócio.  
   - Outros: estados, comunicação, tempo.  

###### Relevância em Metodologias Ágeis  
Apesar de associada a abordagens tradicionais (como RUP), a UML é valorizada em contextos ágeis pois **agrega clareza**. ==Diagramas como *casos de uso* ou *classes* evitam ambiguidades==, enquanto o pensamento ágil prioriza evitar desperdício: modelos são usados apenas se únicos para resolver problemas específicos.  

A **versão 2.0** da UML, atual padrão OMG, inclui 13 tipos de diagramas, cada um focando uma perspectiva do sistema. Seu uso eficaz depende do equilíbrio entre detalhamento e pragmatismo, adaptando-se às necessidades do projeto sem sobrecarregar a equipe.

##### Modelo Orientado a Objetos
==A orientação a objetos é um paradigma que modela o mundo real como uma coleção de objetos==, entidades com identidade, características (atributos) e comportamentos (métodos). Esses objetos podem ser físicos (ex.: livro), conceituais (ex.: diagrama) ou de software (ex.: botão em uma interface), simplificando a representação de sistemas complexos.  

###### Princípios Fundamentais  
1. **Abstração**: ==Foco nos aspectos essenciais de um objeto==, ignorando detalhes irrelevantes. Por exemplo, um gato pode ser visto como "animal doméstico" por um dono (foco em comportamento) ou como "mamífero com determinada raça" por um veterinário (foco em características biológicas).  
2. **Encapsulamento**: ==Separa a interface externa do objeto== (como ele interage) de sua implementação interna (como funciona). Analogia: dirigir um carro requer saber usar acelerador e embreagem, sem entender o motor.  
3. **Herança**: ==Permite que objetos compartilhem atributos e métodos== com base em hierarquias. Exemplo: classes "Veículo" e "Carro", onde "Carro" herda propriedades gerais de "Veículo" e adiciona características específicas.  

###### Características dos Objetos  
- **Identidade**: Única para cada objeto (ex.: ISBN de um livro).  
- **Atributos**: Propriedades mutáveis (ex.: cor, preço).  
- **Comportamentos**: Ações que o objeto executa (ex.: "calcular frete").  

##### Técnicas de Construção do Diagrama de Casos de Uso
O diagrama de caso de uso é uma ==ferramenta essencial para modelar requisitos funcionais==, representando visualmente as interações entre atores (usuários ou sistemas externos) e casos de uso (funcionalidades do software). Sua construção ==inicia após o levantamento de requisitos, identificando atores e funcionalidades==, e visa comunicar o escopo do sistema de forma clara e acessível.  

###### Elementos Principais  
- **Atores**: Representados por bonecos, indicam quem ou o que interage com o sistema (ex.: cliente, administrador).  
- **Casos de uso**: Elipses que descrevem funcionalidades (ex.: "Comprar produto", "Reabastecer estoque").  
- **Relacionamentos**:  
  - **Associação**: Linha contínua ligando ator a caso de uso.  
  - **Inclusão** `<<include>>`: Indica que um caso de uso depende de outro (ex.: "Finalizar compra" inclui "Validar pagamento").  
  - **Extensão** `(<<extend>>)`: Mostra cenários opcionais ou exceções (ex.: "Cancelar compra" estende "Finalizar compra").  

###### Características e Benefícios  
- **Foco no comportamento externo**: ==Mostra **o que** o sistema faz, não **como**== (ex.: máquina self-service permite "Comprar produto" sem detalhar processamento interno).  
- **Validação de requisitos**: ==Facilita a confirmação com usuários==, evidenciando se todas as funcionalidades foram capturadas.  
- **Delimitação do sistema**: Casos de uso ficam dentro de um retângulo, simbolizando os limites do software; atores, externos.  

###### Exemplo Prático  
No sistema de uma **máquina self-service**, o diagrama ilustra:  
- **Atores**: Cliente, Reabastecedor, Coletor.  
- **Casos de uso**: "Comprar produto", "Reabastecer", "Coletar dinheiro".  
- **Relacionamentos**:  
  - Cliente associa-se a "Comprar produto".  
  - "Reabastecer" inclui "Abrir" e "Fechar" compartimentos.  
  - "Comprar produto" pode estender-se para "Cancelar compra" (não explicitado, mas implícito como extensão). <br>
    
    ![[Pasted image 20250502211545.png]]

###### Boas Práticas  
- **Detalhamento progressivo**: Começar com visão macro e desdobrar em subcasos conforme necessidade.  
- **Clareza na nomenclatura**: Nomes de casos de uso devem ser verbos + objeto (ex.: "Emitir relatório").  
- **Evitar redundância**: Relacionamentos *include* e *extend* ajudam a reutilizar lógica e evitar repetição.  

##### Componentes de um Diagrama de Caso de Uso
Um diagrama de caso de uso é ==composto por atores, casos de uso e relacionamentos==, que definem interações e dependências entre elementos.  

###### Ator  
==Representa um papel externo ao sistema== (usuário, sistema ou dispositivo) que interage com as funcionalidades.    <br>
  ![[Pasted image 20250502212155.png|500]]
- **Tipos**:  
  - *Primário*: Inicia a interação principal (ex.: cliente em uma compra online).  
  - *Secundário*: Fornece suporte (ex.: sistema de pagamento externo).  
- **Categorias**: Usuários finais, aplicações, dispositivos (sensores), eventos externos (temporizadores).  
- **Generalização**: Relacionamento hierárquico entre atores. Exemplo: *Secretária Executiva* é um tipo de *Secretária*, herdando seus casos de uso.<br>
  ![[Pasted image 20250502212307.png|500]]

###### Caso de Uso  
==Funcionalidade do sistema==, representada por uma **elipse** com nome descritivo (ex.: *Efetuar Saque*). Deve refletir objetivos claros, como "Autenticar Cliente" ou "Contratar Seguro".  

###### Relacionamentos  
1. **Associação**: Liga ator a caso de uso.  
   - *Direção*: Seta indica quem inicia a interação. Exemplo: Cliente → *Efetuar Saque* (ator inicia).<br>
     ![[Pasted image 20250502212354.png|350]]
1. **Include** `<<include>>`: Indica dependência obrigatória entre casos de uso. Exemplo: *Efetuar Saque* inclui *Autenticar Cliente*.  
2. **Extend** `<<extend>>`: Representa cenários opcionais. Exemplo: *Contratar Seguro* estende *Efetuar Saque*, dependendo da escolha do usuário.<br>
   ![[Pasted image 20250502212451.png|500]]

###### Exemplo Prático  
Em um **caixa eletrônico**:  
- Ator *Cliente* associa-se a *Efetuar Saque*.  
- *Efetuar Saque* inclui *Autenticar Cliente* (obrigatório).  
- *Contratar Seguro* estende *Efetuar Saque* (opcional).  

##### Analisando um Exemplo de Diagrama de Caso de Uso
O estudo de caso analisado envolve uma **livraria virtual** com funcionalidades como vendas online, programa de fidelidade e integração com sistemas externos.
<br>
![[Pasted image 20250502213029.png]]