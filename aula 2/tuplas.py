# Tupla é uma lista em que não posso alterar os elementos
t = 'a', 'b', 'c', 'd'
print(type(t))

t1 = 'a', #virgula para virar uma tupla

t2 = tuple("Fiap")
print(t2)
print(t2[1:3])  # Intervalo

#ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10
print(f'a: {a}, b: {b}')

email = "fulano@gmail.com"
usuario, dominio = email.split("@")  # caracter que separa esses requisitos

print(usuario)
print(dominio)