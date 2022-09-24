# cartilha de tabuado com while
while True:
    tab = int(input("De que número será a tabuada? "))
    print("*" * 19)
    print(f"*   TABUADA DE {tab}  *")
    print("*" * 19)
    for t in range(0, 11):
        print(f"{t} X {tab} = {t * tab}")
        tab += 1
    parar = input("Deseja continuar? [Digite N para parar] ").upper()
    if parar == "N":
        print("Finalizando aqui.")
        break
