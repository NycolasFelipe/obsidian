###### Modelo Lógico ou Relacional

A modelagem relacional, também conhecida como modelagem lógica, é o ==processo de projetar um banco de dados onde todas as informações são armazenadas em tabelas==. Esse modelo, proposto inicialmente por Edgar Codd, baseia-se na teoria dos conjuntos e na álgebra relacional para manipular dados. Os principais componentes do modelo relacional são:

- **Relação:** O conjunto de dados que forma uma tabela.
    
- **Atributo:** O nome que identifica cada coluna em uma tabela.
    
- **Tupla:** Corresponde a cada linha ou registro de uma tabela.
    
- **Domínio:** Define o tipo de dado (inteiro, texto, data, etc.) e os valores permitidos para cada atributo.
    

A terminologia muda entre os modelos: "entidade", "campo" e "registro" no modelo conceitual se tornam, respectivamente, "relação", "atributo" e "tupla" no modelo relacional.

==A álgebra relacional é uma linguagem formal que usa operadores para manipular essas tabelas==. Os operadores fundamentais incluem a **seleção** (representada por σ), que filtra as linhas (tuplas) com base em uma condição, e a **projeção** (representada por π), que seleciona colunas (atributos) específicas de uma tabela.

==Para garantir a consistência dos dados, o modelo relacional utiliza **restrições de integridade**==, como a integridade referencial (uso de chaves estrangeiras), a unicidade (garantindo que um campo como o CPF não tenha valores repetidos) e a integridade de chave (cada tupla deve ter uma chave primária única).

###### Normalização

==A normalização é um processo de refinamento do modelo lógico que visa organizar as tabelas para minimizar a redundância de dados e evitar anomalias== de inserção, alteração e exclusão. O processo envolve a aplicação de um conjunto de regras chamadas **Formas Normais (FN)**. Embora existam cinco, na prática, as três primeiras são suficientes para a maioria dos casos.

- **Primeira Forma Normal (1FN):** ==Exige que a tabela tenha uma chave primária e que todos os atributos contenham valores atômicos==, ou seja, sem grupos de repetição ou valores múltiplos em um mesmo campo. Atributos repetitivos ou multivalorados são movidos para novas tabelas.
    
- **Segunda Forma Normal (2FN):** ==A tabela deve estar na 1FN e todos os seus atributos não-chave devem depender totalmente da chave primária composta==. Se um atributo depende apenas de parte da chave, ele deve ser movido para uma nova tabela.
    
- **Terceira Forma Normal (3FN):** ==A tabela deve estar na 2FN e não pode haver dependências transitivas, ou seja, nenhum atributo não-chave pode depender de outro atributo não-chave==. Atributos derivados, como um campo "total" que é resultado de um cálculo entre "quantidade" e "valor unitário", devem ser eliminados.
    

###### Conversão para o Modelo Físico

Esta é a ==fase final do projeto==, onde o modelo lógico (relacional) ==é convertido em uma implementação real== em um SGBD específico, como MySQL ou Oracle. Nessa etapa, o modelo lógico é traduzido para um script SQL que cria as tabelas, colunas, chaves e outras restrições no banco de dados. Ferramentas de modelagem como o DBDesigner podem automatizar a geração desse script. O arquivo físico do banco de dados geralmente é um arquivo único que contém não apenas os dados, mas também um dicionário de dados que descreve sua estrutura.

###### Outros Esquemas de Modelagem: Modelagem Dimensional

Além do modelo relacional, existe a modelagem dimensional, usada principalmente para _Data Warehouses_ (armazéns de dados) e _Business Intelligence_ (BI). Proposta por Ralph Kimball, essa técnica utiliza dados desnormalizados para otimizar a recuperação e análise de grandes volumes de informação. Seus componentes principais são:

- **Tabelas Fato:** Contêm as métricas e os dados numéricos do negócio, como valor total de vendas ou quantidade de produtos vendidos.
    
- **Tabelas Dimensão:** Descrevem os fatos e contêm atributos textuais usados para classificar e filtrar os dados, como tempo, produto, cliente e local.
    

Existem três modelos principais de esquemas dimensionais:

- **Star Schema (Modelo Estrela):** Um modelo simples onde todas as dimensões se conectam diretamente à tabela fato central. As dimensões não são normalizadas.
    
- **Snow Flake (Floco de Neve):** Um modelo mais normalizado onde as dimensões podem se relacionar com outras dimensões, assemelhando-se mais a um modelo relacional.
    
- **Fact Constellation (Constelação):** Um modelo mais complexo que contém múltiplas tabelas fato, geralmente para analisar dados com diferentes níveis de detalhamento.
    

###### Structured Query Language (SQL)

==A SQL é a linguagem padrão para comunicação com bancos de dados relacionais==. Desenvolvida inicialmente pela IBM na década de 1970, foi posteriormente padronizada pelo ANSI e pela ISO para garantir maior compatibilidade entre diferentes SGBDs. A linguagem está em constante evolução, com novas funcionalidades sendo adicionadas ao longo do tempo.

A SQL é dividida em subconjuntos de comandos:

- **DDL (Data Definition Language):** Para criar, alterar e excluir objetos do banco de dados (CREATE, ALTER, DROP).
    
- **DML (Data Manipulation Language):** Para inserir, atualizar e apagar dados nas tabelas (INSERT, UPDATE, DELETE).
    
- **DQL (Data Query Language):** Para consultar dados (SELECT).
    
- **DCL (Data Control Language):** Para gerenciar permissões de acesso (GRANT, REVOKE).
    
- **DTL (Data Transaction Language):** Para controlar transações (COMMIT, ROLLBACK).
    

==Uma **query** ou **script** é uma ou mais instruções SQL enviadas ao SGBD para execução.== Além do padrão ANSI, cada SGBD possui seu próprio **dialeto** (como PL/SQL para Oracle ou T-SQL para Microsoft SQL Server) para funcionalidades mais avançadas.