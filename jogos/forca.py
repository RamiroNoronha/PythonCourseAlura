

def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")
    numero_de_tentativas = 0
    print("Escolha uma dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Dificuldade: "))
    if(dificuldade == 1):
        numero_de_tentativas = 10
    elif(dificuldade == 2):
        numero_de_tentativas = 7
    elif(dificuldade == 3):
        numero_de_tentativas = 5

    # while numero_de_tentativas > 0:


    print("Fim de jogo")
if(__name__ == "__main__"):
    jogar()