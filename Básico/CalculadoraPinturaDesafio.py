def area_parede(altura, largura):
    return altura * largura

def qtd_latas(area, rendimento):
    return area/rendimento

# Main
x = True
while x:
    try:
        rendimento = float(input("Digite o rendimento da tinta: "))
        altura = float(input("Digite a altura da parede: "))
        largura = float(input("Digite a largura da parede: "))
        x = False
    except ValueError:
        print("Erro: Valor inválido. Tente novamente.")

area = area_parede(altura, largura)
print(f"A quantidade de latas necessárias é de {qtd_latas(area, rendimento)}")