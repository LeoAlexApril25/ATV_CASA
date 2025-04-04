import random

def jogo():
    n_computador = random.randint(0,5)

tentativa = int(input("Informe o numero:"))

if tentativa ==jogo():
    print("Parabens, voce acertou.")

else:
    print('Voce errou, tente novamente.')
    