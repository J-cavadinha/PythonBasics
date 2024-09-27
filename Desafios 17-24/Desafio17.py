idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("Você é uma criança.")
elif idade in range(13, 20):
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")