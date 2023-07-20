import  adivinhacao
import  forca


def escolher():
    print("*********************************")
    print("*******Bem vindo aos jogos*******")
    print("*********************************")

    print("(1) jogo da adivinhação, (2) jogo da forca")
    opcao = int(input("Opção: "))
    if(opcao == 1):
        adivinhacao.jogar()
    elif(opcao == 2):
        forca.jogar()
    else:
        print("Nenhuma das opções foi selecionada")



if(__name__ == "__main__"):
    escolher()