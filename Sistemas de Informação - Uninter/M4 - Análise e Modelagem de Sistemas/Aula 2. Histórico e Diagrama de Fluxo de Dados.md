##### Análise de sistemas – a história  
A **Era da Informação** (século XX em diante) impulsionou a necessidade de sistemas para processar dados em escala, separando informações úteis de ruído. Nas organizações, sistemas computacionais surgiram para otimizar decisões estratégicas (ex.: BI, IA) e gerenciar dados de clientes, mercado e concorrentes.  

**Tecnologia da Informação (TI)**: Combina *hardware* e *software* para armazenar, processar e distribuir dados, evoluindo para atender complexidades crescentes de negócios.  

###### Análise de sistemas  
Definida por Pressman (2016) como a ==prática de modelar entidades reais (ex.: cliente, venda) para compreender e projetar soluções de software==. Divide-se em:  
1. **Modelos de Análise**:  
   - **Domínio da informação**: Dados processados (ex.: entrada de usuários, saída em relatórios).  
   - **Funcionalidades**: Requisitos detalhados (ex.: processamento de pagamentos).  
   - **Comportamento**: Interações com ambiente externo (ex.: tempo de resposta, usabilidade).  
2. **Modelos de Projeto**:  
   - Arquitetura, interfaces (UI/UX) e componentes técnicos para implementação.  

**Princípios-chave**:  
- **Particionamento**: Dividir problemas complexos em partes gerenciáveis.  
- **Abstração progressiva**: Do entendimento do usuário final (essência) aos detalhes técnicos (implementação).  

###### Métodos de modelagem  
1. **Estruturada**:  
   - Foco em decomposição funcional.  
   - Ferramentas: DFD (Diagrama de Fluxo de Dados), Dicionário de Dados.  
2. **Essencial**:  
   - Baseada em eventos externos (ex.: ação do usuário) para derivar funções.  
3. **Orientada a Objetos**:  
   - Modela entidades do mundo real (ex.: "Produto" com atributos como código e preço).  
   - Objetos podem ser físicos (ex.: produto) ou abstratos (ex.: venda).  

###### Analista de sistemas  
Atua como **ponte entre negócio e tecnologia**, ==traduzindo requisitos em modelos técnicos==. Responsabilidades incluem:  
- Projetar soluções alinhadas à arquitetura definida.  
- Criar documentação para desenvolvedores (ex.: fluxos de processo, especificações).  
- Garantir que sistemas atendam a critérios de qualidade (ex.: desempenho, usabilidade).  

**Habilidades requeridas**:  
- Conhecimento em metodologias de análise (ex.: UML, BPMN).  
- Domínio de ferramentas de modelagem (ex.: Bizagi, Lucidchart).  
- Visão estratégica para alinhar software aos objetivos do negócio.  

**Exemplo prático**: Um analista modela um sistema de vendas, definindo entidades como "Cliente" e "Pedido", fluxos de pagamento e integração com módulo de fidelidade, garantindo que o software reflita as regras do negócio.

##### Análise estruturada
A análise estruturada visa criar **modelos lógicos** (não físicos) de sistemas, focando na lógica das funcionalidades e na comunicação clara entre usuários, analistas e desenvolvedores. Utiliza técnicas gráficas para especificar requisitos, integrando fluxos de dados, processos e estruturas de informação.  

###### Principais ferramentas  
1. **Diagrama de Fluxo de Dados (DFD)**:  
   - Representa fluxos de dados entre processos, entidades externas e armazenamentos (ex.: cliente → sistema → banco de dados).  
2. **Dicionário de Dados (DD)**:  
   - Padroniza termos e estruturas de dados (ex.: definição de "cliente" com atributos como ID, nome, e-mail).  
3. **Especificações de Processos**:  
   - Detalha a lógica de cada função (ex.: regras para calcular desconto em vendas).  

###### Evolução da análise estruturada  
- **Década de 1970**: Substituiu documentação narrativa por modelos visuais, reduzindo ambiguidades.  
- **Melhorias posteriores**:  
  - **Foco no novo sistema**: Abandonou a modelagem detalhada de sistemas legados.  
  - **Separação lógico vs. físico**:  
    - *Modelo lógico*: Essência do sistema (ex.: fluxo de vendas).  
    - *Modelo físico*: Implementação tecnológica (ex.: integração com API de pagamento).  
  - **Novos diagramas**:  
    - *Diagrama de Transição de Estados (DTE)*: Para sistemas em tempo real (ex.: controle de semáforos).  
    - *Diagrama Entidade-Relacionamento (DER)*: Modela dados e seus relacionamentos (ex.: cliente ↔ pedido).  

###### Benefícios  
- **Clareza visual**: DFDs facilitam o entendimento de usuários sobre o sistema proposto.  
- **Identificação de gaps**: Revela inconsistências em estágios iniciais (ex.: fluxos de dados incompletos).  
- **Integração de sistemas**: Mostra interfaces com sistemas existentes (ex.: conexão com ERP).  
- **Padronização**: Dicionário de dados resolve conflitos de nomenclatura (ex.: "cliente" vs. "consumidor").  

###### Desafios e limitações  
- **Resistência à documentação**: Manutenção do DD exige esforço contínuo.  
- **Complexidade limitada**: Dificuldade em modelar sistemas altamente interativos ou baseados em eventos.  
- **Percepção de rigidez**: Programadores podem sentir-se restritos por especificações detalhadas.  
- **Treinamento necessário**: Usuários e analistas precisam aprender a interpretar diagramas.  

###### Aplicação prática  
**Exemplo**: Em um sistema de e-commerce:  
- **DFD**: Mostra fluxo de "seleção de produto" → "carrinho" → "pagamento" → "confirmação".  
- **DER**: Define entidades como "Produto", "Pedido", "Pagamento" e seus relacionamentos.  
- **DD**: Padroniza "valor_total" como soma dos preços dos itens no carrinho.  

###### Contexto atual  
A análise estruturada ainda é relevante em **sistemas legados** ou projetos com foco em processos sequenciais. No entanto, métodos como análise orientada a objetos ganharam espaço em sistemas complexos e dinâmicos.

##### Diagrama de fluxo de dados (DFD)  
O **DFD** é uma ==ferramenta gráfica da análise estruturada que modela o fluxo de dados== entre processos, entidades externas e armazenamentos, focando na **lógica funcional** (não na implementação física) do sistema.  

###### Componentes principais  
1. **Processos (Transformações)**:  
   - **Função**: Representam ações/funcionalidades do sistema (ex.: "Cadastrar cliente", "Emitir nota fiscal").  
   - **Características**:  
     - Nomeados com **verbos** (ex.: *calcular*, *armazenar*).  
     - Podem ser manuais ou automatizados.  
     - Representados por círculos, retângulos arredondados ou "bolhas". <br>
       ![[Pasted image 20250426175537.png|400]]
       <br>
       
       

2. **Fluxos de Dados**:  
   - **Função**: Conectam componentes, mostrando o movimento de dados.  
   - **Tipos**:  
     - *Externo* (entidade ↔ processo).  
     - *Interno* (processo ↔ processo).  
     - *Acesso a memória* (processo ↔ depósito de dados). <br>
       ![[Pasted image 20250426175724.png|200]]
       <br>
       

3. **Depósito de Dados**:  
   - **Função**: Armazenamento lógico de dados (ex.: lista de clientes, histórico de vendas).  
   - **Diferença de BD**: Não representa estrutura física (ex.: tabelas SQL), apenas a necessidade de reter dados.  
   - **Nomeclatura**: Plural (ex.: *Clientes*, *Produtos*).<br>
     ![[Pasted image 20250426175812.png|400]]
     <br>

4. **Entidades (Terminadores)**:  
   - **Função**: Pontos de origem/destino de dados externos (ex.: cliente, fornecedor, sistema de pagamento).  
   - **Características**:  
     - Nome em maiúsculo e plural (ex.: *CLIENTES*, *FORNECEDORES*).  
     - Podem ser pessoas, sistemas ou dispositivos.<br>
       ![[Pasted image 20250426175922.png|300]]
       <br>

###### Princípios de modelagem  
- **Níveis de Abstração**:  
  - **DFD Nível 0 (Contexto)**: Visão macro do sistema.  
  - **DFD Nível 1+**: Detalhamento gradual de processos (ex.: decompor "Processar pagamento" em subtarefas).  
- **Boas Práticas**:  
  - Nomes claros e consistentes (ex.: evitar "Dados 1" → usar "Pedido").  
  - Evitar complexidade excessiva (dividir em subdiagramas).  
  - Validar consistência entre níveis.  

###### Exemplo prático  
**Sistema de Vendas**:  
1. **Entidade**: *CLIENTE* envia fluxo "Pedido" para o processo *Registrar Pedido*.  
2. **Processo**: *Verificar Estoque* consulta o depósito *PRODUTOS*.  
3. **Fluxo de Erro**: Se produto indisponível, envia "Notificação de Falta" para *CLIENTE*.  
4. **Depósito**: *PEDIDOS* armazena dados para emissão futura de nota fiscal.  

###### Vantagens  
- **Clareza Visual**: Facilita o entendimento de usuários e desenvolvedores.  
- **Foco na Lógica**: Separa análise (o *que* o sistema faz) de projeto (o *como*).  
- **Identificação de Gaps**: Revela fluxos incompletos ou redundantes.  

###### Limitações  
- Não modela **comportamento temporal** (ex.: sistemas em tempo real exigem Diagrama de Estados).  
- Dificuldade em representar **interações complexas** (ex.: loops dinâmicos).  

O DFD é ideal para sistemas baseados em processos sequenciais, mas complementado por outras ferramentas (DER, DTE) em cenários complexos.