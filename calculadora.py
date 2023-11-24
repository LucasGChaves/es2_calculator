class Calculadora:

  def soma(self, a, b):
    return a + b

  def subtracao(self, a, b):
    return a - b

  def multiplicacao(self, a, b):
    return a * b

  def divisao(self, a, b):
    if b == 0:
      raise ValueError('Não é possível dividir por zero.')
    return a / b

  def calcula(self):
    print("Calculadora simples")
    print("Selecione a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Operação: ")
    numero1 = float(input("Número 1: "))
    numero2 = float(input("Número 2: "))

    if operacao == "1":
      resultado = soma(numero1, numero2)
    elif operacao == "2":
      resultado = subtracao(numero1, numero2)
    elif operacao == "3":
      resultado = multiplicacao(numero1, numero2)
    elif operacao == "4":
      resultado = divisao(numero1, numero2)
    else:
      print("Operação inválida.")

    print("Resultado:", resultado)