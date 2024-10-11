import os


# Esta é a função responsável por obter os dados dos jogadores no ficheiro correspondente a um determinado jogo.
# Providencia-se o nome do ficheiro e a função retorna os dados do ficheiro na forma de um dicionário.
# O dicionário é feito de forma que a chave seja o nome do jogador e o valor sejam os pontos deste jogador no jogo
def obter_dados_pontos_jogadores(nome_do_ficheiro_com_os_pontos):
	# Abre o arquivo no modo de leitura e escrita
	with open(nome_do_ficheiro_com_os_pontos, 'r') as arquivo:
		# Dicionário para armazenar os pontos de cada jogador
		pontos_jogadores = {}
		
		# Percorre as linhas do arquivo e extrai os pontos de cada jogador
		for linha in arquivo.readlines():
			# a linha do ficheiro está no formato "*Nome-Jogador* : *Pontos*". O objetivo é obter os dois
			nome_jogador, pontos_atual = linha.split(':')  # divide-se a linha em duas partes
			nome_jogador = nome_jogador.strip()  # removem-se espaços em branco no inicio e fim do nome do jogador
			pontos_atual = pontos_atual.strip()  # removem-se espaços em branco no inicio e fim dos pontos do jogador
			
			pontos_jogadores[nome_jogador] = int(pontos_atual)  # os dados do jogador são guardados no dicionário
	
	return pontos_jogadores


# Está função é chamada cada vez que um jogador termina uma partida de hangman para poder atualizar a sua pontuação.
def atualizar_arquivo_hangman(nome_jogador, tentativas):
	nome_do_ficheiro_com_os_pontos = "Pontos Hangman.txt"
	
	# este dicionario vai conter a relação entre os jogadores existentes e os respetivos pontos
	pontos_jogadores = obter_dados_pontos_jogadores(nome_do_ficheiro_com_os_pontos)
	
	# Atualizar os pontos do jogador caso a pontuação atual for melhor que a pontuação antiga, que no caso do hangman
	# ocorre quando o número de tentativas atual é menor que o número de tentativas antigo
	if nome_jogador in pontos_jogadores:
		antiga_pontuacao_do_jogador = pontos_jogadores[nome_jogador]
		if tentativas < antiga_pontuacao_do_jogador:
			pontos_jogadores[nome_jogador] = tentativas
	else:  # caso o jogador ainda não existir, as tentativas atuais são automaticamente as melhores tentativas
		pontos_jogadores[nome_jogador] = tentativas
		
	# escreve no ficheiro a lista atualizada de jogadores com os seus respetivos pontos
	# Utiliza-se o "w" para que o conteúdo do ficheiro seja apagado e o novo conteúdo substitua ele
	with open(nome_do_ficheiro_com_os_pontos, "w") as ficheiro_de_pontos:
		for jogador, pontos in pontos_jogadores.items():
			ficheiro_de_pontos.write(f"{jogador}: {pontos} \n")


# Vai ao ficheiro que contém os pontos de cada jogador no jogo de tic-tac-toe
# e o atualiza conforme a vitória de um jogador
def atualizar_arquivo_tic_tac_toe(nome_jogador):
	nome_do_ficheiro_com_os_pontos = "Pontos Tic-Tac-Toe.txt"
	
	# este dicionario vai conter a relação entre os jogadores existentes e os respetivos pontos
	pontos_jogadores = obter_dados_pontos_jogadores(nome_do_ficheiro_com_os_pontos)
	
	# Atualizar os pontos do jogador
	if nome_jogador in pontos_jogadores:  # Se ele já existir, aumenta-se o número de vitórias atuais
		pontos_jogadores[nome_jogador] += 1
	else:  # Se for um jogador novo, ele deve ser adicionado
		pontos_jogadores[nome_jogador] = 1
	
	# escreve no ficheiro a lista atualizada de jogadores com os seus respetivos pontos
	# Utiliza-se o "w" para que o conteúdo do ficheiro seja apagado e o novo conteúdo substitua ele
	with open(nome_do_ficheiro_com_os_pontos, "w") as ficheiro_de_pontos:
		for jogador, pontos in pontos_jogadores.items():
			ficheiro_de_pontos.write(f"{jogador}: {pontos} \n")


# Esta função, dado o nome de um jogo, mostra a Top 5 dos jogadores para este mesmo jogo.
def mostrar_top_5_do_jogo(nome_do_jogo):
	# Apagar o conteúdo da consola (funciona para Windows e Linux)
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"Mostrando a Top 5 para o jogo: {nome_do_jogo}\n")
	
	nome_ficheiro_com_pontos = f"Pontos {nome_do_jogo}.txt"
	pontos_jogadores = obter_dados_pontos_jogadores(nome_ficheiro_com_pontos)
	
	# As pontuações são ordenadas para poder selecionar a top 5
	if nome_do_jogo == "Tic-Tac-Toe":
		# No caso de Tic-tac-toe a ordem é crescente porque se querem os jogadores com o maior número de vitórias
		pontuacoes_ordenadas = sorted(pontos_jogadores.items(), key=lambda x: x[1], reverse=True)
		tipo_de_pontos = "Vitórias"
	elif nome_do_jogo == "Hangman":
		# No caso de Hangman a ordem é decrescente porque se querem os jogadores com o menos número de tentativas
		pontuacoes_ordenadas = sorted(pontos_jogadores.items(), key=lambda x: x[1])
		tipo_de_pontos = "Tentativas"
	
	# apanham-se os primeiros 5 jogadores para criar a top 5
	top_5 = pontuacoes_ordenadas[:5]
	
	# o enumerate associa cada jogador ao índice que ele tem no dicionário (começando em 0)
	# dados_jogador é uma tupla no formato: (nome_jogador, pontos_jogador)
	for posicao, dados_jogador in enumerate(top_5):
		lugar = posicao+1  # adiciona-se 1 unidade porque inicia-se em 0 e quere-se que inicie em 1
		nome_jogador = dados_jogador[0]  # o primeiro valor da tupla corresponde ao nome do jogador
		pontos_jogador = dados_jogador[1]  # o segundo valor da tupla corresponde aos pontos do jogador
		
		# Este print vai mostrar uma linha da top 5 no formato: Xº Lugar -> *Nome-Jogador* com Y *Tipo-Pontos*
		print(f"{lugar}º Lugar -> {nome_jogador} com {pontos_jogador} {tipo_de_pontos}")
	
	# Evita que o utilizador volte ao Menu imediatamente
	input("\nPressione qualquer botão para voltar ao Menu")


# Esta é a função chamada pelo Menu quando o utilizador escolhe a opção "Top 5". Permite que o utilizador especifique
# para qual jogo ele quer ver a top 5 e age de acordo com esta decisão.
def mostrar_top_5():
	# Mostram-se, para o utilizador, as opções de jogos que ele pode escolher para ver a respetiva top 5
	print("Mostrar Top 5 para: \n"
	      "    1 -> Tic-Tac-Toe \n"
	      "    2 -> Hangman")
	
	# Este ciclo só termina se o utilizador escolher uma opção válida de um jogo
	while True:
		opcao = input("Insira o número da opção que desejas executar: ")
		if opcao == "1":
			mostrar_top_5_do_jogo("Tic-Tac-Toe")
			break
		elif opcao == "2":
			mostrar_top_5_do_jogo("Hangman")
			break
		else:  # se a opção for inválida, o utilizador é informado
			print("A opção escolhida é inválida!")
