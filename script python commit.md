```python
import pathlib
from git.repo import Repo

# Requires GitPython - pip install GitPython

# Inicializa o repositório Git no diretório especificado (path)
# e obtém objetos para interagir com o repositório e o índice.
repo = Repo.init(pathlib.Path(__file__).parent.resolve()).git
index = Repo.init(pathlib.Path(__file__).parent.resolve()).index
origin = Repo.init(pathlib.Path(__file__).parent.resolve()).remotes[0]

# Apresentação do programa
print(f"{"#"*20} CONVENTIONAL COMMITS v1.0 {"#"*20}")
print()
print("Digite 0 em qualquer etapa para cancelar o commit.")

# Apresenta as opções de tipos de commit disponíveis ao usuário,
# seguindo a convenção de Conventional Commits.
print("""
Escolha um tipo de commit:
1 [test]: Qualquer tipo de criação ou alteração de códigos de teste.
Exemplo: Criação de testes unitários.

2 [feat]: Desenvolvimento de uma nova feature ao projeto. 
Exemplo: Acréscimo de um serviço, funcionalidade, endpoint, etc.

3 [refactor]: Refatoração de código que não tenha qualquer tipo de impacto no funcionamento do projeto.
Exemplo: Alteração do código para melhorar a performance.

4 [style]: Mudanças de formatação e estilo do código que não alteram o sistema de nenhuma forma. 
Exemplo:  indentações, remover espaços em brancos, remover comentários, etc.

5 [fix]: Correção de erros que estão gerando bugs no sistema.
Exemplo: Aplicar tratativa para uma função que não está tendo o comportamento esperado e retornando erro.

6 [chore]: Mudanças no projeto que não afetem o sistema ou arquivos de testes. Mudanças de desenvolvimento.
Exemplo: Remover arquivos que não são mais utilizados, modificar o .gitignore, etc.

7 [docs] Mudanças na documentação do projeto.
Exemplo: Adicionar informações na documentação da API, mudar o README, etc.

8 [build]: Mudanças que afetam o processo de build do projeto ou dependências externas.
Exemplo: Adicionar/remover dependências do npm, etc.

9 [revert] Reversão para um commit anterior.
""")

# Retorna o tipo de commit correspondente ao número fornecido.
def get_commit_type(num):
  if num == 1: return "test"
  if num == 2: return "feat"
  if num == 3: return "refactor"
  if num == 4: return "style"
  if num == 5: return "fix"
  if num == 6: return "chore"
  if num == 7: return "docs"
  if num == 8: return "build"
  if num == 9: return "revert"

# Solicita ao usuário que selecione um tipo de commit e retorna o tipo escolhido.
def select_commit_type():
  while True:
    print("Selecione um tipo de commit:")
    num = int(input(">>> "))
    if num == 0:
      quit()
    elif (num < 0 or num > 9):
      print("Tipo inválido.")
      print()
    else:
      print(f"Tipo de commit escolhido: [{get_commit_type(num)}]")
      print()
      return get_commit_type(num)

# Solicita ao usuário que insira o escopo da mudança e retorna o escopo.
def set_scope():
  while True:
    print("Insira o nome do escopo modificado. Exemplo: Tela de login, assets, etc.")
    scope = input(">>> ")
    if scope == "0":
      quit()
    elif (not scope):
      print("Insira o nome do escopo.")
      print()
    else:
      print(f"Escopo modificado: [{scope}]")
      print()
      return scope

# Solicita ao usuário que insira uma descrição detalhada da mudança e retorna a descrição.
def set_description():
  while True:
    print("Insira uma descrição. Exemplo: Correção de bug na página de matrícula.")
    description = input(">>> ")
    if description == "0":
      quit()
    elif (not description):
      print("Insira uma descrição.")
      print()
    else:
      print(f"Descrição: [{description}]")
      print()
      return description

# Loop principal do programa     
while True:
  commit_type = select_commit_type()
  scope = set_scope()
  description = set_description()
  
  commit_message = f"{commit_type}({scope}): {description}"
  
  print(f"git commit -m \"{commit_message}\"")
  print()
  
  print("Confirmar commit?")
  print("1. Sim")
  print("2. Tentar novamente")
  print("3. Sair")
  confirm = input(">>> ")
  
  if confirm == "1":
    # Adiciona um novo commit ao repositório
    index.commit(commit_message)
    origin.push()
    print()
    print("Commit e push realizado com sucesso.")
    quit()
  elif confirm == "2":
    print()
    continue
  else:
    quit()

```