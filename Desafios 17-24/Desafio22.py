localizacoes = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington DC",
    "Argentina": "Buenos Aires",
    "Peru": "Lima",
    "Chile": "Santiago"
}

pais_escolhido = input("Digite um país: ")

if pais_escolhido in localizacoes:
    print(f"{pais_escolhido}, {localizacoes[pais_escolhido]}")
else:
    print("Sem dados para esse país.")