import os
from hangman import jogar_hangman
from tic_tac_toe import jogar_tic_tac_toe
from funcionalidades_pontuacoes import mostrar_top_5

MENU = "---- Menu ----: \n" \
       "1 -> Tic Tac Toe \n" \
       "2 -> Hangman \n" \
       "3 -> Top 5 \n" \
       "4 -> Sair"


# Esta função permite obter a opção do menu que o utilizador quer executar.
# Caso o utilizador providenciar uma opção inválida, ele é informado disto e pede-se para introduzir a opção novamente.
# A função só termina quando o utilizador insere uma opção válida.
def obter_opcao_do_utilizador():
	print(MENU)  # Mostrar o Menu com as opções disponíveis
	while True:
		opcao = input("Insira o número da opção que desejas executar: ")
		if opcao in ["1", "2", "3", "4"]:  # se a opção não estiver presente nesta lista, ela é inválida
			return opcao
		else:
			print("A opção escolhida é inválida!")


# Esta função executa a opção que corresponde à escolha do utilizador.
def executa_opcao_escolhida(opcao, nome_do_jogador):
	# Apagar o conteúdo da consola sempre que uma funcionalidade vai ser executada (funciona para Windows e Linux)
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if opcao == "1":
		jogar_tic_tac_toe(nome_do_jogador)
	elif opcao == "2":
		jogar_hangman(nome_do_jogador)
	elif opcao == "3":
		mostrar_top_5()
	elif opcao == "4":
		print("Terminando o Programa. Obrigado por jogar, volte sempre!")
		exit()

	
# Esta função inicia o funcionamento do menu, que nada mais é que este ciclo:
#   Primeiro: As opções do menu são apresentadas para o utilizador e ele deve escolher qual quer executar;
#   Segundo: Ao escolher uma opção (válida), a funcionalidade relativa à esta opção é executada.
# Após uma funcionalidade terminar, o ciclo recomeça, ou seja, o programa só termina se o utilizador escolher a opção 4.
def iniciar_ciclo_principal(nome_do_jogador):
	while True:
		# Apagar o conteúdo da consola sempre que entrar no Menu (funciona para Windows e Linux)
		os.system('cls' if os.name == 'nt' else 'clear')
		opcao = obter_opcao_do_utilizador()
		executa_opcao_escolhida(opcao, nome_do_jogador)
