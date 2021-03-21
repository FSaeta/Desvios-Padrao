R = '\033[31m' # vermelho
G = '\033[01;32m' # verde
Y = '\033[01;33m' # amarelo
C = '\033[36m' # ciano
W = '\033[0m'  # branco

from os import system, name

def limpar_tela():
	system('cls' if name == 'nt' else 'clear')

class Menu:
	def __init__(self, nome, id, msg, op_dict):
		self.nome = nome
		self.msg = msg
		self.opcoes = op_dict
		self.funcoes_params = self.get_funcoes_params()

	def get_funcoes_params(self):
		funcoes_parametros = {}
		for opcao in self.opcoes.keys():
			funcs_params = []
			for funcao_params in self.opcoes[opcao]:
				funcs_params.append(funcao_params)

			funcoes_parametros.update({opcao:funcs_params})
		return funcoes_parametros

	def exec_funcs(self, opcao):
		ret = {}
		for funcao, params in self.funcoes_params[opcao]:
			if len(params) != 0:
				ret_f = funcao(*params)
			else:
				ret_f = funcao()
			ret.update({funcao.__name__: ret_f})
		return ret
		
	def valida_opcao(self, opcao):
		op_permitidas = list(self.opcoes.keys())
		if opcao not in op_permitidas:
			raise ValueError
