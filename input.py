a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
# Comentario
soma = a + b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
resto = a % b

print(type (soma)) # Imprime o tipo da variavel
print('--------------------------')
print('Soma: {} Subtração: {} \n Multiplicação: {} Divisão: {} Resto: {}'
      .format(soma, subtracao, multiplicacao, divisao, resto))
print('--------------------------')
