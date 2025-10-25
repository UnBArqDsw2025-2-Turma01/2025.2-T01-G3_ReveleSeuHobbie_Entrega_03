from abc import ABC, abstractmethod
class Vincular(ABC):
	
	def executar(self, id_usuario, id_alvo):
		if not self.validar(id_usuario, id_alvo):
			print("Ação inválida!")
			return False
		
		self.relacionar(id_usuario, id_alvo)
		
		self.notificar(id_usuario, id_alvo)
		
		return True
	
	@abstractmethod
	def validar(self, id_usuario, id_alvo):
		pass
	
	@abstractmethod
	def relacionar(self, id_usuario, id_alvo):
		pass
	
	def notificar(self, id_usuario, id_alvo):
		print(f"Usuário {id_usuario} realizou ação com {id_alvo}")
		
class Seguir(Vincular):
	
	def validar(self, id_usuario, id_seguido):
		return id_usuario != id_seguido 
	
	def relacionar(self, id_usuario, id_seguido):
		print(f"Usuário {id_usuario} agora segue {id_seguido}")
class Inscrever(Vincular):
	
	def validar(self, id_usuario, id_comunidade):
		return id_usuario != id_comunidade  
	
	def relacionar(self, id_usuario, id_comunidade):
		print(f"Usuário {id_usuario} se inscreveu na comunidade {id_comunidade}")
seguir = Seguir()
seguir.executar("user1", "user2")
inscrever = Inscrever()
inscrever.executar("user3", "comunidade")
seguir.executar("clarissa", "yzabella")