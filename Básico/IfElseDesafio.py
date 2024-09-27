x = True
while x:
    try:
        temperatura_carne = int(input("Qual é a temperatura da carne? "))
        print(f"Temperatura registrada {temperatura_carne}")
        x = False
    except ValueError:
        print("Erro: valor inválido")

if temperatura_carne < 48:
    print("A carne está crua.")

elif temperatura_carne in range (48, 53):
    print("A carne está selada.")

elif temperatura_carne in range (54, 59):
    print("A carne está ao ponto para mal passada.")

elif temperatura_carne in range (60, 64):
    print("A carne está ao ponto.")

elif temperatura_carne in range (65, 70):
    print("A carne está bem passada.")

else:
    print("Queimou.")