###### Sistemas de Informação Gerencial e Bancos de Dados  
A aula aborda a importância dos bancos de dados (BD) como elementos centrais dos sistemas de informação gerenciais (SIG), destacando sua função de armazenar e gerenciar dados para tomada de decisões.  

###### Conceitos Fundamentais  
- **Banco de Dados (BD)**: ==Coleção organizada de dados relacionados logicamente==, como fichários médicos ou agendas telefônicas.  
- **Sistema Gerenciador de Banco de Dados (SGBD)**: ==Software intermediário que controla o acesso ao BD, garantindo integridade, segurança e evitando redundâncias==. Exemplos de funções: controle de acesso (ex: dados financeiros restritos a setores específicos) e transações concorrentes (ex: reserva de assentos em voos).  

###### Tipos de Bancos de Dados  
1. **Hierárquico**: ==Estrutura em árvore (pai-filho), comum em mainframes==. Exemplo: estoque de loja com categorias (pai) e tamanhos (filho).  
2. **Rede**: ==Permite múltiplos relacionamentos entre registros== (como uma teia), reduzindo redundâncias.  
3. **Não-Relacional (NoSQL)**: ==Flexível, armazena dados não estruturados== (imagens, textos), usado em redes sociais e buscas.  
4. **Relacional**: ==Modelo mais comum, baseado em tabelas interligadas por campos-chave==. Exemplo: tabela "Clientes" relacionada a "Pedidos" via campo "CódigoDoCliente".  

###### Linguagem SQL  
- **Comandos Principais**:  
  - `SELECT`: Recupera dados (ex: `SELECT * FROM Clientes WHERE CPF = '123'`).  
  - `INSERT`: Adiciona registros (ex: `INSERT INTO Produtos VALUES (1, 'Camiseta')`).  
  - `UPDATE`: Altera dados (ex: `UPDATE Pedidos SET Status = 'Entregue' WHERE ID = 100`).  
  - `DELETE`: Remove registros.  
- Integrada aos SIG, o SQL opera em segundo plano, permitindo consultas e atualizações transparentes aos usuários.  

###### Importância e Modelagem de Dados  
- **Relevância**: BD suportam sistemas críticos (ex: e-commerce, controle aéreo) e lidam com grandes volumes de dados (IoT, redes sociais).  
- **Modelagem**: Etapa inicial de projeto, definindo tabelas, campos, relacionamentos e regras. Exemplo:  
  - Tabelas para "Produtos", "Categorias", "Clientes" e "Pedidos" em um e-commerce.  
  - Relacionamento "um-para-muitos" entre "Clientes" e "Pedidos".  
- **Fatores-chave**: Escalabilidade, segurança e integridade (ex: campos obrigatórios como "Nome" em "Clientes").  
