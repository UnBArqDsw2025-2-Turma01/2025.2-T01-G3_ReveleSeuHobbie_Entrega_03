from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
class Notificacao(ABC):
	@abstractmethod
	def executar(self):
		pass
class NotificacaoDecorador(Notificacao):
	def __init__(self, notificacao: Optional[Notificacao] = None):
		self._notificacao = notificacao
		self._titulo = ""
		self._descricao = ""
	def escreverTitulo(self, dado: str):
		self._titulo = dado
	def escreverDescricao(self, data: str):
		self._descricao = data
	def envia(self, notificacao: str):
		print(f" Notificação: {notificacao}")
	def executar(self):
		if self._notificacao:
			self._notificacao.executar()
class NotificacaoHobby(NotificacaoDecorador):
	def __init__(self, nome: str, detalhe: str, notificacao: Optional[Notificacao] = None):
		super().__init__(notificacao)
		self.nome = nome
		self.detalhe = detalhe
	def enviar(self):
		msg = f" + [Hobby] Novo hobby cadastrado: {self.nome} - {self.detalhe}"
		self.envia(msg)
	def executar(self):
		super().executar()
		self.enviar()
class NotificacaoNovoUsuario(NotificacaoDecorador):
	def __init__(self, nome: str, detalhe: str, notificacao: Optional[Notificacao] = None):
		super().__init__(notificacao)
		self.nome = nome
		self.detalhe = detalhe
	def enviar(self):
		msg = f" + [Usuário] Bem-vindo(a) {self.nome}! {self.detalhe}"
		self.envia(msg)
	def executar(self):
		super().executar()
		self.enviar()
class NotificacaoEvento(NotificacaoDecorador):
	def __init__(self, nome: str, detalhe: str, notificacao: Optional[Notificacao] = None):
		super().__init__(notificacao)
		self.nome = nome
		self.detalhe = detalhe
	def enviar(self):
		msg = f" + [Evento] {self.nome}: {self.detalhe} - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
		self.envia(msg)
	def executar(self):
		super().executar()
		self.enviar()
class NotificacaoComentario(NotificacaoDecorador):
	def __init__(self, nome: str, detalhe: str, notificacao: Optional[Notificacao] = None):
		super().__init__(notificacao)
		self.nome = nome
		self.detalhe = detalhe
	def enviar(self):
		msg = f" + [Comentário] {self.nome}: {self.detalhe}"
		self.envia(msg)
	def executar(self):
		super().executar()
		self.enviar()
if __name__ == "__main__":
	# Cria notificações independentes
	n1 = NotificacaoHobby("Fotografia", "Novo hobby adicionado ao sistema.")
	n2 = NotificacaoNovoUsuario("Ana", "Sua conta foi criada com sucesso.")
	n3 = NotificacaoEvento("Hackathon", "Evento de programação neste fim de semana.")
	n4 = NotificacaoComentario("Carlos", "Comentou na sua publicação.")
	print("\n--- Notificações Individuais ---")
	n1.executar()
	n2.executar()
	n3.executar()
	n4.executar()
	
	print("\n--- Notificações Encadeadas ---")
	noti_composta = NotificacaoComentario("Maria", "Respondeu seu comentário.",
					   NotificacaoEvento("Workshop Python", "Hoje às 19h.",
					   NotificacaoNovoUsuario("João", "Acabou de se registrar.")))
	noti_composta.executar()