numeros = []
while True:
    numerol = input("Digite um número de 0 a 1000 (N para terminar): ")
    if numerol.upper() == "N":
        break
    numero = float(numerol)

    if numero <0 or numero >1000:
     print("Digite um número entre 0 e 1000")
     continue

    numeros.append(numero)

print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
print("Soma dos valores:", sum(numeros))