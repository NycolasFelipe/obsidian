##### Estrutura Básica Recomendada
```bash
meu-projeto/
├── src/                 # Código-fonte
│   ├── utils/           # Funções utilitárias
│   ├── components/      # Componentes (React/Vue/etc)
│   └── services/        # Lógica de negócio/APIs
│
├── __tests__/           # Testes unitários
│   ├── utils/           # Testes de utilitários
│   ├── components/      # Testes de componentes
│   └── services/        # Testes de serviços
│
├── jest.config.js       # Configuração do Jest
├── babel.config.js      # Configuração do Babel (se necessário)
├── package.json
└── README.md
```

##### Variações Comuns de Estrutura
###### Testes Junto ao Código (Flat Structure)
```bash
src/
├── utils/
│   ├── math.js
│   └── math.test.js     # Teste colado no arquivo
```

###### Diretório Separado de Testes
```bash
tests/
├── unit/
│   ├── utils.test.js
│   └── services.test.js
```

###### Agrupado por Funcionalidade
```bash
src/
├── feature-auth/
│   ├── index.js
│   ├── auth.service.js
│   └── __tests__/       # Testes específicos da feature
│       ├── auth.service.test.js
│       └── auth.hooks.test.js
```