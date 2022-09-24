# aproveitamento de jogador
from operator import itemgetter

gols = []
total = 0
aprov = {"Nome": str(input("Nome do jogador: ")),
         "Partidas": int(input("Partidas jogadas: "))}
if aprov["Partidas"] > 0:
    for i in range(1, aprov["Partidas"] + 1):
        gols.append(int(input(f"Quantos gols na partida {i}? ")))
        total += 1
    aprov["Gol"] = gols[:]
    aprov["Total"] = total
    print(aprov)
else:
    print(f"{aprov['Nome']}, não teve aproveitamento jogando {aprov['Partidas']} partidas.")
