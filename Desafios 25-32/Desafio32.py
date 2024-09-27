square = lambda x: x**2

lista = [1,2,3,4,5]

nova_lista = []
for i in range(len(lista)):
    nova_lista.append(square(lista[i]))

print(f"{nova_lista}")