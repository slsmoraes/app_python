# Aula 5
lista = [1, 3, 5, 7, 2]
list_animal = ['cachorro', 'gato', 'elefante', 'arara']
#print(lista)
#print(list_animal[1])
# soma = 0
# for x in list_animal:
#     print(x)
# print('-----------------------')
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
# print(sum(lista))
# print(max(lista))
# print(min(lista))

# print(max(list_animal))
# print(min(list_animal))

# if 'gato' in list_animal:
#     print('existe um gato')

# nova_lista = list_animal * 3
# print(nova_lista)

# if 'lobo' in list_animal:
#     print('existe um lobo')
# else:
#     list_animal.append('lobo')
#     print(list_animal)

# list_animal.pop() #Retira o ultimo da lista
# print(list_animal)
# list_animal.pop(1) #Retira a posição especificada
# print(list_animal)

# list_animal.remove('elefante')
# print(list_animal)

# lista.sort()
# list_animal.sort()
# print(lista)
# print(list_animal)
# list_animal.reverse()
# print(list_animal)

# print('-------- Tupla é imutavel-------')
tupla = (1, 10, 12, 14)
# print(tupla)
# print(tupla[2])
# print(len(tupla))
# print(len(list_animal))
# print(len(lista))

print('-------- Converter lista para tupla----------')
tupla_animal = tuple(list_animal)
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)