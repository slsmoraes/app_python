# Grava arqui com as notas dos alunos e calcula a média
import shutil
def ler_arquivo(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        #print(x)
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        #print(aluno)
        lista_notas.pop(0)
        #print(lista_notas)

        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    #import shutil esta no inicio
    shutil.copy(nome_arquivo, 'C:/Users/baruk/Projects')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/baruk/Projects/notasM.txt')

if __name__ == '__main__':
    # ler_arquivo('teste.txt')
    # gavar_arquivo('Arquivo em um diretorio especifico.\n')
    #aluno = '\nGaliane, 7, 8, 5, 6'
    #atualizar_arquivo('notas.txt', aluno)
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #copia_arquivo('notas.txt')
    move_arquivo('notas.txt')