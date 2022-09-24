# jogo de pedra papel e tesoura com o computador
from random import shuffle

print("-=-"*8)
print("PEDRA, PAPEL E TESOURA")
print("-=-"*8)

player = int(input("1 - pedra, 2 - papel e 3 - tesoura: "))
ppt = [1, 2, 3]
shuffle(ppt)

if ppt[0] == 1:
    if player == 1:
        print("EMPATE! Foi pura sorte...")
    elif player == 2:
        print("Perdi :(. Papel ganha de pedra.")
    elif player == 3:
        print("Ganhei! Pedra ganha de tesoura.")
    else:
        print("Comando inválido, tente novamente.")
if ppt[0] == 2:
    if player == 1:
        print("Ganhei! Papel ganha de pedra")
    elif player == 2:
        print("EMPATE! Foi pura sorte...")
    elif player == 3:
        print("Perdi :(. Tesoura ganha de papel.")
    else:
        print("Comando inválido, tente novamente.")
if ppt[0] == 3:
    if player == 1:
        print("Perdi :(. Pedra ganha de tesoura.")
    elif player == 2:
        print("Ganhei! Tesoura ganha de papel.")
    elif player == 3:
        print("EMPATE! Foi pura sorte...")
    else:
        print("Comando inválido, tente novamente.")
