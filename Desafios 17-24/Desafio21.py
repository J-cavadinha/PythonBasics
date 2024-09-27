cidades = {"Rio de Janeiro", "São Paulo", "Recife"}

escolha = input("Digite o nome de uma cidade: ")

if escolha in cidades:
    print("A cidade está na lista de cidades.")
else:
    print("A cidade não está na lista de cidades.")