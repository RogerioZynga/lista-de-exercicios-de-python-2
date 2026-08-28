print("Operação -- Adição!")
while True:
 numero1 = float(input("Digite o primeiro numero: "))
 numero2 = float(input("Digite o segundo numero: "))
 soma = numero1 + numero2
 print(f"{numero1} + {numero2} = {soma}")
 pergunta = input("Deseja realizar mais uma soma? [S ou N]").upper()
 if pergunta == "N":
   break

