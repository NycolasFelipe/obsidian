##### Conceitos fundamentais da Análise de Requisitos
A análise de requisitos é essencial para definir ==o que um sistema deve fazer e suas restrições==, alinhando funcionalidades às necessidades do usuário e do negócio. Requisitos não são meros "desejos", mas ==demandas validadas que consideram viabilidade técnica e organizacional==. Dividem-se em:  
- **Requisitos de usuário**: ==descritos em linguagem natural, acessíveis a não especialistas== (ex: "o sistema não deve pagar horas não trabalhadas").  
- **Requisitos de sistema**: ==detalhados tecnicamente para orientar desenvolvedores== (ex: especificações de desempenho ou integração).  

###### Classificação dos requisitos  
1. **Funcionais**: definem ==ações do sistema== (ex: calcular salário, emitir relatório) e podem incluir restrições (ex: bloquear pagamentos sem autorização).  
2. **Não funcionais**: abrangem ==restrições globais, como desempenho, segurança e legislação== (ex: tempo de resposta máximo de 2 segundos).  
3. **De domínio**: ==específicos do contexto de atuação== (ex: sigilo em sistemas bancários ou normas sanitárias em hospitais).  

###### Documento de requisitos  
É a formalização das necessidades, servindo como contrato entre usuários e desenvolvedores. Segue padrões como o **IEEE 830**, com:  
- Visão geral do sistema.  
- Descrição de funcionalidades e restrições.  
- Critérios de validação (ex: testes de desempenho para verificar requisitos não funcionais).  

###### Processo de engenharia de requisitos  
1. **Estudo de viabilidade**: avalia se o projeto é alinhado aos objetivos organizacionais, tecnicamente possível e economicamente viável.  
2. **Elicitação**: técnicas como entrevistas, observação e cenários são usadas para capturar necessidades.  
3. **Validação**: verifica consistência, realismo e facilidade de teste (ex: garantir que um requisito possa ser comprovado após implementação).  
4. **Gerenciamento**: controla mudanças, rastreia impactos e mantém histórico de evolução (ex: uso de ferramentas CASE para documentação).  

###### Desafios e práticas  
- **Volatilidade**: ==requisitos mudam devido a contextos dinâmicos== (ex: novas tecnologias de autenticação, como biometria).  
- **Comunicação**: ==é crucial estabelecer empatia com usuários para evitar resistência== e garantir clareza nas demandas.  
- **Gerenciamento de mudanças**: ==exige análise de impacto em custo, prazo e qualidade==(ex: alterações tributárias em sistemas de vendas).  

==A engenharia de requisitos é iterativa==, exigindo adaptação contínua para equilibrar necessidades do usuário, restrições técnicas e mudanças organizacionais.