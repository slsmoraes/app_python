from Televisao import Televisao

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

from Classe import Calculadora
calculadora = Calculadora()
print(calculadora.subtracao(20, 5))

from Contador_letras import contador_letras, teste
lista = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista)
print('Total de letras por palavra da lista: {}'.format(total_letras))
print(teste())

