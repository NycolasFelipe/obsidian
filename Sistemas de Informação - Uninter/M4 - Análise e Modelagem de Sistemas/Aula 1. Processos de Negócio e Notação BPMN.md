##### O que são processos de negócios
Um processo de negócio é um ==conjunto estruturado de tarefas interligadas que visa produzir um produto ou serviço específico== para clientes. Se não gerar valor (produto/serviço), o processo não tem razão de existir. Exemplos incluem fabricação de carros, atendimento de pedidos, contratação de funcionários e compra de matéria-prima. Esses processos ==envolvem múltiplos departamentos, profissionais, sistemas e recursos==, garantindo eficiência e qualidade na entrega final.  

###### Classificando os processos de negócio  
Os processos são divididos em três categorias:  
1. **Primários (finalísticos)**: ==Atividades essenciais que cumprem a missão da empresa==, como produção de um carro ou venda de um serviço.  
2. **De suporte**: ==Apoiam os processos primários==, como contratação de pessoal (RH), manutenção de sistemas (TI) ou limpeza e segurança.  
3. **Gerenciais**: ==Coordenam e controlam atividades empresariais==, como gestão de projetos ou governança, garantindo alinhamento com metas estratégicas.  

###### Documentando os processos de negócio  
A documentação ==formaliza como a empresa opera, refletindo sua estratégia e diferencial competitivo==. Processos bem definidos padronizam resultados (ex.: McDonald’s, onde o sabor do sanduíche é consistente em qualquer loja) e reduzem riscos de erros ou perda de conhecimento com a saída de colaboradores. Empresas sem processos documentados enfrentam custos elevados em caso de falhas, como recalls em montadoras devido a peças incorretas no motor.  

###### Importância da gestão de processos  
Processos claros garantem eficiência, qualidade e criação de valor para o cliente. Eles permitem:  
- Padronização de atividades.  
- Visão integrada do fluxo de trabalho.  
- Melhoria contínua (identificação de falhas e otimizações).  
- Alinhamento com objetivos estratégicos (missão, visão e valores).  

###### Riscos de processos mal definidos  
Falhas na definição ou execução podem levar a prejuízos financeiros e de imagem. Exemplo: uma montadora que insere peças erradas no motor precisa arcar com recalls e reparos. Portanto, ==mapear e gerenciar processos é crucial para o sucesso empresarial==.

##### Mapeando os processos AS IS e elaborando o TO BE
O mapeamento de processos inicia com a ==identificação das características essenciais de um processo==, conforme Ogunnaike e Ray (1994): junção de atividades e recursos, objetivo global, foco no cliente, execução recorrente, estrutura clara de tarefas, entradas/processamento/saídas, e definição de desempenho e responsabilidades.

###### Entendendo os processos AS IS  
O **AS IS** ==representa o mapeamento do processo atual==, documentando seu fluxo real, incluindo etapas, envolvidos, problemas e oportunidades de melhoria. Para isso:  
- **Entrevistas e observação**: Engajar profissionais que executam o processo (atores), clientes e fornecedores para capturar a visão completa.  
- **Desafios**: Resistência de colaboradores (medo de automação ou críticas) exige empatia e sensibilidade do analista.  
- **Documentação**: Padronização com ferramentas como BPMN (Business Process Model and Notation) e validação com gestores para garantir fidelidade à realidade.  
- **Identificação de problemas**: Burocracia excessiva, atividades redundantes, prazos inadequados, riscos não tratados e custos elevados.  

###### Elaborando os processos TO BE  
O **TO BE** ==propõe o redesenho do processo, visando eficiência e alinhamento estratégico==. Passos críticos:  
- **Colaboração**: Envolver executores do processo, gestores e especialistas para garantir viabilidade e ganhos tangíveis.  
- **Priorização**: Trabalhar em blocos menores do processo para implementar melhorias controladas.  
- **Inovação**: Evitar restrições mentais e focar em simplificação, eliminando etapas sem valor.  
- **Validação**: Alinhar propostas com a alta gestão para garantir aderência à estratégia empresarial.  

###### Perguntas-chave para melhoria  
O analista deve estimular reflexões como:  
- Quais atividades não agregam valor?  
- O que pode ser eliminado, substituído, adicionado ou paralelizado?  
- Como reduzir custos e tempo, mantendo a qualidade?  

###### Implementação e avaliação  
==Documentar sugestões, definir responsabilidades e criar cronogramas para implantação==. ==Medir resultados pós-implementação== (ex.: redução de custos, aumento de produtividade) para validar eficácia. Processos TO BE bem definidos facilitam treinamento de equipes e permitem melhorias contínuas, fortalecendo a competitividade do negócio.  

**Exemplo prático**: Uma montadora que redesenha seu processo de fabricação (TO BE) após identificar falhas no AS IS (como peças incorretas no motor) evita recalls e custos de imagem, garantindo maior confiabilidade no produto final.

##### Conhecendo e aplicando a notação BPMN em processos de negócio  
A notação **BPMN (Business Process Model and Notation)** ==é um padrão global para modelar processos de negócio, integrando pessoas, tecnologia e estratégia==. Ela visa facilitar a comunicação clara entre stakeholders, representando fluxos de forma visual e intuitiva.  

###### Visão do BPM e BPMN  
- **BPM (Business Process Management)**: Disciplina que alinha processos à estratégia empresarial, englobando mapeamento, análise, redesenho e gestão de ponta a ponta.  
- **BPMN 2.0**: Versão atual da notação, usada em ferramentas como Bizagi Modeler. Elementos gráficos padronizados garantem clareza e aderência à realidade operacional.  

###### Elementos principais da BPMN  
1. **Piscina e Raia**:  
   - **Piscina**: Representa um participante do processo (ex.: empresa, cliente).  
   - **Raia**: Divide responsabilidades dentro de uma piscina (ex.: departamentos). <br> 
![[img_1.png|500]]
<br>
2. **Eventos**:  
   - **Início** (círculo verde) e **Fim** (círculo vermelho): Indicam disparadores externos (ex.: pedido do cliente) e conclusões do processo.<br>
   ![[Pasted image 20250426162521.png|120]]
   <br>
   
1. **Atividades/Tarefas** (retângulo): Ações executadas (ex.: "Verificar estoque", "Emitir fatura"). Podem ser manuais, automáticas ou subprocessos.<br>
   ![[Pasted image 20250426162612.png|120]]
   <br>
2. **Fluxo de Sequência** (seta): Liga elementos, definindo a ordem de execução.<br>
   ![[Pasted image 20250426162636.png|200]]
   <br>
3. **Gateway** (losango): Controla bifurcações (decisões) ou convergências de fluxos (ex.: estoque disponível vs. indisponível).<br>
   ![[Pasted image 20250426162717.png|120]]
   <br>
###### Exemplo prático: processo de atendimento de pedido  
- **Fluxo**: Inicia com solicitação do cliente → Atendente verifica estoque → Gateway direciona para "Pedido atendido" (caminho feliz) ou "Pedido recusado" (caminho alternativo).  
- **Ferramentas**: Bizagi Modeler, entre outras, permitem modelagem detalhada com elementos BPMN. <br>
  ![[Pasted image 20250426162926.png]]

###### Diferença entre tarefas e eventos  
- **Tarefas**: Ações internas pré-definidas, executadas por atores conhecidos (ex.: "Cadastrar cliente").  
- **Eventos**: Disparadores externos que iniciam/interrompem processos (ex.: "Recebimento de pagamento").  

###### Benefícios da BPMN  
- **Clareza**: Elimina ambiguidades com símbolos padronizados.  
- **Detalhamento**: Permite representar paralelismo, mensagens, temporizadores e subprocessos.  
- **Alinhamento estratégico**: Conecta execução operacional aos objetivos do negócio.  

**Exemplo de aplicação**: Em um processo de vendas, a BPMN pode modelar desde a entrada do pedido (evento) até a entrega (tarefa), identificando gargalos e otimizando etapas críticas.

##### Aprofundando o conhecimento da notação BPMN  
A BPMN oferece elementos especializados para detalhar processos, especialmente em cenários de automação (TO BE). Esses elementos permitem modelar interações com sistemas, mensagens e temporização, facilitando a transição para softwares.  

###### Especializações de tarefas  
As tarefas podem ser categorizadas para indicar **como** são executadas:  
1. **Comum**: Ação genérica sem detalhes de execução (ex.: "Analisar pedido").  
2. **Serviço**: Automatizada por sistema (ex.: cálculo automático de frete).  
3. **Recebimento**: Aguarda mensagem externa para prosseguir (ex.: confirmação de cliente via e-mail).  
4. **Envio**: Dispara comunicação externa (ex.: SMS de confirmação de pedido).  
5. **Usuário**: Requer interação humana com suporte de sistema (ex.: preenchimento de formulário em plataforma).  
6. **Script**: Execução automatizada via código (ex.: processamento noturno de vendas).  
7. **Manual**: Realizada totalmente por pessoa (ex.: ligação telefônica para cliente).<br>
   ![[Pasted image 20250426165159.png]]
###### Especializações de eventos  
Além de início e fim, eventos intermediários controlam fluxos complexos:  
- **Envio/Recebimento de Mensagem**:  
  - *Envio*: Sistema dispara mensagem (ex.: notificação de pagamento).  
  - *Recebimento*: Fluxo pausa até receber resposta (ex.: aprovação de proposta).  
- **Tempo**: Define prazos ou espera (ex.: aguardar 48h para resposta do cliente).<br>
  ![[Pasted image 20250426165350.png]]
  ![[Pasted image 20250426165314.png]]

###### Diferença entre tarefas e eventos em automação  
- **Tarefas**: Representam ações executáveis (com ou sem automação).  
- **Eventos**: Gerenciam condições externas ou temporais que influenciam o fluxo (ex.: espera por resposta).  

###### Aplicação prática  
- **Exemplo de automação**: Em um processo de contratação de seguro:  
  - *Evento de tempo*: Aguarda 2 dias para cliente responder.  
  - *Tarefa script*: Gera relatório de análise automática.  
  - *Tarefa de envio*: Dispara e-mail com proposta.  

###### Recursos para aprofundamento  
- **Ferramentas**: Bizagi Modeler permite aplicar elementos BPMN em fluxos.  
- **Documentação oficial**: OMG (Object Management Group) mantém padrões atualizados em [omg.org/spec/BPMN](https://www.omg.org/spec/BPMN/).  

**Nota**: Especializações são essenciais para TO BE automatizado, enquanto elementos básicos bastam para AS IS. A escolha depende do nível de detalhe necessário para implementação.

##### Exemplo de modelagem de processo
Modelagem do processo de vendas on-line de uma livraria virtual, com estoque próprio, múltiplos métodos de pagamento (cartão, boleto) e programa de fidelidade (10% de desconto para clientes com compras acima de R$500/ano).

![[Pasted image 20250426170247.png]]