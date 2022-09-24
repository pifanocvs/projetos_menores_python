# cartilha de tabuada com for

tab = int(input("Qual é a menor tabuada? "))
tab2 = int(input("Qual é a maior tabuada? "))
for i in range(tab, tab2 + 1):
    print("*" * 19)
    print(f"*   TABUADA DE {tab}  *")
    print("*" * 19)
    for t in range(0, 11):
        print(f"{t} X {tab} = {t * tab}")
    tab += 1
