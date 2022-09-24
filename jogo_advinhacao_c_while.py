# fazer a maquina pensar de 0 a 10 mas o jogador vai continuar tentando ate acertar
from random import shuffle

vezes = user = 0
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(num)
print("X"*53)
print("X Vou pensar em um numero de 0 a 10. Tente advinhar. X")
print("X"*53)
while user != num[0]:
    user = int(input("Em que número estou pensando? "))
    if num[0] != user:
        vezes += 1
        print("Errou! Tente novamente.")
if vezes == 0:
    print(f"Acertou! Não acredito! Foi de primeira!")
else:
    print(f"Acertou! Mas foram necessárias {vezes} tentativas.")
