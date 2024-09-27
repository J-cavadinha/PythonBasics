def fatorial(valor, iteracao):
    while iteracao > 0:
        valor = valor * iteracao
        iteracao -= 1
        fatorial(valor, iteracao)
    return valor

num = int(1)
print(f"O valor de {num} fatorial é {fatorial(num, num)}")