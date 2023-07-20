import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo da adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    numero_total_tentativas = 0
    pontos = 1000
    print("Escolha uma dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    dificuldade = int(input("Dificuldade: "))

    if (dificuldade == 1):
        numero_total_tentativas = 20
    elif (dificuldade == 2):
        numero_total_tentativas = 10
    else:
        numero_total_tentativas = 5

    for tentativa in range(1, numero_total_tentativas + 1):

        print("Tentativa {} de {} ".format(tentativa, numero_total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute

        if (acertou):
            print("Você acertou! Sua pontuação foi: {}".format(pontos))
            break
        elif (maior):
            print("Você errou!, o número secreto é menor")
        else:
            print("Você errou!, o número secreto é maior")

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos
        if (tentativa == numero_total_tentativas):
            print("Você perdeu e sua pontuação foi 0")
    print("Fim de jogo, o número secreto é:", numero_secreto)

if(__name__ == "__main__"):
    jogar()