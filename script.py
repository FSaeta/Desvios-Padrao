import menu
from menu import R,G,Y,C,W
import sys

msg_menu_inicial = f"""{G}BEM VINDO AO PROGRAMA DE DESVIO PADRÃO{W}

{Y}[1]{W} Dados não agrupados
{Y}[2]{W} Dados agrupados {Y}sem{W} classe
{Y}[3]{W} Dados agrupados {Y}com{W} classe

{Y}[0]{W} Sair
"""
msg_simples = f"""{G}DADOS NÃO AGRUPADOS{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""
msg_grup = f"""{G}DADOS AGRUPADOS SEM CLASSE{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""
msg_grup_classe = f"""{G}DADOS AGRUPADOS POR CLASSES{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""

#--------------------------------
def soma(*args):
	soma = 0
	for arg in args[0]:
		soma += arg
	return soma

def soma2(*args):
	new_x = []
	for x in args[0]:
		x_2 = x**2
		new_x.append(x_2)
	return soma(new_x)

def calc_xini(indx, nums):
	xini = []
	cont = 0
	for n in nums:
		xini.append(indx[cont]*n)
		cont += 1
	print(f"XINI = {xini}")
	return xini

# Funções de computar dados
# -------------------------
def computar_dados(numeros):
	N = len(numeros)
	soma_xi = round(soma(numeros),2)
	soma_xi2 = round(soma2(numeros),2)
	x_ = round(soma_xi / N, 2)
	x_2 = round(x_**2, 2)
	s2 = (soma_xi2 - N * x_2) / (N-1)
	values = {'numeros': numeros, 'N': N, 'soma_xi': soma_xi, 'soma_xi2': soma_xi2, 'x_': x_, 'x_2': x_2, 's2': s2}
	return values

def computar_dados_grup(numeros):
	start = int(input('start'))
	end = int(input('end'))+1
	indexes = range(start, end)
	print(indexes)
	N = len(numeros)
	soma_ni = round(soma(numeros),2)
	xini = calc_xini(indexes, numeros)
	soma_xini = round(soma(xini),2)
	xini2 = calc_xini(indexes, xini)
	soma_xini2 = round(soma(xini2),2)
	x_ = round(soma_xini / soma_ni, 2)
	x_2 = round(x_**2, 2)
	s2 = (soma_xini2 - soma_ni * x_2) / (soma_ni-1)
	values = {'indexes': indexes,'numeros': numeros, 'N': soma_ni, 'xini': xini,'soma_xini': soma_xini, 'xini2': xini2, 'soma_xini2': soma_xini2, 'x_': x_, 'x_2': x_2, 's2': s2}
	return values

def computar_dados_grup_classe(numeros):
	classes = pedir_classes()
	N = len(numeros)
	soma_ni = round(soma(numeros),2)
	xi = calc_pontos_medios(classes)
	xi2 = [x**2 for x in xi]
	xini = calc_xini(xi, numeros)
	xi2ni = calc_xini(xi2, numeros)
	soma_xini = round(soma(xini),2)
	soma_xini2 = round(soma(xi2ni),2)
	x_ = round(soma_xini / soma_ni, 2)
	x_2 = round(x_**2, 2)
	s2 = (soma_xini2 - soma_ni * x_2) / (soma_ni-1)
	values = {'classes': classes,'numeros': numeros,'xi':xi,'xi2':xi2,'xini':xini,'xi2ni': xi2ni, 
			  'soma_ni': soma_ni, 'soma_xini': soma_xini, 'soma_xini2': soma_xini2, 
			  'x_': x_, 'x_2': x_2, 's2': s2}
	return values

# Funções de montagem dos gráficos
# --------------------------------
def montar_graf_simples(values):
	header = "      xi    |    xi²   \n"
	escopo = header
	for n in values['numeros']:
		linha = f"      {n}".ljust(12) + f"|    {n**2}".ljust(10) + "\n"
		escopo += linha
	linha_soma = f"\nsoma= {values['soma_xi']}".ljust(13)+ f"|    {values['soma_xi2']}"
	escopo += linha_soma
	escopo += "\n___________________________\n\n"
	return escopo

def montar_graf_grup(values):
	header = "      xi   |   ni   |   xi.ni  |   xi².ni   \n"
	escopo = header
	indx = 0
	for xi in values['indexes']:
		linha = f"      {xi}".ljust(11) + \
				f"|   {values['numeros'][indx]}".ljust(9) + \
				f"|    {values['xini'][indx]}".ljust(11) + \
				f"|    {values['xini2'][indx]}".ljust(10) + \
				"\n"
		escopo += linha
		indx += 1
	linha_soma = f"\nsoma= ".ljust(12)+ \
				 f"|    {values['N']}".ljust(9) + \
				 f"|    {values['soma_xini']}".ljust(11) + \
				 f"|    {values['soma_xini2']}".ljust(10)
	escopo += linha_soma
	escopo += "\n________________________________\n\n"
	return escopo

def montar_graf_grup_classe(values):
	header = "    Classes   |   ni   |   xi   |   xi²   |   xi.ni  |   xi².ni   \n"
	cels_len = [len(cel) for cel in header.split('|')]
	import pdb; pdb.set_trace()
	escopo = header
	indx = 0
	for classe in values['classes']:
		linha = f"     {classe[0]}|-{classe[1]}".ljust(cels_len[0]) + \
				f"|   {values['numeros'][indx]}".ljust(cels_len[1]) + \
				f"|   {values['xi'][indx]}".ljust(cels_len[2]) + \
				f"|    {values['xi2'][indx]}".ljust(cels_len[3]) + \
				f"|    {values['xini'][indx]}".ljust(cels_len[4]) + \
				f"|    {values['xi2ni'][indx]}".ljust(cels_len[5]) + \
				"\n"
		escopo += linha
		indx += 1
	linha_soma = f"\nsoma= ".ljust(15)+ \
				 f"|    {values['soma_ni']}".ljust(9) + \
				 f"|".ljust(9) + \
				 f"|".ljust(9) + \
				 f"|    {values['soma_xini']}".ljust(11) + \
				 f"|    {values['soma_xini2']}".ljust(10)
	escopo += linha_soma
	escopo += "\n________________________________\n\n"
	return escopo

# Funções Agrupadas com Classe
# ----------------------------
def pedir_classes():
	pede_cl = True
	classes = []
	while pede_cl:
		try:
			classe = input("Classe: ")
			classe = classe.split(',')
			classes.append(classe)
		except KeyboardInterrupt:
			pede_cl = False
	return classes

def calc_pontos_medios(classes):
	pontos_medios = []
	for classe in classes:
		pm = (int(classe[0])+int(classe[1]))/2
		pontos_medios.append(pm)
	return pontos_medios

# --------- Main Functions ----------

def mudar_id(novo_id):
	global id_menu
	id_menu = novo_id
	return id_menu

def muda_pede():
	global pede
	pede = not pede

def pede_numeros():
	numeros = []
	pede = True
	while pede:
		try:
			numero = float(input("numero: "))
			numeros.append(numero)
		except KeyboardInterrupt:
			pede = False
			return numeros

# -----------------------------------

def run_simples_amostra():

	numeros = pede_numeros()
	values = computar_dados(numeros)
	
	print(values)
	print(montar_graf_simples(values))

	print(f"Soma xi = {values['soma_xi']}")
	print(f"N = {values['N']}")
	print(f"x_2 = ({values['soma_xi']} / {values['N']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2']} - {values['N']} * {values['x_2']}) / {values['N']-1}  = {values['s2']}")


def run_grupo_amostra():

	numeros = pede_numeros()
	values = computar_dados_grup(numeros)

	print(values)
	print(montar_graf_grup(values))

	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xini2 = {values['soma_xini2']}")
	print(f"N = {values['N']}")
	print(f"x_2 = ({values['soma_xini']} / {values['N']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xini2']} - {values['N']} * {values['x_2']}) / {values['N']-1}  = {values['s2']}")


def run_grupo_class_amostra():

	numeros = pede_numeros()		
	values = computar_dados_grup_classe(numeros)

	print(values)
	print(montar_graf_grup_classe(values))

	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xini2 = {values['soma_xini2']}")
	print(f"N = {values['soma_ni']}")
	print(f"x_2 = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xini2']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")

menu_inicial = menu.Menu(nome="Inicial", id=0, msg=msg_menu_inicial, 
						 op_dict={0:[(sys.exit,[])], 
						 		  1:[(mudar_id,[1])],
						 		  2:[(mudar_id,[2])],
						 		  3:[(mudar_id,[3])]
						 		  })
menu_simples = menu.Menu(nome="Simples", id=1, msg=msg_simples, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_simples_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
menu_grup = menu.Menu(nome="Grupo sem Classe", id=2, msg=msg_grup, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_grupo_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
menu_grup_classe = menu.Menu(nome="Grupo por Classe", id=3, msg=msg_grup_classe, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_grupo_class_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
if __name__ == '__main__':
	running = True
	menus = {0:menu_inicial, 1:menu_simples, 2:menu_grup, 3:menu_grup_classe}
	id_menu = 0

	while running:
		try:
			menu_ativo = menus[id_menu]
			print(menu_ativo.msg)
			op = int(input("op :"))
			menu_ativo.valida_opcao(op)
			menu_ativo.exec_funcs(op)
		except SystemExit:
			running = False
		except:
			print(f"{R}ops... algo deu ruim{W}")
