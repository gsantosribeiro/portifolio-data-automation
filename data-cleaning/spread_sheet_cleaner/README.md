# Spread Sheet Cleaner

## 🚀 Descrição

O **Spread Sheet Cleaner** é um notebook Python projetado para **limpeza e normalização de planilhas Excel** de forma automática.  
Ele é ideal para lidar com dados sujos ou inconsistentes, comuns em planilhas de clientes, extratos contábeis, registros de vendas ou dados exportados de sistemas.

O notebook combina técnicas de **Pandas**, **regex** e **unicodedata** para tratar:

- Nomes de colunas bagunçados (espaços, acentos, símbolos)
- Valores numéricos inconsistentes (números por extenso, vírgulas, pontos, caracteres extras)
- Textos com espaços, acentos e caracteres indesejados
- Datas inválidas ou em formatos diferentes
- Linhas e colunas vazias
- Criação de planilhas de teste com dados aleatórios para validação do pipeline

---

## 🧰 Funcionalidades principais

1. **Normalização de colunas**
   - Remove espaços, acentos e símbolos
   - Converte para minúsculas
   - Substitui caracteres não alfanuméricos por `_`
   - Garante nomes de colunas consistentes para automação

2. **Normalização de texto**
   - Remove espaços extras, `None` ou `"nan"`  
   - Padroniza textos para minúsculas sem acentos  
   - Substitui caracteres inválidos por `_`  

3. **Normalização de valores numéricos**
   - Converte números por extenso (ex: `"vinte"` → 20)  
   - Remove caracteres extras (ex: `"R$ 10,50"` → 10.50)  
   - Padroniza ponto decimal  
   - Converte valores inválidos em `NaN`

4. **Normalização de datas**
   - Converte datas em múltiplos formatos para datetime  
   - Datas inválidas viram `NaN`  

5. **Pipeline completo**
   - Funções wrapper para aplicar limpeza em múltiplas colunas  
   - Função `limpeza_basica` para normalizar cabeçalho e remover colunas irrelevantes  

6. **Gerador de planilhas sujas**
   - Cria planilhas de teste aleatórias simulando dados reais bagunçados  

---

## 💻 Como usar

### 1. Abrir o notebook

No Google Colab ou Jupyter:  
data-cleaning/spread_sheet_cleaner/spread_sheet_cleaner.ipynb


### 2. Instalar dependências

```bash
pip install pandas numpy openpyxl

### 3. Rodar o notebook

- Opcionalmente, gere uma planilha suja para teste.
- Aplique o pipeline de limpeza nas colunas desejadas.
- Visualize o DataFrame já limpo.

### 4. Exemplo de resultado

**Antes (planilha bagunçada):**

- Nome: `" Beto"`, IDADE??: `"vinte"`, preço,unitário: `"R$ 5,00"`, Data: `"32/13/2022"`
- Nome: `None`, IDADE??: `25`, preço,unitário: `"10,50"`, Data: `"2023-01-01"`

**Depois (limpo):**

- nome: `beto`, idade: `20`, preco_unitario: `5.0`, data: `NaT`
- nome: `NaN`, idade: `25`, preco_unitario: `10.5`, data: `2023-01-01`
