# #------ Classe --------
# class Calculadora:
#     def __init__(self, num1, num2):
#         self.valor_a = num1
#         self.valor_b = num2
#     def soma(self): # Metodos
#         return self.valor_a + self.valor_b
#     def subtracao(self):
#         return self.valor_a - self.valor_b
#     def multiplicacao(self):
#         return self.valor_a * self.valor_b
#     def divisao(self):
#         return self.valor_a / self.valor_b
# calculadora = Calculadora(10,2)
# print(calculadora.valor_a)
# print(calculadora.valor_b)
# print('soma:          ', calculadora.soma())
# print('subtração:     ', calculadora.subtracao())
# print('multiplicação: ', calculadora.multiplicacao())
# print('divisão:       ', calculadora.divisao())

# ----- Metodo -------
# def soma(a, b): # Definição
#     return a + b
# def subtracao(a, b):
#     return (a - b)
# def multiplicacao(a, b):
#     return (a * b)
# def diviao(a, b):
#     return (a / b)
# print('soma: ', soma(3, 5))
# print('subtração: ', subtracao(10, 2))
# print('multiplicação: ', multiplicacao(10, 2))
# print('divisão: ', diviao(10, 2))

#------ Classe --------
class Calculadora:

    def soma(self, valor_a, valor_b): # Metodos
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
if __name__ == '__main__':
    calculadora = Calculadora()
    print('soma:          ', calculadora.soma(10, 2))
    print('subtração:     ', calculadora.subtracao(5, 3))
    print('multiplicação: ', calculadora.multiplicacao(10,5))
    print('divisão:       ', calculadora.divisao(100,2))