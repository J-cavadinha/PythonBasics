altura = float(input("Qual é a sua altura (cm)? "))
peso = float(input("Qual é o seu peso (kg)? "))

imc = float(peso / ((altura / 100) ** 2))

if imc < 18.5:
    print("Magreza.")

elif 18.5 <= imc < 24.9:
    print("Normal.")

elif 25 <= imc < 29.9:
    print("Sobrepeso.")

elif 30 <= imc < 39.9:
    print("Obesidade.")

else:
    print("Obesidade grave.")