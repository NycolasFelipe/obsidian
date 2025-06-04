###### Fundamentos de Banco de Dados

O estudo de Banco de Dados é essencial para profissionais de tecnologia, visto que quase todas as informações são, de alguma forma, armazenadas em bancos de dados. 

Um Banco de Dados (BD) é um local para armazenar dados de uma aplicação, como informações de clientes, produtos e pedidos em um sistema de delivery. Ele pode ser definido como uma ==coleção de dados inter-relacionados e persistentes==.

###### Modelos de Banco de Dados

A estrutura de um banco de dados é representada por um modelo de dados. Os principais modelos são:

- **Hierárquico:** Criado na década de 1960, ==organiza os dados em uma estrutura de árvore com relações pai-filho==. Sua principal desvantagem é a rigidez, pois alterações na estrutura podem exigir a recriação de todo o banco de dados.
    
- **Rede:** ==Surgiu como uma evolução do modelo hierárquico, permitindo relações mais complexas== do que apenas pai-filho. Embora mais flexível para pesquisas, ainda sofria com a rigidez estrutural.
    
- **Orientado a Objetos:** ==Armazena informações na forma de objetos, que encapsulam tanto os dados quanto os comportamentos== (métodos) para manipulá-los.
    
- **Relacional:** Proposto nos anos 1970 por Edgar Frank Codd, este modelo ==representa os dados em tabelas (relações) que se interligam==. Sua flexibilidade e simplicidade na representação e manutenção o tornaram um padrão.
    
- **NoSQL (Não Relacional):** Utilizado para ==grandes volumes de dados não estruturados ou semiestruturados==, como em redes sociais e Big Data. Caracteriza-se pela flexibilidade, escalabilidade horizontal (adicionando mais máquinas) e alta performance.
    

###### Sistema Gerenciador de Banco de Dados (SGBD)

O SGBD é o ==software que atua como uma interface entre os usuários (ou aplicações) e os dados armazenados== fisicamente. Ele permite realizar operações como inserir, recuperar, atualizar e excluir dados. SGBDs conhecidos incluem MySQL, Oracle, SQL Server e PostgreSQL.

Um SGBD possui características essenciais, como:

- **Controle de redundância:** Armazena a informação em um único local para evitar duplicação e inconsistências.
    
- **Controle de concorrência:** Gerencia o acesso simultâneo de múltiplos usuários aos mesmos dados, garantindo a correção das operações.
    
- **Segurança e Controle de acesso:** Define permissões para diferentes usuários.
    
- **Integridade:** Garante que as regras definidas (ex: data de nascimento não pode ser no futuro) sejam cumpridas.
    
- **Backup e recuperação:** Oferece mecanismos para restaurar dados em caso de falhas.
    
- **Independência de dados:** Desvincula as aplicações da estrutura física de armazenamento dos dados.
    

Um sistema de banco de dados é um ecossistema composto por hardware, o SGBD, as aplicações e os usuários, que se dividem em programadores, usuários finais e o Administrador de Banco de Dados (DBA). ==O DBA é o profissional responsável por gerenciar o banco de dados, definir acessos, monitorar o desempenho e realizar manutenções==.

###### Modelagem e Projeto de Dados

A modelagem de dados visa representar um cenário do mundo real e suas necessidades de informação. O projeto de um banco de dados geralmente passa por quatro etapas, guiadas pelas regras de negócio:

1. **Análise de Requisitos:** Entendimento das necessidades.
2. **Modelo Conceitual:** Uma visão de alto nível e abstrata do banco de dados, independente de tecnologia. É a fase ideal para a comunicação com o usuário. A técnica mais comum aqui é o Modelo Entidade-Relacionamento (MER).
    
3. **Modelo Lógico:** Descreve o banco de dados considerando o tipo de SGBD (ex: relacional). Define tabelas, colunas e tipos de dados.
    
4. **Modelo Físico:** É a implementação real do banco de dados, descrevendo detalhadamente como os dados são armazenados e dependendo do SGBD específico escolhido.
    

###### Modelo Entidade-Relacionamento (MER)

Desenvolvido por Peter Chen, o MER é um modelo conceitual que descreve a realidade com base em três conceitos fundamentais:

- **Entidade:** Representa um objeto do mundo real sobre o qual se deseja guardar informações (ex: Cliente, Produto). As entidades podem ser **fundamentais** (independentes), **associativas** (nascem de um relacionamento) ou **fracas** (dependentes de outra entidade para existir).
    
- **Campo (ou Atributo):** São as propriedades ou características de uma entidade (ex: Nome, Endereço, Data de Nascimento para a entidade Cliente). Podem ser classificados como obrigatórios, opcionais, simples, compostos, monovolarados ou multivalorados.
    
- **Relacionamento:** É a associação que existe entre duas ou mais entidades (ex: um Cliente _reside em_ uma Cidade). Um relacionamento de uma entidade com ela mesma é chamado de autorrelacionamento.
    

Para identificar unicamente cada registro (instância) de uma entidade, usam-se **chaves**. A **chave primária (PK)** é um campo (ou conjunto de campos) cujo valor é único para cada registro e não pode ser nulo. A **chave estrangeira (FK)** é um campo em uma entidade que é a chave primária de outra entidade, servindo para estabelecer o relacionamento entre elas.

###### Cardinalidade

A cardinalidade define o número de instâncias de uma entidade que podem se relacionar com instâncias de outra entidade. É a regra que determina onde a chave estrangeira deve ser colocada. Existem três tipos básicos:

1. **Um para Um (1:1):** Uma instância de A se relaciona com no máximo uma de B, e vice-versa. Neste caso, a chave estrangeira pode ficar em qualquer uma das entidades.
    
2. **Um para Muitos (1:n):** Uma instância de A se relaciona com várias de B, mas uma de B se relaciona com apenas uma de A. A chave estrangeira (FK) deve sempre ser colocada na entidade do lado "muitos" (n).
    
3. **Muitos para Muitos (n:n):** Uma instância de A pode se relacionar com várias de B, e uma de B pode se relacionar com várias de A. Este tipo de relacionamento sempre exige a criação de uma nova entidade, chamada **entidade associativa**, para resolver a relação. Esta nova entidade conterá as chaves primárias de ambas as entidades originais como chaves estrangeiras.
    

A notação de cardinalidade também pode especificar um número **mínimo** e **máximo** de ocorrências, como (0,n), que significa que a relação é opcional (mínimo de zero) e pode ter muitas ocorrências (máximo de 'n'). Após a aplicação correta das regras de cardinalidade, um modelo final não deve conter relacionamentos n:n.