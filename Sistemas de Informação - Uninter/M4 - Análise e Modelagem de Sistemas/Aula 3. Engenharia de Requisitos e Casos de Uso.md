##### Engenharia de Requisitos
A engenharia de requisitos é fundamental para o desenvolvimento de software, pois ==define as necessidades das partes interessadas e orienta todo o projeto==. Requisitos, expressos em linguagem natural para facilitar o entendimento entre técnicos e usuários, devem ser coletados com quem conhece o negócio e validados para evitar ambiguidades. Pressman (2016) destaca a complexidade dessa etapa, enquanto Mall (2014) reforça a importância do estudo de viabilidade inicial, que analisa aspectos técnicos, financeiros e de prazo.  

O processo de ==coleta de requisitos é estruturado em quatro etapas principais==: **estudo de viabilidade, coleta, especificação e validação**. Pressman propõe uma ==evolução desse ciclo para sete passos, visando maior controle e adaptação== às necessidades do projeto:  
1. **Concepção**: compreensão macro do problema e alinhamento entre equipes técnicas e de negócio.  
2. **Levantamento**: entrevistas com usuários e análise detalhada das necessidades.  
3. **Elaboração**: refinamento dos requisitos em modelos técnicos e cenários de uso.  
4. **Negociação**: priorização de requisitos, conciliando custo, prazo e escopo.  
5. **Especificação**: definição de tecnologias e arquitetura para implementação.  
6. **Validação**: revisão formal para garantir clareza, coerência e viabilidade técnica.  
7. **Gestão de requisitos**: controle contínuo de mudanças e rastreabilidade entre requisitos.  

###### O analista de requisitos  
Este profissional atua como ==ponte entre usuários e equipe técnica==, exigindo habilidades como compreensão de conceitos abstratos, sensibilidade ao contexto de negócio e comunicação clara. ==Deve identificar não apenas funcionalidades, mas comportamentos e detalhes críticos== (ex.: formatação específica de relatórios de vendas). Sua capacidade de sintetizar informações e mediar conflitos é essencial para traduzir necessidades em requisitos técnicos.  

###### O documento de especificação de requisitos  
A ==Especificação de Requisitos de Software (SRS)== formaliza o acordo entre stakeholders[^1], descrevendo funcionalidades, casos de uso, restrições e itens fora de escopo. Além de evitar mal-entendidos, o documento ==serve como base para estimativas de custo e prazo==. Pressman (2016) ressalta que ==uma SRS bem elaborada reduz riscos de falhas no projeto==, garantindo clareza sobre o que o software deve (e não deve) fazer. A manutenção da documentação atualizada é crucial, mesmo após a entrega, para facilitar futuras modificações.  
<br>

[^1]: Partes interessadas, grupos de interesse


##### Requisitos Funcionais e Não Funcionais
Os ==requisitos funcionais (RF) definem o que o sistema deve fazer, englobando tarefas, serviços e comportamentos específicos==. Exemplos incluem cadastrar médicos, emitir relatórios ou alterar estados de processos (ex.: mudar status de cliente de "em consulta" para "consultado"). Esses requisitos ==orientam a arquitetura aplicativa do sistema e são críticos para o funcionamento== correto do software.  

Já os ==requisitos não funcionais (RNF) estabelecem critérios de qualidade e restrições técnicas, como desempenho, usabilidade, segurança e padrões de implementação==. Exemplos são tempos de resposta (ex.: relatório gerado em 5 segundos), conformidade com normas setoriais ou uso de tecnologias específicas (ex.: Java). Eles ==direcionam a arquitetura técnica do sistema== e garantem que as funcionalidades atendam a padrões de eficiência e confiabilidade.  

A distinção entre RF e RNF é fundamental: enquanto ==os primeiros focam em funcionalidades tangíveis, os últimos qualificam como essas funcionalidades devem ser entregues==. Ambos são essenciais para evitar mal-entendidos, definir limites do sistema (incluindo o que está fora do escopo) e fornecer bases realistas para estimativas de custo e prazo. A colaboração entre equipes técnicas e de negócio é vital para equilibrar expectativas, priorizando requisitos que agreguem valor ao cliente final. Documentar esses requisitos de forma clara e concisa, como em uma Especificação de Requisitos de Software (SRS), assegura alinhamento contínuo e reduz riscos de falhas no projeto.

##### Documentando Requisitos Funcionais
A documentação de requisitos funcionais via casos de uso é essencial para traduzir processos de negócio em funcionalidades claras e executáveis. Os casos de uso ==detalham como o software deve se comportar==, descrevendo fluxos de interação entre usuários e sistema. Eles são estruturados em três tipos de fluxos:  
1. **Fluxo Principal (FP)**: Sequência ideal de ações sem erros (ex.: cadastro de cliente com dados válidos).  
2. **Fluxo Alternativo (FA)**: Tratamento de situações anormais (ex.: CPF inválido durante o cadastro).  
3. **Fluxo de Exceção (FE)**: Ações opcionais não essenciais ao objetivo principal (ex.: consultar histórico de compras durante uma nova compra).  

Um caso de uso bem elaborado inclui:  
- **Nome e descrição** autoexplicativos (ex.: "UC01 – Comprar Produto").  
- **Pré-condições** (ex.: usuário logado).  
- **Fluxos detalhados** com numeração sequencial (FP, FA, FE).  
- **Regras de negócio** (ex.: cálculo de frete baseado em distância).  
- **Mensagens do sistema** (ex.: "CEP inválido").  

Exemplo prático: No caso de uso *Comprar Produto*, o fluxo principal inclui seleção de itens e finalização da compra, enquanto fluxos alternativos tratam de crédito não aprovado ou CEP inválido. Regras como o cálculo de frete (R$0,65/km + taxa por tipo de entrega) garantem precisão técnica.  

##### Estórias de Usuário
As estórias de usuário são centrais em metodologias ágeis, ==focando na experiência do usuário== e no valor entregue, em contraste com a abordagem tradicional baseada em casos de uso. Elas são descritas em linguagem simples, seguindo o formato: *"Como `[papel do usuário]`, quero `[ação]` para `[benefício]`"*. Exemplos incluem:  
- *"Como Vendedor, quero consultar estoques para oferecer produtos disponíveis."*  
- *"Como Aluno, preciso ver minhas notas para acompanhar meu desempenho."*  

Os **épicos** ==representam funcionalidades complexas divididas em estórias menores==, facilitando entregas incrementais. Por exemplo, um épico como "Gerenciamento de Pedidos" pode ser desdobrado em estórias como "Cadastrar Pedido" e "Rastrear Entrega".  

###### Benefícios das estórias de usuário  
- **Foco no usuário**: Priorizam necessidades reais, não apenas tarefas técnicas.  
- **Colaboração**: Promovem diálogo contínuo entre equipe técnica e usuários, mediado pelo *Product Owner* (PO), que atua como elo semelhante ao analista de requisitos em métodos tradicionais.  
- **Criatividade e ritmo**: Estimulam soluções inovadoras e mantêm a equipe motivada com entregas frequentes.  

###### Princípios INVEST  
Cohn (2004) define critérios para estórias eficazes:  
1. **Independente**: Não depende de outras estórias para fazer sentido.  
2. **Negociável**: Detalhes podem ser ajustados conforme discussões com o usuário.  
3. **Valiosa**: Deve agregar valor claro ao negócio ou usuário.  
4. **Estimável**: A equipe precisa compreendê-la para estimar esforço.  
5. **Pequena**: Deve ser granular, permitindo desenvolvimento em poucos dias.  
6. **Testável**: Requer critérios de aceitação claros (ex.: "O sistema deve exibir estoque atualizado em tempo real").  

##### Analisando um Exemplo de Descrição de Caso de Uso
###### Exemplo - Programa de Fidelidade de uma Loja Virtual
**Nome:** UC01 – Utilizar Programa de Fidelidade
**Descrição breve do caso de uso:** o objetivo deste caso de uso é verificar quanto o cliente já comprou em um ano e se a sua compra é passível de receber o desconto do programa de fidelidade.
**Pré-condições:** o cliente precisa ser um usuário válido, estar logado no sistema e efetuar uma compra no site.
**Fluxo Principal:**
1. Sistema acessa tabela Cliente com CPF_Cliente e retorna campo Status_Fidelidade
2. Se campo Status_Fidelidade = “Elegível”
	a. Sistema calcula 10% do valor total da compra realizada
	b. Sistema apresenta valor calculado no campo Desconto de Fidelidade
	c. Sistema atualiza o campo Valor_Total_Compras_Fidelidade da tabela Cliente = R$ 0,00
d. Sistema chama UC03 – Apresentar Carrinho de Compras
3. Se campo Status_Fidelidade = “Não Elegível”
a. Sistema mostra R$ 0,00 no campo Desconto de Fidelidade
b. Sistema atualiza o campo Valor_Total_Compras_Fidelidade da tabela Cliente somando o valor da compra que está sendo realizada
c. Sistema chama UC03 – Apresentar Carrinho de Compras

**Fluxos Alternativos:**
1.a: Cliente novo no site
4. Sistema mostra R$ 0,00 no campo Desconto de Fidelidade
5. Sistema chama UC03 – Apresentar Carrinho de Compras