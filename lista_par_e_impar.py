# programa q leia x valores e coloque em uma lista e crie duas listas extras p colocar os pares e os impares
numeros = []
par = []
impar = []
cont = "S"
while cont == "S":
    num = int(input("Digite um numero: "))  # numero.append(int(input("Digite um numero: ")))
    numeros.append(num)
    cont = input("Deseja continuar? [S/N] ").upper()
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f"O numero digitados foram: {numeros}")
print(f"Os numeros pares foram: {par}")
print(f"Os numero impares foram: {impar}")
