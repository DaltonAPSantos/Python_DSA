import random
from os import system, name

def limpa_tela():
    # Limpa a tela do console
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpa_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    palavras = ["homem de ferro", "hulk", "thor", "capitao america", "pantera negra", "gaviao arqueiro", "viuva negra", "doutor estranho", "homem aranha", "deadpool"]

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances>0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ",chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -=1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era: ",palavra)
    
if __name__ == "__main__":
    game()
    print("\n Parabéns. Você está aprendendo programação em Python com a DSA.\n")