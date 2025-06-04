##### Questão 01: Criação de Diagrama e Casos de Uso
###### Parte I - Requisitos
Escolher 3 requisitos funcionais, 3 requisitos não funcionais e descrevê-los na área de requisitos do caderno de respostas.
<br>

**Requisitos Funcionais**
- RF01: O sistema deve permitir controle para acessar as portas de entrada via comando de voz para funcionários autorizados.
- RF02: O sistema deve ajustar automaticamente a iluminação e o ar-condicionado baseado na detecção de pessoas por câmeras.
- RF03: O sistema deve enviar notificações por Whatsapp quando forem detectadas pessoas não autorizadas.

**Requisitos Não Funcionais**
- RNF01: O sistema deve funcionar localmente para evitar dependência externa e garantir segurança.
- RNF02: O reconhecimento de voz deve demorar até 2 segundos para responder.
- RNF03: O sistema deve ser compatível com lâmpadas LED e ar-condicionadas já presentes no escritório.

###### Parte II - Diagrama de Casos de Uso (PlantUML)
Criar o diagrama de casos de uso com base em todos os 12 requisitos levantados e colocar o diagrama na área do diagrama do caderno de respostas.

###### Parte III - Requisitos Funcionais e Não Funcionais
Responda à pergunta: Dos requisitos que você coletou, como é realizada a identificação de qual requisito é funcional e qual é requisito não funcional?

Os requisitos funcionais descrevem o que o sistema deve fazer, funcionalidades e ações específicas. Já os requisitos não funcionais dizem como o sistema deve funcionar em termos de segurança, desempenho, compatibilidade, etc.
<br>

```uml 
@startuml
left to right direction

actor "Funcionário" as Funcionario
actor "Administrador" as Admin
actor "Sistema de Segurança" as Seguranca
actor "API WhatsApp" as WhatsApp

rectangle Sistema {
  usecase "Controlar acesso por voz" as UC1
  usecase "Ajustar iluminação automaticamente" as UC2
  usecase "Regular ar-condicionado" as UC3
  usecase "Detectar acesso não autorizado" as UC4
  usecase "Enviar notificação de segurança" as UC5
  usecase "Gerenciar configuração do servidor" as UC6
  usecase "Autenticar comando de voz" as UC7
  usecase "Integrar com hardware existente" as UC8
  usecase "Monitorar consumo de energia" as UC9
  usecase "Processar feed de câmeras" as UC10
  usecase "Atualizar permissões de funcionários" as UC11
  usecase "Manter segurança do sistema" as UC12
}

Funcionario --> UC1
Funcionario --> UC2
Funcionario --> UC3
Admin --> UC6
Admin --> UC11
Seguranca --> UC4
Seguranca --> UC10
UC4 --> UC5
UC5 --> WhatsApp
UC1 --> UC7
UC2 --> UC8
UC3 --> UC8
UC6 --> UC12
UC10 --> UC9
UC8 --> UC12

@enduml
```
<br>

![[Pasted image 20250504195318.png]]

##### Questão 02: Criação de Diagrama de Classes
###### Parte I - Requisitos
Escolher 3 requisitos funcionais e 3 requisitos não funcionais diferentes dos usados na questão 01 e colocar na área de requisitos do caderno de resposta, questão 02.
<br>
**Requisitos Funcionais**
- RF04: Registrar histórico de acessos e alterações no sistema.
- RF05: Permitir configuração de horários comerciais para automação de luzes e ar-condicionado.
- RF06: Realizar o backup automático diário dos dados do sistema.

**Requisitos Não Funcionais**
- RNF04: O sistema deve ser utilizável por funcionários com treinamento básico em informática.
- RNF05: A interface de voz deve reconhecer comandos em português brasileiro com 95% de precisão.
- RNF06: O sistema deve permitir adicionar até 20 novos dispositivos sem perda de desempenho.

###### Parte II - Diagrama de Classes (PlantUML)
Criar o diagrama de Classes com base nos 12 requisitos levantados e colocar o diagrama na área do diagrama do caderno de respostas.
<br>
```uml
@startuml

class SistemaAutomatizacao {
  - servidor: ServidorLocal
  - controleAcesso: ControleAcesso
  - gerenciadorEnergia: GerenciadorEnergia
  - notificador: Notificador
  - historicoAlteracoes: List<Registro>
  + iniciarSistema(): void
  + realizarBackupDiario(): void
  + registrarAlteracao(funcionario: Funcionario, descricao: String): void
}

class ControleAcesso {
  - usuariosAutorizados: List<Funcionario>
  - historicoAcessos: List<Registro>
  + autenticarVoz(comando: String): boolean
  + registrarAcesso(funcionario: Funcionario): void
}

class GerenciadorEnergia {
  - dispositivos: List<Dispositivo>
  - configHorarios: ConfiguracaoHorarios
  + ajustarIluminacao(): void
  + regularArCondicionado(): void
  + adicionarDispositivo(dispositivo: Dispositivo): void
}

class ConfiguracaoHorarios {
  - horarios: Map
  + definirHorario(dia: String, inicio: Time, fim: Time): void
}

class ServidorLocal {
  - capacidadeArmazenamento: int
  + armazenarDados(dados: Object): void
  + backupAutomatico(): void
}

class Notificador {
  - apiWhatsApp: APIWhatsApp
  + enviarAlerta(mensagem: String): void
}

class Funcionario {
  - nome: String
  - treinamentoBasico: boolean
  + solicitarAcesso(): void
}

class Dispositivo {
  - tipo: TipoDispositivo
  - status: boolean
  + ligar(): void
  + desligar(): void
}

enum TipoDispositivo {
  LUZ
  AR_CONDICIONADO
  CAMERA
}

class Registro {
  - data: Date
  - funcionario: Funcionario
  - tipoEvento: TipoEvento
  - descricao: String
}

enum TipoEvento {
  ACESSO
  ALTERACAO
}

class APIWhatsApp {
  + enviarMensagem(destinatario: String, mensagem: String): void
}

class InterfaceUsuario {
  + exibirMenu(): void
  + processarComandoVoz(comando: String): void
  + interfaceSimples(): void
}

SistemaAutomatizacao --> ControleAcesso
SistemaAutomatizacao --> GerenciadorEnergia
SistemaAutomatizacao --> ServidorLocal
SistemaAutomatizacao --> Notificador
SistemaAutomatizacao --> InterfaceUsuario
ControleAcesso --> Funcionario
ControleAcesso --> Registro
GerenciadorEnergia --> Dispositivo
GerenciadorEnergia --> ConfiguracaoHorarios
Notificador --> APIWhatsApp
InterfaceUsuario --> Funcionario
InterfaceUsuario --> ControleAcesso

@enduml
```

![[Pasted image 20250504202506.png]]
<br>
###### Parte III - Conversão de Requisitos em Classes
Como fazemos para converter um requisito ou um grupo de requisitos em uma classe para o diagrama de classes?
<br>
Para converter requisitos em classes, começamos primeiro identificando as entidades principais dos requisitos. Substitantivos relevantes tendem a se transformar em classes (funcionário, por exemplo), e ações tendem a se tornar métodos (registrar, solicitar, etc).

Também podemos agrupar requisitos relacionados em uma única classe, de forma a simplificar a modelagem. Por exemplo, o requisito "adicionar até 20 dispositivos" se transforma na classe "GerenciadorEnergia" que possui um método "adicionarDispositivo".