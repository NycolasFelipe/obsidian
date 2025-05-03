##### Conhecendo o Diagrama de Estado
O **Diagrama de Estado**, também chamado de *Diagrama de Máquina de Estados*, é um recurso da UML utilizado para ==representar mudanças no estado de um objeto durante sua existência no sistema==. Ele captura como eventos externos ou internos influenciam as transições entre estados, sendo especialmente ==útil em cenários onde objetos apresentam comportamentos complexos e regras específicas de transição==.  

Na UML, esse diagrama complementa outros, como o de **Caso de Uso** (focado em interações entre usuários e sistema), o de **Classe** (estrutura estática) e o de **Sequência** (fluxo temporal de mensagens). ==Sua aplicação é mais relevante em sistemas com objetos que possuem ciclos de vida dinâmicos==, dependendo de regras ou condições específicas para alterar estados.  

Os elementos fundamentais incluem:  
- **Estado**: c==ondição temporária de um objeto==, como um telefone em modo *ocioso* (no gancho) ou *ativo* (em uso).  
- **Evento**: ==gatilho para uma transição==, podendo ser *externo* (ação do usuário), *interno* (gerado pelo sistema) ou *temporal* (baseado em tempo, como inatividade após 5 minutos).  
- **Transição**: ==mudança entre estados==, como passar de *ocioso* para *ativo* ao retirar o telefone do gancho.  
- **Objeto**: ==entidade que sofre alterações==, como um aparelho telefônico.  

Um exemplo prático é o de um telefone analógico, onde os estados principais são *ocioso* e *ativo*. O evento de retirar o telefone do gancho inicia uma transição para o estado *ativo*, enquanto colocá-lo de volta retorna ao estado *ocioso*.  

![[Pasted image 20250503200506.png|400]]
<br>

O diagrama ==é recomendado para documentar sistemas com múltiplos estados== interdependentes e regras complexas, como validações ou temporizadores. Por outro lado, ==não é necessário em sistemas simples==, como um cadastro básico sem lógica de transição entre estados.  

##### Conhecendo o Diagrama de Atividades
