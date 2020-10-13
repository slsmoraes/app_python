

def divisao_zero():
    try:
        divisao = 10 / 0
    except ZeroDivisionError:
        print('Não é possivel realizer uma divisão por zero')
def exececao_encadeada():
    try:
        arquivo = open('teste.txt', 'r')
        texto = arquivo.read()
        lista = [1, 10]
        divisao = 10 / 0
        numero = lista[1]
        #x = a
    except ZeroDivisionError:
        print('Não é possivel realizer uma divisão por zero')
    except IndexError:
        print('Indice fora do limite')
    except Exception as ex:
        print('Erro desconhecido. Erro: {}'.format(ex))
    else:
        print('Executa qdo não ocorrer erro!!!')
    finally:
        print('Sempre executa')
        print('Fechando o arquivo')
        arquivo.close()

if __name__ == '__main__':
    #divisao_zero()
    exececao_encadeada()
