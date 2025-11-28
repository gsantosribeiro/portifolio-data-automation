@ -0,0 +1,24 @@
# Error Propagation Calculator

Script para calcular erro por propagação usando derivadas automáticas (SymPy).

## Funcionalidades

- Aceita qualquer função matemática simbólica (ex: x1*x2**2/sqrt(x3))
- Calcula derivadas parciais automaticamente
- Usa `lambdify` para transformar derivadas em funções reais
- Aplica a fórmula geral de propagação de incertezas
- Funciona para qualquer número de variáveis

## Como usar

Execute:

python error_propagation.py

E insira:

1. Número de variáveis  
2. Valores das grandezas  
3. Erros associados  
4. A função simbólica  
