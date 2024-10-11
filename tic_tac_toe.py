import random
import os
from funcionalidades_pontuacoes import atualizar_arquivo_tic_tac_toe


# Esta função retorna uma grelha limpa para ser utilizada cada vez que inicia uma nova partida do jogo Tic-Tac-Toe
# A grelha nada mais é que um dicionário onde as chaves são as coordenadas das posições jogaveis e o valor é
# um dos jogadores ("X" ou "O") caso algum deles escolher jogar naquela coordenada, ou um espaço em branco (" ")
def obter_grelha_limpa():
	grelha = {"1-1": " ", "2-1": " ", "3-1": " ",
	          "1-2": " ", "2-2": " ", "3-2": " ",
	          "1-3": " ", "2-3": " ", "3-3": " "}
	
	return grelha


# Dada uma grelha, a função verifica se algum dos jogadores venceu o jogo. Caso alguem ganhou, é retornado o seu símbolo
# Uma Pessoa ganha o jogo se posicionar o seu símbolo em três coordenadas consecutivas da grelha.
# Antes de realizar cada condição de vitória verifica-se que o símbolo inicial da sequência não seja um espaço em branco
# (" "), pois, se for, vale dizer que a sequência não é de vitória. Caso for encontrada uma sequência de vitória,
# retorna-se o símbolo naquela coordenada, pois é o mesmo das restantes coordenadas da sequência e corresponde ao
# símbolo do vencedor.
def verifica_vitoria(grelha):
	# Verificar se há vitórias em algumas das LINHAS ---------------------------
	# Linha 1
	if grelha["1-1"] != " " and grelha["1-1"] == grelha["2-1"] == grelha["3-1"]:
		return grelha["1-1"]
	# Linha 2
	if grelha["1-2"] != " " and grelha["1-2"] == grelha["2-2"] == grelha["3-2"]:
		return grelha["1-2"]
	# Linha 3
	if grelha["1-3"] != " " and grelha["1-3"] == grelha["2-3"] == grelha["3-3"]:
		return grelha["1-3"]
	
	# Verificar se há vitórias em algumas das COLUNAS --------------------------
	# Coluna 1
	if grelha["1-1"] != " " and grelha["1-1"] == grelha["1-2"] == grelha["1-3"]:
		return grelha["1-1"]
	# Coluna 2
	if grelha["2-1"] != " " and grelha["2-1"] == grelha["2-2"] == grelha["2-3"]:
		return grelha["2-1"]
	# Coluna 3
	if grelha["3-1"] != " " and grelha["3-1"] == grelha["3-2"] == grelha["3-3"]:
		return grelha["3-1"]
	
	# Verificar se há vitórias em algumas das DIAGONAIS ------------------------
	# Diagonal Canto-Superior-Esquerdo -> Canto-Inferior-Direito
	if grelha["1-1"] != " " and grelha["1-1"] == grelha["2-2"] == grelha["3-3"]:
		return grelha["1-1"]
	# Diagonal Canto-Inferior-Esquerdo -> Canto-Superior-Direito
	if grelha["3-1"] != " " and grelha["3-1"] == grelha["2-2"] == grelha["1-3"]:
		return grelha["3-1"]
	
	return " "  # se chegar até aqui, quer dizer que ainda não há um vencedor
	

# Esta função faz o jogador humano escolher entre usar o símbolo X ou O na partida. Caso o jogador escolher
# um símbolo inválido, ele vai ter que inserir o símbolo novamente. A função só termia quando for escolhido um válido
def obter_simbolo_jogador_humano():
	while True:
		simbolo_escolhido = input("Insira o símbolo que deseja utilizar (X ou O): ").strip()
		
		if simbolo_escolhido != "X" and simbolo_escolhido != "O":
			print("O símbolo escolhido é inválido!")
		else:
			return simbolo_escolhido


# Esta função é responsável por desenhar a grelha de jogo conforme as jogadas feitas (passadas como parâmetro)
def desenha_grelha_de_jogo(grelha):
	print(f"   1   2   3")  # mostrar as coordenadas do eixo x para facilitar a coompreensão do utilizador
	print(f"1  {grelha['1-1']} | {grelha['2-1']} | {grelha['3-1']}")  # mostrar a primeira linha da grelha
	print("  -----------")
	print(f"2  {grelha['1-2']} | {grelha['2-2']} | {grelha['3-2']}")  # mostrar a segunda linha da grelha
	print("  -----------")
	print(f"3  {grelha['1-3']} | {grelha['2-3']} | {grelha['3-3']}")  # mostrar a terceira linha da grelha


# Percorre a grelha e procura todas as coordenadas vazias (onde é possivel algum jogador colocar o seu símbolo)
def obter_jogadas_disponiveis(grelha):
	jogadas_disponiveis = []
	for coordenada in grelha:
		if grelha[coordenada] == " ":
			jogadas_disponiveis.append(coordenada)
	
	return jogadas_disponiveis


# Esta função faz o jogador humano escolher uma jogada entre as jogadas disponíveis atualmente no jogo
def obter_jogada_de_humano(jogadas_disponiveis):
	while True:
		jogada = input("Insira as coordenadas da jogada que desejas efetuar (no formato X-Y): ").strip()
		
		if jogada not in jogadas_disponiveis:
			print("As coordenadas inseridas são inválidas!")
		else:
			return jogada


def jogar_tic_tac_toe(nome_jogador):
	simbolo_humano = obter_simbolo_jogador_humano()  # o jogador humano escolhe o seu símbolo
	
	# Inicialização da Partida -----------------------------------------------------------------------------------------
	# o computador fica com o símbolo que sobrar
	if simbolo_humano == "X":
		simbolo_computador = "O"
	else:
		simbolo_computador = "X"
		
	grelha = obter_grelha_limpa()  # obter uma nova grelha para esta partida
	turno = random.randint(1, 2)  # indica qual jogador vai jogar no turno atual (1: Humano, 2: Computador)
	simbolo_vencedor = " "  # esta variavel vai ter o símbolo do vencedor, por enquanto fica vazia
	# ------------------------------------------------------------------------------------------------------------------
	while simbolo_vencedor == " ":
		# Apagar o conteúdo da consola sempre que um novo turno começar (funciona para Windows e Linux)
		os.system('cls' if os.name == 'nt' else 'clear')
		
		desenha_grelha_de_jogo(grelha)
		
		jogadas_disponiveis = obter_jogadas_disponiveis(grelha)
		if len(jogadas_disponiveis) == 0:  # Se não há mais jogadas disponíveis o jogo acaba com um empate
			print("Empate! Não há mais jogadas disponíveis para esta partida.")
			break
		
		if turno == 1:
			print(f"\nÉ a vez do jogador: {nome_jogador}")
			jogada = obter_jogada_de_humano(jogadas_disponiveis)
			grelha[jogada] = simbolo_humano
			turno = 2  # passar o turno para o computador
		else:
			print(f"\nÉ a vez do jogador: Computador")
			jogada = random.choice(jogadas_disponiveis)  # o computador escolhe uma coordenada aleatória em que jogar
			grelha[jogada] = simbolo_computador
			turno = 1  # passar o turno para o jogador humano
		
		simbolo_vencedor = verifica_vitoria(grelha)
	
	if simbolo_humano == simbolo_vencedor:
		os.system('cls' if os.name == 'nt' else 'clear')  # Apagar o conteúdo da consola (funciona para Windows e Linux)
		desenha_grelha_de_jogo(grelha)  # desenhar a grelha para mostrar como foi a vitória
		print(f"\nO Jogador {nome_jogador} Venceu esta Partida!")
		atualizar_arquivo_tic_tac_toe(nome_jogador)  # se o humano ganhar, adiciona-se uma vitória no seu registro
	elif simbolo_computador == simbolo_vencedor:
		os.system('cls' if os.name == 'nt' else 'clear')  # Apagar o conteúdo da consola (funciona para Windows e Linux)
		desenha_grelha_de_jogo(grelha)  # desenhar a grelha para mostrar como foi a vitória
		print("\nO Computador Venceu esta Partida!")
		
	# Evita que o utilizador volte ao Menu imediatamente
	input("\nPressione qualquer botão para voltar ao Menu")
