# um programa q peça o nome todo e faça
nome = input("Digite seu nome todo: ")
print(f"O nome com todas as letras maiusculas: {nome.upper()}")
print(f"O nome com todas as letras minusculas: {nome.lower()}")
print(f"Quantidade de  letras do nome (sem espaço): {len(nome) - nome.count(' ')}")
pri_pal = nome.split()
print(f"Quantidade de letras do primeiro nome: {pri_pal[0].count('') - 1}")
