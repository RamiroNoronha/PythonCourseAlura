import random





def jogar():
    enforcou = False
    acertou = False
    palavra = carrega_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra]
    erro = 0
    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = pede_chute()
        if(chute in palavra):
            marca_chute_correto(chute, letras_acertadas, palavra)
            acertou = ("_" not in letras_acertadas)
        else:
            erro+=1
            desenha_forca(erro)
            enforcou = erro == 7

    imprime_mensagem_final(acertou, palavra)



def imprime_mensagem_final(acertou, palavra):
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)
        
def marca_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = chute
        index += 1

def pede_chute():
    chute = input("Letra: ")
    return chute.strip().upper()

def carrega_palavra_secreta():

    palavras = []
    with open("arquivo.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()
def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()