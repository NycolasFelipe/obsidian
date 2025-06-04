###### Tipos de Dados em SQL (Data Types)

O SGBD MySQL oferece diversas categorias de tipos de dados que definem as características de uma coluna, como o tipo de valor que ela pode conter, seu comprimento e, para números, sua precisão e escala. ==A escolha correta do tipo de dado é crucial para o uso eficiente do espaço de armazenamento==, uma tarefa importante para os administradores de banco de dados. Os tipos são agrupados em três categorias principais:

- **Tipos Numéricos:** Incluem valores inteiros (como `TINYINT`, `INT`, `BIGINT`), de ponto flutuante que não têm limite definido de precisão (como `FLOAT`, `DOUBLE`), e de ponto fixo com precisão e escala definidas (`DECIMAL`).
    
- **Tipos de Cadeia de Caracteres (String):** Dividem-se em binários e não binários. Os não binários, como `CHAR` e `VARCHAR`, são os mais comuns. A principal diferença é que `CHAR` ocupa um espaço fixo, enquanto `VARCHAR` ocupa apenas o espaço do dado armazenado mais um caractere de controle, sendo mais econômico para colunas com dados de tamanho variável.
    
- **Tipos Temporais:** Usados para armazenar datas e horas, incluem `DATE` (apenas data), `TIME` (apenas hora), `DATETIME` (data e hora sem fuso horário), `TIMESTAMP` (data e hora com base no fuso horário) e `YEAR` (apenas o ano).
    

###### SQL na Prática: Comandos Essenciais

Comandos iniciais úteis incluem `show databases;` para listar os bancos de dados existentes, `use <nome_do_banco>;` para se conectar a um banco de dados específico, `show tables;` para listar as tabelas, e `describe <nome_da_tabela>;` para visualizar a estrutura de uma tabela.

Os principais comandos são:

- **CREATE:** Utilizado para criar novos objetos. `create database <nome_do_banco>;` cria um novo banco de dados, e `create table <nome_da_tabela> (...);` cria uma nova tabela, definindo suas colunas e tipos de dados.
    
- **INSERT:** O comando `insert into <tabela> (colunas) values (valores);` é usado para adicionar novas linhas de dados a uma tabela.
    
- **SELECT:** É o comando fundamental para consultar dados. `select * from <tabela>;` retorna todas as colunas e linhas de uma tabela. A cláusula `where` permite filtrar os resultados com base em condições, e a cláusula `order by` é usada para ordenar a saída em ordem ascendente (padrão) ou descendente (usando `DESC`).
    
- **DROP:** Usado para excluir objetos de forma irreversível. `drop table <tabela>;` exclui uma tabela e todos os seus dados, enquanto `drop database <banco_de_dados>;` remove um banco de dados inteiro.
    

###### Chaves (PK, FK e UK) e Restrições (Constraints)

==As restrições (constraints) são regras aplicadas aos dados para garantir sua integridade==. As principais chaves são:

- **Chave Primária (Primary Key - PK):** Declarada com `primary key (coluna)`, identifica unicamente cada linha em uma tabela. Uma coluna definida como PK deve ser `NOT NULL`.
    
- **Chave Estrangeira (Foreign Key - FK):** Estabelece um vínculo entre duas tabelas. É declarada com `foreign key (coluna) references tabela_origem (coluna_origem)`, garantindo a integridade referencial. Isso impede, por exemplo, a inserção de um valor na tabela filha que não exista na tabela pai.
    
- **Chave Única (Unique Key - UK):** A restrição `UNIQUE` garante que todos os valores em uma coluna sejam exclusivos, similar à chave primária, mas uma tabela pode ter várias chaves únicas.
    
- **Chave Composta:** É uma chave primária formada pela união de duas ou mais colunas, comum em tabelas associativas resultantes de relacionamentos muitos-para-muitos.
    

Outras restrições importantes incluem:

- **NOT NULL:** Impede que uma coluna aceite valores nulos (vazios).
    
- **CHECK:** Valida se os valores em uma coluna atendem a uma condição específica.
    
- **DEFAULT:** Define um valor padrão para uma coluna caso nenhum valor seja fornecido durante a inserção.
    

###### Alterações e Propriedades Especiais

Para modificar a estrutura de uma tabela existente sem precisar recriá-la, utiliza-se o comando `ALTER TABLE`. Ele é combinado com outras cláusulas para realizar ações específicas:

- `ADD` para adicionar uma nova coluna.
    
- `MODIFY` para alterar o tipo de dado ou o tamanho de uma coluna existente.
    
- `CHANGE` para renomear uma coluna.
    
- `DROP` para excluir uma coluna.
    

Existem também propriedades especiais para colunas numéricas:

- **UNSIGNED:** Impede que uma coluna do tipo inteiro aceite valores negativos.
    
- **ZEROFILL:** Preenche os espaços não utilizados de um número com zeros à esquerda. Uma coluna com `ZEROFILL` é automaticamente `UNSIGNED`.
    
- **AUTO_INCREMENT:** Gera automaticamente um número sequencial para uma coluna, geralmente uma chave primária, a cada nova linha inserida. A coluna deve ser do tipo inteiro, `NOT NULL` e definida como chave primária ou única.