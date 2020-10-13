# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita')
# arquivo.close()
#
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nMinha segunda escrita')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

def ler_arquivo(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto  = arquivo.read()
    print(texto)

def gravar_arquivo(texto):
    diretorio = ('C:/Users/baruk/Projects/app_python/Teste2.txt')
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        #print(x)
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum ([int(i) for i in notas]) / 4
        print(media(lista_notas))

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
    #atualizar_arquivo('Terceira linha.\n')
    #ler_arquivo('teste.txt')
    #gavar_arquivo('Arquivo em um diretorio especifico.\n')
    #aluno = 'Cesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    media_notas('notas.txt')