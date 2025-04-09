##### O que é Mocking?
Mocking é a ==técnica de **simular componentes** (funções, módulos, APIs, bancos de dados) durante testes==, substituindo o comportamento real por versões controladas. Isso permite testar unidades de código **isoladamente**, sem depender de recursos externos.

##### Por que usar Mocks?
1. **Isolar testes**: Evitar que falhas em dependências externas afetem seu teste
2. **Evitar efeitos colaterais**: Não enviar e-mails reais, não modificar bancos de dados
3. **Controlar cenários**: Simular respostas específicas (sucesso, erro, dados fictícios)
4. **Velocidade**: Evitar esperar por APIs lentas ou operações complexas

##### Tipos Comuns de Mocks
1. **Funções** (`jest.fn()`)
2. **Módulos** (`jest.mock()`)
3. **APIs Externas**
4. **Banco de Dados**

##### Exemplos
###### Mock de Lista de Usuários (Simulação de API)
```js
// Mock de resposta de API
export const mockUsers = [
  {
    id: 1,
    name: "Leia Organa",
    email: "leia@rebelalliance.com",
    status: "active"
  },
  {
    id: 2,
    name: "Luke Skywalker",
    email: "luke@jediorder.org",
    status: "inactive"
  }
];

// Uso em teste:
test('Deve retornar usuários ativos', () => {
  const activeUsers = filterActiveUsers(mockUsers);
  expect(activeUsers.length).toBe(1);
  expect(activeUsers[0].name).toMatch(/Leia/);
});
```

###### Mock de Produtos (Banco de Dados Simulado)
```js
// Mock de dados de produtos
const mockProducts = [
  {
    id: "prod-001",
    name: "Lightsaber",
    price: 2999.99,
    inStock: true,
    tags: ["jedi", "weapon"]
  },
  {
    id: "prod-002",
    name: "Holocron",
    price: 4999.99,
    inStock: false,
    tags: ["artifact"]
  }
];

// Teste de busca:
test('Encontra produtos em estoque', () => {
  const availableProducts = findInStockProducts(mockProducts);
  expect(availableProducts).toHaveLength(1);
  expect(availableProducts[0].id).toBe("prod-001");
});
```

###### Mock de Formulário (Dados de Input)
```js
// Mock de dados de formulário
const mockFormData = {
  username: "DarthVader92",
  password: "DeathStar@123",
  preferences: {
    theme: "dark",
    notifications: true
  }
};

// Teste de validação:
test('Valida formulário complexo', () => {
  const isValid = validateForm(mockFormData);
  expect(isValid).toBeTruthy();
  expect(mockFormData.preferences.theme).toBe("dark");
});
```

###### Mock de Erro (Resposta de API com Falha)
```js
// Mock de erro de API
export const mockApiError = {
  status: 404,
  message: "User not found",
  details: {
    code: "USER_404",
    timestamp: "2024-03-20T12:00:00Z"
  }
};

// Teste de tratamento de erro:
test('Lida com erro de API', () => {
  const errorHandler = handleApiError(mockApiError);
  expect(errorHandler).toContain("not found");
  expect(mockApiError.details.code).toBe("USER_404");
});
```

###### Mock de Dados Aninhados (Relacionamentos Complexos)
```js
// Mock de dados relacionais
const mockOrder = {
  id: "ord-789",
  customer: {
    id: "cust-123",
    name: "Obi-Wan Kenobi",
    address: "Tatooine Desert"
  },
  items: [
    {
      productId: "prod-001",
      quantity: 2,
      price: 5999.98
    }
  ],
  total: 5999.98
};

// Teste de cálculo:
test('Calcula total do pedido', () => {
  expect(calculateOrderTotal(mockOrder)).toBe(5999.98);
  expect(mockOrder.items[0].quantity).toBe(2);
});
```
