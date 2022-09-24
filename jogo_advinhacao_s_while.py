# programa q faz o computador gerar um numero de 0 a 5 e o usuario tem q advinhar qual é
from random import shuffle

num = [0, 1, 2, 3, 4, 5]
shuffle(num)
print("X"*53)
print("X Vou pensar em um numero de 0 a 5. Tente advinhar. X")
print("X"*53)
user = int(input("Em que número estou pensando? "))
if user == num[0]:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou! Pensei no número: {num[0]}")
