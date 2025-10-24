from abc import ABC, abstractmethod
 
class Imagem:
    def __init__(self, arquivo=None):
        self.arquivo = arquivo
 
class Conteudo:
    def __init__(self, texto=None):
        self.texto = texto
 
class Comentario:
    def __init__(self, texto=None, autor=None):
        self.texto = texto
        self.autor = autor
 
class Publicacao:
    def __init__(self, imagem=None, texto=None, autor=None):
        self.imagem = imagem
        self.texto = texto
        self.autor = autor
 
class Construtor(ABC):
    @abstractmethod
    def reiniciar(self): pass
    @abstractmethod
    def criarTexto(self, texto): pass
    @abstractmethod
    def criarAutor(self, autor): pass
    @abstractmethod
    def criarImagem(self, arquivo): pass
    @abstractmethod
    def getResultado(self): pass
 
class ConstrutorPublicacao(Construtor):
    def reiniciar(self):
        self.publicacao = Publicacao()
        print("[ConstrutorPublicacao] Reiniciando publicação.")
 
    def criarTexto(self, texto):
        print(f"[ConstrutorPublicacao] Adicionando texto: {texto}")
        self.publicacao.texto = texto
 
    def criarAutor(self, autor):
        print(f"[ConstrutorPublicacao] Definindo autor: {autor}")
        self.publicacao.autor = autor
 
    def criarImagem(self, arquivo):
        print(f"[ConstrutorPublicacao] Inserindo imagem: {arquivo}")
        self.publicacao.imagem = Imagem(arquivo=arquivo)
 
    def getResultado(self):
        return self.publicacao
 
class Diretor:
    def criar_publicacao(self, builder, texto, autor, arquivo_imagem):
        builder.reiniciar()
        builder.criarTexto(texto)
        builder.criarAutor(autor)
        builder.criarImagem(arquivo_imagem)
        return builder.getResultado()
 
builder = ConstrutorPublicacao()
diretor = Diretor()
 
publicacao = diretor.criar_publicacao(
    builder,
    texto="Gosto de jogar Bloons TD6",
    autor="User1",
    arquivo_imagem="foto1.jpg"
)
 
print("Autor:", publicacao.autor)
print("Texto:", publicacao.texto)
print("Imagem:", publicacao.imagem.arquivo)
 