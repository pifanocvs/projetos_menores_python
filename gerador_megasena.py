# gerador de jogos mega sena
from random import randint

jogo = []
qntd = int(input("Quantos jogos você quer gerar? "))
for i in range(1, qntd + 1):
    jogada = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    sorted(jogada)
    jogo.append(jogada[:])
    jogada.clear()
print(jogo)
