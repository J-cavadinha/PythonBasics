estoque = ["BMW X6", "BMW I5", "BMW I8"]

carro = input("Digite o carro que deseja buscar em estoque: ")

if carro in estoque:
    print("O carro está em estoque.")
else:
    print("O carro não está em estoque.")