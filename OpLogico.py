a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b:
    print('O maior número é: {}'. format(a))
else:
    print('O maior número é: {}'.format(b))
print('Final do programa')
#-----------------------------------------
print('-----------------------------------')
if a > b and a > c:
    print('O maior número é: {}'. format(a))
elif b > a and b > c:
    print('O maior número é: {}'.format(b))
else:
    print('O maiot número é {}'.format(c))
print('Final do programa')
#------------------------------------------
print('-----------------------------------')
resto = a % 2
if resto == 0:
    print('O número é par!')
else:
    print('O número é impar!')
#------------------------------------------
print('-----------------------------------')
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print('Foi digitado um número é par!!!')
else:
    print('Nenhum número par foi digitado!!!')

#-----------Média----------------------------
print('-----------------------------------')
n1 = int(input('Primeiro bimestre: '))
n2 = int(input('Segundo  bimestre: '))
n3 = int(input('Terceiro bimestre: '))
n4 = int(input('Quarto   bimestre: '))
media = (n1 + n2 + n3 + n4) / 4
if n1 <= 10 and n2 <= 10 and n3 <= 10 and n4 <= 10:
    print('Media: {}'.format(media))
else:
    print('Tem alguma nota errada!!!')