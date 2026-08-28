num = int(input("Digite um número inteiro: "))

if num < 2:
    print(f"{num} NÃO é um número primo")
else:
    e_primo = True
    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break
    
    if e_primo:
        print(f"{num} É um número primo")
    else:
        print(f"{num} NÃO é um número primo")