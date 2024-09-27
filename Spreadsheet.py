# Spreadsheet iniciante Python

# Print simples
# Aspas simples ou duplas

print("Oi") 

#####################

# Input simples

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
cidade = input("Qual é a sua cidade? ")

print("O " + nome + " tem " + str(idade) + " anos de idade e mora na cidade de " + cidade + ".")

#####################

# Casting

ano_nascimento = input("Qual é o seu ano de nascimento? ")
idade = 2024 - int(ano_nascimento)
print("A sua idade é " + str(idade))

#####################

# String formatada

nome = "João"
sobrenome = "Cavadinha"
ocupacao = "estudante"

texto = "O " + nome + " " + sobrenome + " é um grande [" + ocupacao + "]"
print(texto)
texto = f"O {nome} {sobrenome} é um grande [{ocupacao}]"
print(texto)

#####################

# If/Elif/Else

velocidade = 100

if velocidade > 100:
    print("Tá andando legal")
elif velocidade > 160:
    print("Calma ai calabreso")
else:
    print("Você é lerdo")

#####################

# For loop
# Parâmetro -> qtd de iterações

for i in range(5):
    print(i)

# Parâmetro 1 -> posição inicial do loop
# Parâmetro 2 -> posição final do loop

for i in range(1,5):
    print(i)

# Escrever cada letra em uma linha
palavra = "Anna Julia Toval"

for i in palavra:
    print(i)

#####################

# While loop
# Enquanto a condição é verdadeira, executa o código

i = 1
while i < 6:
    print(i)
    i +=1

#####################

# Função

def nomeDaFuncao(argumento1, argumento2):
    print(argumento1 + argumento2)

nomeDaFuncao(1,1)

#####################

# Função com um número ilimitado de argumentos
# Asterísco que faz isso

def somaNum(*numeros):
    soma = 0

    for i in numeros:
        soma += i
    return soma

print(somaNum(1,1))

#####################

# Funçao com un número ilimitado de argumentos com os parâmetros identificados
# Duplo asterísco
# Diferentes argumentos, diferentes parâmetros

def agencia(**carro):
    return carro

print(agencia(marca="Volkswagen", modelo="Gol", cor="Branca", placa=12345))
print(agencia(marca="Volkswagen", modelo="Fusca", cor="Azul"))
print(agencia(marca="Ferrari", cor="Vermelha"))
print(agencia(situacao="destruído"))

#####################

# Listas
# Representado por [] 

cidadesBrasileiras = ["Rio de Janeiro", "São Paulo", "Salvador", "Brasília"]
print(cidadesBrasileiras)

#####################

# Verificar ítens em uma lista
# Case-Sensitive

cores = ["amarelo", "rosa", "roxo"]
existe = "azul"
if existe in cores:
    print(f"A lista possui {existe}")
else:
    print(f"A lista não possui")

#####################

# Tuple
# "Lista" porém imutável, utiliza menos memória (logo, é mais rápida) que uma lista

paises = ("Brasil", "Estados Unidos", "Japão")

#####################

# Array
# Utilizar quando a lista for muito grande, tem as mesmas caractéristicas porém utiliza menos processa-
# mento que uma lista

from array import array

letras = array('u', ["a", "b", "c", "d"])
# Esse u é o tipo associado ao elementos, consultar o site da bib para ter todos

#####################

# Set
# Similar a lista, não aceita valores duplicados, não possui index
# Pode ser instanciado com {}

list1 = [10, 20, 30, 40] # Pode ser "set1 = {10, 20, 30, 40}"
list2 = [50, 30, 10, 100, 60]

set1 = set(list1)
set2 = set(list2)

print(set1 | set2) # Union, junta os sets
print(set1 - set2) # Difference, mostra os que tem no primeiro set e que não tem no segundo
print(set1 ^ set2) # Symmetric Difference, mostra oque tem de único nos sets
print(set1 & set2) # And, mostra oque os dois sets tem em comum

#####################

# Dicionários
# Utiliza index no formato keys and values

aluno = {"nome": "Ana", "idade": 21, "situação": "Aprovada"}
print(aluno["nome"])

aluno.update({"endereço": "Rua Araújo"}) # .update pode modificar valores existentes ou adicionar novo
aluno.keys() # retorna as chaves do dicionário
aluno.values() # retorna os valores " "
aluno.items() # retorna as chaves e os valores no formato de tupla


#####################

# Função .map()
# Muito utilizada com listas
# Aplica uma função a um iterable

# No exemplo temos uma função que multiplica um valor dado por 2
def mult2(x):
    return x * 2

# Agora temos uma lista a qual queremos aplicar a função para cada elemento
lista1 = [1, 2, 3, 4, 5]

# Usamos a função map para aplicar a função nos elementos
lista2 = map(mult2, lista1)

print(list(lista2))

#####################

# Generator Expressions
# Forma mais rápida para listas, dicionários
# Bem menos memória
# Basta substituir os colchetes por parênteses

from sys import getsizeof # Biblioteca para verificar o tamanho

# Simulação de uma iteração de lista normal com 1000
numeros = [x * 10 for x in range(1000)]
print(getsizeof(numeros))

# Mesma coisa mas com um generator expression
numeros = (x * 10 for x in range(1000))
print(getsizeof(numeros))

#####################

# Error Handling
# Mensagens customizadas para erros

try:
    lista1 = ["a", "b", "c"]
    print(lista1[3])
except IndexError:
    print("Error: Index out of bounds. Try again.")

#####################

# Classes

# Import bib do tempo atual
from datetime import datetime

# Criando a Classe
class Funcionario:
    # Construtor
    def __init__(self, nome, sobrenome, cargo, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.ano_nascimento = ano_nascimento

    def nomecompleto(self):
        return self.nome + " " + self.sobrenome
    
    def idade(self):
        ano_atual = datetime.now().year # Função da bib
        return ano_atual - int(self.ano_nascimento)

# Criando o objeto
funcionario1 = Funcionario("João", "Machado", "Gerente", "2004")

print(funcionario1.nomecompleto())
print(funcionario1.idade())