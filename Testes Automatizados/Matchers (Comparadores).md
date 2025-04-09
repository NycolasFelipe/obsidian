##### `toBeTruthy()`
Verifica se o valor é **"truthy"** (considerado verdadeiro pelo JavaScript).
**Não precisa ser exatamente `true`**

Exemplos:
```js
expect(1).toBeTruthy()		// Número != 0
expect('a').toBeTruthy()	// Strings não vazias
expect({}).toBeTruthy();	// Objetos
expect(true).toBeTruthy();	// true
```
<br>

##### `.toBeFalsy()`
Verifica se o valor é **"falsy"** (considerado falso pelo JavaScript).
**Não precisa ser exatamente `false`**

Exemplos:
```js
expect(0).toBeFalsy();			// 0
expect('').toBeFalsy();			// String vazia
expect(null).toBeFalsy();		// null
expect(undefined).toBeFalsy();	// undefined
expect(false).toBeFalsy();		// false
```
<br>

##### `.toBe()` (Igualdade Estrita `===`)
Compara **valor e tipo**:
```js
expect(1).toBe(1);			// Ok
expect('1').not.toBe(1);	// Falha (string vs number)
```
<br>

##### `.toEqual()` (Igualdade Profunda)
Compara **propriedades de objetos/arrays**:
```js
const obj = { a: 1 };
expect(obj).toEqual({ a: 1 }); // Ok (mesmo conteúdo)
```
<br>

##### `.toBeNull()`, `.toBeUndefined()`, `.toBeDefined()`
Específicos para `null` e `undefined`:
```js
expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect('value').toBeDefined(); // Não é undefined
```
<br>

##### `.toBeGreaterThan()`, `toBeLessThan()` (Números)
Comparações numéricas:
```js
expect(5).toBeGreaterThan(3);
expect(2).toBeLessThanOrEqual(2);
```
<br>

##### `.toMatch()` (Strings)
Verifica padrões usando Regex:
```js
expect('Hello World').toMatch(/World/);
```
<br>

##### `.toContain()` (Arrays)
Verifica se array contém um elemento:
```js
expect(['a', 'b']).toContain('b');
```
<br>

##### `.toThrow()` (Exceções)
Verifica se uma função lança erro:
```js
function errorFunc() { throw new Error('Erro!'); }
expect(() => errorFunc()).toThrow('Erro!');
```

