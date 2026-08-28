numeros = []
while True:
    numerol = input("Digite um número (N para terminar): ")
    if numerol.upper() == "N":
        break
    numero = float(numerol)
    numeros.append(numero)

print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
print("Soma dos valores:", sum(numeros))
    