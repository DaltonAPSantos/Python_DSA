# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

palavras = ["homem de ferro", "hulk", "thor", "capitao america", "pantera negra", "gaviao arqueiro", "viuva negra", "doutor estranho", "homem aranha", "deadpool"]

# Classe
class Hangman:

	# Método Construtor
     def __init__(self,palavra):
          self.palavra = palavra
          self.letras_descobertas = []
          self.letras_erradas = []

	# Método para adivinhar a letra
     def adiv(self,letra):
          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          return True
	
	# Método para verificar se o jogo terminou
     def endgame(self):
          return self.winnwe() or (len(self.letras_erradas) == 6)
          
		
	# Método para verificar se o jogador venceu
     def winner(self):
          if '_' not in self.hide_palavra():
               return True
          return False
		
	# Método para não mostrar a letra no board
     def attboard(self):
          rtn = ''
		
          for letra in self.palavra:
               if letra not in self.letras_escolhidas:
                    rtn += '_'
               else:
                    rtn += letra
          return rtn
		
	# Método para checar o status do game e imprimir o board na tela
     def displayboard(self):
          print (board[len(self.letras_erradas)])
		
          print ('\nPalavra: ' + self.hide_palavra())
		
          print ('\nLetras erradas: ',) 
		
          for letra in self.letras_erradas:
               print (letra,) 
		
          print ()
		
          print ('Letras corretas: ',)
		
          for letra in self.letras_escolhidas:
               print (letra,)
		
          print ()
