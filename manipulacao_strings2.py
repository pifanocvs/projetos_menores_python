# le um  numero de 0 a 9999 e moste os digitos separados
num = input("Digite um numero de 0 - 9999: ")
u = int(num) // 1 % 10
d = int(num) // 10 % 10
c = int(num) // 100 % 10
m = int(num) // 1000 % 10
print(f"Analisando o número {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar{m}")
