### **Resumo para Consulta Rápida**  
---

#### **1. Atributos**  
- **Nomes**: Potência, Mente, Maestria, Essência.  
- **Custo por Nível** (cumulativo):  
  - Nível 1: 3 pontos de Composição.  
  - Nível 2: +6 (total: 9).  
  - Nível 3: +9 (total: 18).  
  - Nível 4: +12 (total: 30).  

#### **2. Categorias**  
| Categoria       | Composição | Talento | Sortilégio |  
|-----------------|------------|---------|------------|  
| Ordinário       | 18         | 12      | 18         |  
| Insólito        | 24         | 18      | 15         |  
| Extraordinário  | 30         | 24      | 12         |  
| Sobrenatural    | 36         | 30      | 9          |  
| Ascendente      | 48         | 42      | 6          |  
| Pilar           | 60         | 54      | 3          |  

#### **3. Maturidade**  
| Maturidade | Modificador Composição | Experiência | Sortilégio |  
|------------|-------------------------|-------------|------------|  
| Infante    | -1/3                   | 12          | +6         |  
| Jovem      | 0                      | 24          | +3         |  
| Maduro     | +1/3                   | 36          | 0          |  
| Sênior     | -1/3                   | 48          | -6         |  

**Fórmula da Composição Total**:  
```  
Composição Total = Composição da Categoria + (Composição × Fração da Maturidade)  
```  
*Exemplo*:  
Categoria "Sobrenatural" (36) + Maturidade "Maduro" (+1/3):  
```  
36 + (36 × 1/3) = 48  
```  

---

#### **4. Habilidades e Perícias**  
- **Habilidades**:  
  - 16 habilidades, custo em **Talento**:  
    - Nível 1: 2 | Nível 2: 6 | Nível 3: 12.  
- **Perícias**:  
  - 48 perícias, custo em **Experiência**:  
    - Nível 1: 1 | Nível 2: 3 | Nível 3: 6.  

---

#### **5. Graduações**  
- Custo: **1 ponto de Experiência** cada.  
- Valide pré-requisitos (ex: "Alfabetização" requer Conhecimento 1).  

---

#### **6. Distribuição de Atributos por Categoria**  
| Categoria       | Especialista          | Equilibrado             | Generalista              |  
|-----------------|-----------------------|-------------------------|--------------------------|  
| Ordinário       | 1 Atributo Nível 3    | 2 Atributos Nível 2     | 3 Nível 1 / 1 Nível 2    |  
| Sobrenatural    | 1 Nível 4 + 2 Nível 1 | 2 Atributos Nível 3     | 4 Atributos Nível 2      |  
| Pilar           | 2 Atributos Nível 4   | 1 Nível 4 + 1 Nível 3   | 1 Nível 4 + 3 Nível 2    |  

---

### **Exemplo Prático**  
```python  
# Cálculo de Composição:  
categoria = "Sobrenatural"  # Composição base: 36  
maturidade = "Maduro"        # Modificador: +1/3  
composicao_total = 36 + (36 * 1/3) = 48  

# Atributos (Especialista):  
Potência N4 (30 pontos) + Mente N1 (3) + Maestria N1 (3) + Essência N1 (3)  
Total gasto: 30 + 3 + 3 + 3 = 39 (dentro de 48 ✅)  
```  

Guarde este resumo para consultar valores, custos e regras rapidamente! 📜