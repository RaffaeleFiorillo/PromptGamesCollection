import random
import os
from funcionalidades_pontuacoes import atualizar_arquivo_hangman

# Esta lista contém todas as etapas do jogo do hangman. Cada etapa corresponde ao íncide desta etapa na lista.
# Começando pela etapa 0 sendo no início do jogo, quando o jogador ainda não cometeu nenhum erro.
# Terminando pela etapa 9, que é quando o jogador perde porque esgotou todas as suas tentativas de adivinhar o número.
etapas_do_hangman = [
	"""
     ____
    |    |
    |
    |
    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |
    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |    |
    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|
    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |    |
    |
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |    |
    |   /
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |    |
    |   / \\
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |    |
    |  _/ \\
    |
    |________
    """,
	"""
     ____
    |    |
    |    O
    |   /|\\
    |    |
    |  _/ \\_
    |
    |________
    """
]

# o número maximo de tentativas que o jogador tem corresponde ao número de etapas até o boneco ficar completo
# faz-se -1 porque ao chegar na última etapa o jogador perde, ou seja, a última etapa não pode ser jogada.
maximo_numero_de_tentativas = len(etapas_do_hangman) - 1


# Esta é a função chamada quando o utilizador escolhe a opção no Menu para jogar Hangman.
# No final de cada jogo a pontuação do jogador (cujo nome foi passado como parametro) vai ser atualizada (caso for
# melhor que a sua pontuação anterior, ou seja, o número de tentativas atual é menor que o antigo)
def jogar_hangman(nome_jogador):
	# Escolher um número aleatório entre 0 e 1000
	numero_secreto = random.randint(0, 1000)
	
	tentativas = 0
	mensagem_de_ajuda = ""  # esta variável vai conter uma mensagem de ajuda conforme as jogadas feitas pelo utilizador
	while True:
		# Atualizar a imagem do jogo conforme as tentativas do jogador
		os.system('cls' if os.name == 'nt' else 'clear')  # apaga-se a consola para maior claridade
		print(etapas_do_hangman[tentativas])  # desenha-se o estado atual do jogo
		print(mensagem_de_ajuda)
		# Solicitar ao jogador para adivinhar o número
		palpite = input("Tente adivinhar o número entre 0 e 1000: ")
		
		# Verificar se o palpite é um número válido
		if not palpite.isdigit():
			mensagem_de_ajuda = "O valor inserido é inválido porque não é um número."
			continue
		
		palpite = int(palpite)
		tentativas += 1
		
		# Verificar se o palpite do jogador está correto
		if palpite == numero_secreto:
			print(f"\nParabéns! Você acertou o número em {tentativas} tentativas.")
			atualizar_arquivo_hangman(nome_jogador, tentativas)
			break
		elif tentativas == maximo_numero_de_tentativas:
			# caso o jogador perder, deve-se atualizar o desenho do boneco para mostrar que ficou completo então apaga-se
			# a consola e coloca-se o desenho da última etapa do hangman
			os.system('cls' if os.name == 'nt' else 'clear')
			print(etapas_do_hangman[tentativas])
			print("\nPerdeste! Ultrapassaste o número de tentativas e o boneco morreu.")
			break
		elif palpite < numero_secreto:
			mensagem_de_ajuda = f"O número é maior que {palpite}."
		else:
			mensagem_de_ajuda = f"O número é menor que {palpite}."
	
	# Evita que o utilizador volte ao Menu imediatamente
	input("\nPressione qualquer botão para voltar ao Menu")
