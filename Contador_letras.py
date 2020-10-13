def contador_letras(lista_palavras):
    contador = []
    for c in lista_palavras:
        qtd = len(c)
        # print('qtd: ', qtd)
        contador.append(qtd)
    return contador

def teste():
    return ('Teste modulo')

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'urubu']
    print(contador_letras(lista))