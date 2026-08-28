nome = input("Digite seu nome: ")

while len(nome) <= 3:
    print("O nome deve ter mais de 3 letras.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("A idade deve ser maior que 0 e menor que 150.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))

while salario <=0:
    print("O salário deve ser maior que 0.")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite o sexo (F/M): ").upper() # F/M/NB

while sexo != "F" and sexo != "M":
    print("Digite apenas F ou M.")
    sexo = input("Digite o sexo (F/M): ").upper()

estado_civil = input("Digite o estado civil (S/C/V/D): ").upper()

while estado_civil not in "SCVD":
    print("Digite apenas (S/C/V/D).")
    estado_civil = input("Digite o estado civil (S/C/V/D): ").upper()

print("\nDados Válidos!")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

