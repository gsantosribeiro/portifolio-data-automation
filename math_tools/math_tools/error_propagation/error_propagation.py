import sympy as sp
import pandas as pd

def error_calculator(symbols,values,errors,dfs):
  somatory=0
  for i in range(len(values)):
    somatory += (dfs[i](*values)*errors[i])**2
  error = somatory**0.5
  return error

def main():

  dfs = []
  n = int(input("Digite o número de variáveis: "))
  symbols = sp.symbols(f'x1:{n+1}')
  values =[]
  errors = []
  for i in range (n):
    v = float(input(f"Digite o valor da grandeza {symbols[i]}: "))
    e = float(input(f"Digite o erro de {symbols[i]}: "))
    values.append(v)
    errors.append(e)

  #Escreva a função aqui (Potência: **)
  function = input("Digite a função (Ex: x1*x2**x3): ")
  try:
    f = sp.sympify(function)
    if not f.free_symbols.issubset(set(symbols)):
      print("Erro! Variáveis inválidas!")
      return
  except sp.SympifyError:
    print("Erro ao interpretar função!")
    return

  for symbol in symbols:
    df = sp.diff(f,symbol)
    df = sp.lambdify(tuple(symbols),df)
    dfs.append(df)

  print(f'Erro final: {error_calculator(symbols,values,errors,dfs)}')
main()
