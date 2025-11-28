# Calculadora de Erro (Propagação de Incerteza)

Este módulo implementa uma calculadora de incerteza baseada na fórmula geral de propagação de erros:

\[
\Delta f = \sqrt{
\left(\frac{\partial f}{\partial x_1}\Delta x_1\right)^2 +
\left(\frac{\partial f}{\partial x_2}\Delta x_2\right)^2 +
\cdots
}
\]

## Como funciona

1. O usuário informa:
   - número de variáveis
   - valor de cada variável
   - erro associado a cada variável
   - a função simbólica (Ex: `x1*x2**2`)

2. O programa usa **SymPy** para:
   - interpretar a função
   - calcular derivadas parciais automaticamente
   - transformar as derivadas em funções avaliáveis (lambdify)

3. O erro final é calculado aplicando a fórmula acima.

## Requisitos

- Python 3
- sympy
- pandas (opcional, mas importado no código)

Instalação:

```bash
pip install sympy pandas
