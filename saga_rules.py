import google.generativeai as genai
import random
import os

# Criar uma variável de ambiente GEMINI_API_KEY com a API_KEY
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

safety_settings={
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE"
    }

model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)
#model = genai.GenerativeModel('gemini-1.5-pro')
#model = genai.GenerativeModel('gemini-1.5-pro-latest')

global protagonista
global profissao
global tipo_de_desafio
global tipo_de_mentor
global tipo_de_solucao
global tipo_de_reinicio

global fase
fase = 1

global texto_a_submeter

protagonista = ''
profissao = ''
tipo_de_desafio = ''
tipo_de_mentor = ''
tipo_de_solucao = ''
tipo_de_reinicio = ''

tipos_de_desafios = ["Colisão de meteoro com a Terra", "Invasão alienígena", "Desastre climático", "Guerra nuclear"]
tipos_de_mentores = ["Hacker sem-teto e com problemas psiquiátricos que tinha uma teoria da simulação da realidade", "Terapeuta quântico que fornecia uma solução mental", "Criança com dons sobrenaturais que desafiava a realidade", "Bilionário arrependido que empreendeu numa solução inusitada"]
tipos_de_solucoes = ["Alterar a simulação da realidade", "Usar uma máquina do tempo e voltar ao passado", "Fugir da Terra numa espaçonave"]
tipos_de_reinicios = ["Acordou numa nova vida", "Retornou ao início de sua carreira", "Renasceu num outro universo"]

global escolhas_fase1
global escolhas_fase2
global escolhas
global escolha

escolhas_fase1=["Aceitar o novo plano de seguro e tentar recuperar o atraso no trabalho",
"Procurar um advogado e lutar contra a seguradora, mesmo que isso signifique mais problemas no trabalho"]

escolhas_fase2=["A pressão no trabalho se intensificou, levando a mais advertências e insatisfação.", 
"O processo se arrastou, causando estresse e distrações que afetaram seu desempenho. Teve que aceitar um cargo inferior, lidando diretamente com clientes insatisfeitos."]


def sortear(tipo):
	sorteado = ""
	if tipo == "protagonista":
		response = model.generate_content("Escolha um nome de protagonista para uma história de ficção. Retorne um único nome.")
		sorteado = response.text
	elif tipo == "profissao":
		response = model.generate_content("Escolha uma profissão para a protagonista de nome "+protagonista+". Retorne uma única profissão.")
		sorteado = response.text
	elif tipo == "desafio":
		sorteado = random.choice(tipos_de_desafios)
	elif tipo == "mentor":
		sorteado = random.choice(tipos_de_mentores)
	elif tipo == "solucao":
		sorteado = random.choice(tipos_de_solucoes)
	return sorteado

def inicializacao_do_mundo():
	global protagonista
	global profissao
	global tipo_de_desafio
	global tipo_de_mentor
	global tipo_de_solucao
	global tipo_de_reinicio	

	if protagonista == '':
		protagonista = "Apolinário"
		profissao = "trabalhador de escritório"
		tipo_de_desafio = tipos_de_desafios[0]
		tipo_de_mentor = tipos_de_mentores[0]
		tipo_de_solucao = tipos_de_solucoes[0]
		tipo_de_reinicio = tipos_de_reinicios[0]
	else:
		protagonista = sortear('protagonista')
		profissao = sortear('profissao')
		tipo_de_desafio = sortear('desafio')
		tipo_de_mentor = sortear('mentor')
		tipo_de_solucao = sortear('solucao')
		tipo_de_reinicio = tipos_de_reinicios[tipos_de_solucoes.index(tipo_de_solucao)]
	titulo_do_jogo = "Saga de "+protagonista

inicializacao_do_mundo()

def get_apresentacao():
	saudacao = "Bem vindo à Saga de "+protagonista+"\n"
	apresentacao = protagonista+" vivia numa rotina monótona, como "+profissao+". Após uma colisão com seu carro, ao se desviar de um bêbado, o seguro não quis pagar as despesas por não cobrir problemas de embriaguez. A partir daí sua vida começou a desmoronar. Atrasos no trabalho, advertências e uma crescente sensação de injustiça começaram a corroer sua fé na ordem das coisas."
	return saudacao, apresentacao

def formatar_escolha(texto_escolha, escolhas_padroes):
	if texto_escolha.strip() == "":
		exit()
	try:
		a_escolha = escolhas_padroes[int(texto_escolha.strip())-1]
	except:
		a_escolha = texto_escolha

	return a_escolha


def run_saga(input_text):
	global fase
	global texto_a_submeter
	global escolha
	global escolhas
	output_text = ""

	if fase == 1:
		escolhas = escolhas_fase1

	if fase == 1:

		# FASE 1 - O mundo comum
		saudacao, apresentacao = get_apresentacao()
		output_text += saudacao
		output_text += apresentacao+"\n"
		output_text += "\nQual deve ser a escolha de "+protagonista+"?\n"
		for e in range(len(escolhas)):
			output_text += "("+str(e+1)+") "+escolhas[e]+"\n"

	elif fase == 2:

		escolha = formatar_escolha(input_text, escolhas)

		if escolha in escolhas:
			escolha2 = escolhas_fase2[escolhas.index(escolha)]
		else:
			escolha2 = random.choice(escolhas_fase2)
		
		texto_a_submeter = "\n"+protagonista+" decidiu "+escolha+". O que pode acontecer depois disso? Selecione uma única possibilidade e escreva um parágrafo em forma narrativa sobre o que houve com "+protagonista+", tendo como resultado final que "+escolha2
		response = model.generate_content(texto_a_submeter)
		output_text += response.text
		texto_a_submeter = response.text+" Com o rebaixamento para uma função que não agradou, como a de atendimento direto ao público. Quais possibilidades existiriam para "+protagonista+"? Apresente as 3 melhores possibilidades (sem marcadores) como uma lista de strings em python, no estilo ['string',...,'string']"

		# FASE 2 - O chamado à aventura
		response = model.generate_content(texto_a_submeter)
		escolhas=eval(response.text.replace("```python","").replace("```",""))
		output_text += "\nQual deve ser a escolha?\n"
		for e in range(len(escolhas)):
			output_text += "("+str(e+1)+") "+escolhas[e]+"\n"

	elif fase == 3:

		escolha = formatar_escolha(input_text, escolhas)
		texto = "Ao "+escolha+", ocorreu um ponto de ruptura. A pressão e o estresse acabaram cobrando seu preço, todos os erros levaram à demissão. Agora, é viver sem emprego e sem teto (pois não conseguiu pagar seu aluguel), vivendo nas ruas e questionando a ordem que sempre acreditou existir."
		texto_a_submeter = "Corrija o seguinte texto: "+texto+" e retorne apenas uma única opção como um parágrafo narrativo"
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"

		texto_a_submeter = texto+" Apresente as 3 melhores possibilidades (sem marcadores), como uma lista de strings em python, no estilo ['string',...,'string']"
		response = model.generate_content(texto_a_submeter)
		texto_a_submeter = response.text

		escolhas=eval(texto_a_submeter) #.replace("```python","").replace("```",""))
		output_text += "\nQual deve ser a escolha?\n"
		for e in range(len(escolhas)):
			output_text += "("+str(e+1)+") "+escolhas[e]+"\n"
		
	elif fase == 4:

		escolha = formatar_escolha(input_text, escolhas)
		texto = "Enquanto "+protagonista+" escolhia "+escolha+", descobriu uma notícia alarmante vinda de uma TV em uma loja de eletrônicos: "+tipo_de_desafio+". Isso lhe desencadeou grande desespero, ao mesmo tempo que surgiu uma esperança ao lembrar de "+tipo_de_mentor
		texto_a_submeter = "Corrija o seguinte texto: "+texto+" e retorne apenas uma única opção como um parágrafo narrativo"
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"

		texto = protagonista+" imaginou então que com a ajuda do "+tipo_de_mentor+" haveria uma solução e saiu em sua procura"		
		texto_a_submeter = "Corrija o seguinte texto: "+texto+" e retorne apenas uma única opção como uma frase narrativa"
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"

		texto_a_submeter = protagonista+" encontrou "+tipo_de_mentor+", e perguntou qual o plano para vencer "+tipo_de_desafio+". Descreva a conversa em um parágrafo"
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"

		texto = "Num momento de dúvida, "+protagonista+" teme em seguir o plano de "+tipo_de_mentor
		texto_a_submeter = "Esboçar um parágrafo narrativo para: "+texto		
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"

		texto_a_submeter = "Apresente duas possibilidades (sem marcadores) para dizer SIM ou NÃO ao plano de "+tipo_de_mentor+", como uma lista de strings sem marcadores, no estilo ['string',...,'string']"
		response = model.generate_content(texto_a_submeter)
		escolhas=eval(response.text) #.replace("```python","").replace("```",""))

		output_text += "\nQual deve ser a escolha?\n"
		for e in range(len(escolhas)):
			output_text += "("+str(e+1)+") "+escolhas[e]+"\n"

	elif fase == 5:

		# FASE 5
		escolha = formatar_escolha(input_text, escolhas)

		texto_a_submeter = "Como "+protagonista+" resolveu "+escolha+", o plano de "+tipo_de_mentor+" para evitar "+tipo_de_desafio+" e suceder "+tipo_de_reinicio+" terá um desfecho. Elabore o final da história."
		response = model.generate_content(texto_a_submeter)
		texto = response.text.replace("\n"," ")
		output_text += "\n"+texto+"\n"
		output_text +="\n\n--- FIM ---\n\n\n"

		inicializacao_do_mundo()
		fase = 0

	fase = fase + 1
	return output_text
