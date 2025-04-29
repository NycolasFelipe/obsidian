##### Análise de sistemas – a história  
###### A Era da Informação e a Importância dos Sistemas  
O século XX marcou o início da Era da Informação, período que persiste com intensidade crescente. A informação tornou-se central na vida pessoal, profissional e social, exigindo mecanismos para filtrar dados úteis de irrelevantes. Nas organizações, decisões estratégicas dependem de informações precisas sobre clientes, mercado e concorrentes, que permitem analisar o passado, compreender o presente e prever o futuro. ==Sistemas de informação computacionais surgiram para organizar esses dados==, evoluindo para incorporar Business Intelligence (BI) e inteligência artificial, otimizando decisões e impulsionando resultados financeiros.  

###### Tecnologia da Informação e Desenvolvimento de Software  
A Tecnologia da Informação (TI) ==combina hardware e software para armazenar, processar e utilizar dados==, estruturando sistemas que sustentam e evoluem os negócios. Com a complexidade crescente dos softwares, metodologias padronizadas foram criadas para garantir confiabilidade, custo adequado e agilidade. A análise de sistemas emergiu como disciplina essencial, ==focada em entender processos e definir soluções lógicas para processar informações==.  

###### Modelagem na Análise de Sistemas  
==A análise de sistemas baseia-se em modelos que representam entidades físicas== (como clientes ou vendas) e funcionalidades do software. Esses modelos abrangem três domínios: informações (dados processados), funcionalidades (tarefas do sistema) e comportamento (interações com o ambiente externo). ==Para simplificar problemas complexos, utiliza-se o *particionamento*==, dividindo desafios em partes menores. Dois tipos de modelos são essenciais:  
- **Modelos de análise**: focam nos requisitos do cliente, sem detalhes técnicos.  
- **Modelos de projeto**: definem arquitetura, interfaces e componentes técnicos para a implementação.  

###### Métodos de Modelagem  
Três métodos destacam-se na evolução da análise de sistemas:  
1. **Estruturada**: ==prioriza decomposição funcional==, usando ferramentas como DFD (Diagrama de Fluxo de Dados) e Dicionário de Dados.  
2. **Essencial**: evolui da abordagem estruturada, ==focando em eventos externos== que acionam respostas do sistema.  
3. **Orientada a objetos**: ==modela entidades reais ou abstratas== (como "produto" ou "venda"), integrando dados e comportamentos em objetos.  

###### O Papel do Analista de Sistemas  
O analista de sistemas ==atua como ponte entre negócios e tecnologia, traduzindo necessidades empresariais em soluções técnicas==. Suas responsabilidades incluem projetar arquiteturas de software, documentar requisitos e garantir que os modelos sejam implementados corretamente pelos desenvolvedores. Para isso, requer conhecimento em metodologias de análise, padrões de desenvolvimento e compreensão tanto do contexto técnico quanto das demandas dos usuários finais. Profissionais dessa área devem ==equilibrar habilidades técnicas com visão estratégica==, garantindo que os sistemas atendam a objetivos de negócio e sejam sustentáveis a longo prazo.

##### Análise estruturada
###### Análise Estruturada: Modelagem Lógica e Evolução  
A análise estruturada é um ==método tradicional que foca na construção de modelos lógicos== de sistemas, priorizando a compreensão da lógica por trás das funcionalidades do software. ==Seu objetivo é fornecer uma especificação clara e sistemática==, usando técnicas gráficas como Diagramas de Fluxo de Dados (DFD), Dicionário de Dados (DD) e especificações de processos. Essas ferramentas facilitam a comunicação entre usuários, analistas e desenvolvedores, garantindo que o sistema atenda às necessidades do cliente e sirva como base para o projeto técnico.  

###### Evolução do Método  
Na década de 1970, os requisitos de software eram documentados apenas em texto, o que gerava ambiguidades. A análise estruturada evoluiu ao incorporar diagramas visuais para representar fluxos e estruturas de dados. Principais avanços incluem:  
- **Foco no novo sistema**: substituição da modelagem física por processos de negócio, evitando esforço em sistemas obsoletos.  
- **Distinção clara entre modelos lógico e físico**: o lógico define a essência do sistema; o físico aborda a implementação tecnológica.  
- **Diagramas complementares**: introdução do Diagrama de Transição de Estado (DTE) para sistemas em tempo real e do Diagrama de Entidades-Relacionamentos (DER) para estruturar dados e seus relacionamentos.  
- **Integração de ferramentas**: combinação coerente de diagramas para uma visão holística do software.  

###### Benefícios da Abordagem Estruturada  
- **Clareza para usuários**: DFDs facilitam a visualização do sistema proposto, superando a ambiguidade de narrativas textuais.  
- **Identificação precoce de conflitos**: fluxos lógicos expõem mal-entendidos antes da implementação.  
- **Padronização de dados**: o Dicionário de Dados resolve inconsistências de nomenclatura e promove qualidade no desenvolvimento.  
- **Interfaces transparentes**: integração com sistemas existentes é representada de forma intuitiva.  

###### Desafios e Limitações  
- **Esforço documental**: a elaboração detalhada do Dicionário de Dados e diagramas exige tempo, gerando resistência em equipes.  
- **Percepção de rigidez**: programadores podem sentir-se restritos por especificações detalhadas, reduzindo criividade.  
- **Necessidade de treinamento**: usuários e analistas precisam adaptar-se à leitura de diagramas, embora a linguagem do DFD seja simplificada.  
- **Aplicabilidade limitada**: o método é menos eficaz em sistemas complexos que demandam múltiplas perspectivas além do fluxo de dados.  

###### Contexto Atual
A análise estruturada ==mantém relevância em empresas com sistemas legados==, mas sua eficácia depende do contexto do projeto e da integração com outras metodologias para suprir suas lacunas.

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
  - **DFD Contexto**: Visão macro do sistema.  
  - **DFD Nível 0+**: Detalhamento gradual de processos (ex.: decompor "Processar pagamento" em subtarefas).  
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

##### Níveis de um DFD
Um Diagrama de Fluxo de Dados (DFD) ==organiza-se em camadas hierárquicas para simplificar a compreensão== de sistemas complexos. Começa com uma visão panorâmica e vai se aprofundando gradualmente, ==como se fosse um zoom que revela detalhes== passo a passo.  

No **nível de contexto** (ou nível 0), ==o sistema é retratado de forma ampla, como uma única "caixa preta"== que interage com entidades externas. Por exemplo, em um sistema de vendas, o DFD de contexto mostraria como o cliente envia um pedido, como a logística recebe a fatura e como o financeiro processa o pagamento, ==sem detalhar o que acontece dentro do próprio sistema==. É como ver o sistema de fora, identificando quem se conecta a ele e quais dados circulam nessas interações.  

![[Pasted image 20250428195251.png|500]]

Já o **nível zero** descompacta essa "caixa preta", ==dividindo o sistema em processos principais==. Usando o mesmo exemplo, o sistema de vendas seria decomposto em funcionalidades como "Criar Pedido" e "Processar Pedido", mostrando como os dados fluem entre essas etapas e onde são armazenados (como em um depósito de *Clientes* ou *Pedidos*). A numeração dos processos ajuda a rastrear cada parte do fluxo, mantendo a clareza mesmo em sistemas mais elaborados.

![[Pasted image 20250428195328.png|500]]

==Quando um processo do nível zero é muito complexo==, entra em cena o **nível intermediário**. Nele, ==cada macrofuncionalidade é detalhada em subprocessos==. Por exemplo, "Processar Pedido" pode ser dividido em "Validar Estoque", "Calcular Total" e "Emitir Fatura", revelando como cada etapa contribui para o todo. A hierarquia é mantida por meio de numeração (como 2.1, 2.2), criando uma ligação clara entre os níveis.  

![[Pasted image 20250428195410.png|400]]

A hierarquia do DFD permite que equipes trabalhem sem se perder em detalhes excessivos. Imagine um arquiteto que primeiro desenha a planta da casa (nível de contexto), depois detalha cada cômodo (nível zero) e, por fim, especifica a instalação elétrica de uma sala (nível intermediário). ==Essa abordagem garante que todos entendam o projeto como um todo==, mesmo que se concentrem em partes específicas.  

==A escolha de quantos níveis criar depende da complexidade do sistema==. Um pequeno aplicativo pode precisar apenas do contexto e do nível zero, enquanto um sistema bancário exigiria vários níveis intermediários para cobrir todas as regras e integrações.
