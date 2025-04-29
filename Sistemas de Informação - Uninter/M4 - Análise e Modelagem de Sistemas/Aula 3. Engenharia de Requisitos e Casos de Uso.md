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