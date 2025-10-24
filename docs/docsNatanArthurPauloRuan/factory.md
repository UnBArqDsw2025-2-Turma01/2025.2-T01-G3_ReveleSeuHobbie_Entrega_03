# Factory

## Introdução

Este artefato documenta a aplicação do padrão de projeto criacional Factory Method no projeto "Revele seu Hobbie". O Factory Method é um padrão que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. No contexto do projeto, ele foi utilizado para gerenciar a criação dos diferentes tipos de usuários (`UsuarioComum` e `UsuarioAdmin`), desacoplando o código cliente das classes concretas de usuários.

## Metodologia

Para o desenvolvimento deste artefato, foram realizadas as seguintes etapas:

1. Estudo do padrão de projeto Factory Method com base em materiais de referência mostrado em sala de aula pela professora [1]
2. Para a modelagem, inicialmente foi feita uma chamada de vídeo com os integrantes responsáveis por este artefato, onde alinhamos as ideias e discutimos o planejamento sobre o que implementariamos dado o contexto do projeto
3. Foram feitos os diagramas em conjunto utilizando o diagrama UML, pela ferramentado do [drawio](https://app.diagrams.net/#G1pcJVnAAakuv8rYM0g8ZvuhaQBeCKSzbq#%7B%22pageId%22%3A%22RUmJMx5qTw6CUYCq72ed%22%7D)
4. Elaboração deste relatório técnico para documentar a aplicação do padrão.

O desenvolvimento aconteceu em uma video chamada no teams.
Disponível [aqui](https://unbbr-my.sharepoint.com/:v:/g/personal/222006169_aluno_unb_br/EZmuOaIGDuhEm-0E5mRHDREBbccaEFDJGd7MzXDVIR_i3w?e=Dgb2XT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).

## Modelagem 

A seguir, é apresentada a modelagem UML que descreve a estrutura do padrão Factory Method aplicada à criação de usuários no sistema. O diagrama ilustra a interface `FactoryUser`, as fábricas concretas (`FactoryAdmin` e `FactoryComum`) e os produtos que elas criam (`UsuarioAdmin` e `UsuarioComum`). [2] [3]

<p align="center"> Modelagem do GoF criacional Factory Method </p>

![diagrama-factory](/assets/factory.png)

## Implementação

A classe abstrata `Usuario` atua como o "Produto", enquanto `UsuarioComum` e `UsuarioAdmin` são os produtos concretos. A interface `FactoryUser` define o método de fabricação, que é implementado pelas classes `FactoryComum` e `FactoryAdmin`.

```python
from abc import ABC, abstractmethod

# Interface/Classe Abstrata do Produto
class Usuario(ABC):
    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha
        self.role = "indefinido"
    
    def getUsername(self):
        return self.username

    def getRole(self):
        return self.role

    def __str__(self):
        return f"Usuário: {self.username}, Role: {self.role}"

# Produto Concreto 1
class UsuarioComum(Usuario):
    def __init__(self, username, email, senha):
        super().__init__(username, email, senha)
        self.role = "comum"

    def entrarComunidade(self, comunidadeName):
        print(f"{self.getUsername()} entrou na comunidade {comunidadeName}")
    
    def publicarPost(self, postName):
        print(f"{self.getUsername()} publicou: '{postName}'")

# Produto Concreto 2
class UsuarioAdmin(Usuario):
    def __init__(self, username, email, senha):
        super().__init__(username, email, senha)
        self.role = "admin"
    
    def gerenciarComunidade(self, comunidade):
        print(f"Admin fez alguma alteração da comunidade: {comunidade}")

    def gerenciarUsuario(self):
        print(f"Lista de todos os usuários disponíveis: ...")

# Interface do Criador (Factory)
class FactoryUser(ABC):
    @abstractmethod
    def novoUsuario(self, username, email, senha) -> Usuario:
        pass

# Criador Concreto 1
class FactoryComum(FactoryUser):
    def novoUsuario(self, username, email, senha) -> UsuarioComum:
        print("FactoryComum: Criando um novo usuário comum")
        return UsuarioComum(username, email, senha)

# Criador Concreto 2
class FactoryAdmin(FactoryUser):
    def novoUsuario(self, username, email, senha) -> UsuarioAdmin:
        print("FactoryAdmin: Criando um novo usuário administrador")
        return UsuarioAdmin(username, email, senha)
```

## Interface CLI de teste

```python
# Classes de suporte para teste

class Post:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

class Comunidade:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []
        self.posts = []
    
    def adicionar_membro(self, usuario: Usuario):
        self.membros.append(usuario)
        
    def adicionar_post(self, post: Post):
        self.posts.append(post)

# Aplicação

class AppReveleSeuHobbie:
    def __init__(self):
        self.usuarios_cadastrados = {} 
        self.comunidades = {}           
        self.usuario_logado = None
    
    def criar_usuario_pela_role(self, role, username, email, senha):
        factories = {"comum": FactoryComum(), "admin": FactoryAdmin()}
        if role not in factories:
            raise ValueError("Role de usuário inválida!")
        factory = factories[role]
        return factory.novoUsuario(username, email, senha)

    def registrar_usuario(self):
        print("\n--- Registro de Novo Usuário ---")
        username = input("Nome de usuário: ")
        if username in self.usuarios_cadastrados:
            print(">> ERRO: Nome de usuário já existe.")
            return
        
        email = input("Email: ")
        senha = getpass.getpass("Senha: ") # getpass esconde a senha
        role = input("Qual o tipo de usuário? (comum/admin): ").lower()

        try:
            novo_usuario = self.criar_usuario_pela_role(role, username, email, senha)
            self.usuarios_cadastrados[username] = novo_usuario
            print(f"\n>> Usuário '{username}' registrado com sucesso!")
        except ValueError as e:
            print(f">> ERRO: {e}")

    def fazer_login(self):
        if self.usuario_logado:
            print("\n>> Você já está logado. Faça logout primeiro.")
            return
            
        print("\n--- Login ---")
        username = input("Nome de usuário: ")
        senha = getpass.getpass("Senha: ")

        usuario = self.usuarios_cadastrados.get(username)
        if usuario and usuario.senha == senha:
            self.usuario_logado = usuario
            print(f"\n>> Login bem-sucedido! Bem-vindo(a), {username}!")
        else:
            print("\n>> ERRO: Nome de usuário ou senha incorretos.")

    def fazer_logout(self):
        if self.usuario_logado:
            print(f"\n>> {self.usuario_logado.getUsername()} deslogado com sucesso.")
            self.usuario_logado = None
        else:
            print("\n>> Ninguém está logado.")

    def entrar_em_comunidade(self):
        if not isinstance(self.usuario_logado, UsuarioComum):
            print("\n>> Ação disponível apenas para usuários do tipo 'comum'.")
            return
            
        nome_comunidade = input("Qual o nome da comunidade que deseja entrar? ")
        if nome_comunidade not in self.comunidades:
            self.comunidades[nome_comunidade] = Comunidade(nome_comunidade)
        
        comunidade = self.comunidades[nome_comunidade]
        self.usuario_logado.entrarComunidade(comunidade)
        
    def publicar_post_em_comunidade(self):
        if not isinstance(self.usuario_logado, UsuarioComum):
            print("\n>> Ação disponível apenas para usuários do tipo 'comum'.")
            return

        nome_comunidade = input("Em qual comunidade você quer postar? ")
        if nome_comunidade not in self.comunidades:
            print(f"\n>> ERRO: Comunidade '{nome_comunidade}' não existe.")
            return
            
        comunidade = self.comunidades[nome_comunidade]
        texto = input("Digite seu post: ")
        self.usuario_logado.publicarPost(comunidade, texto)

    def menu_admin(self):
        if not isinstance(self.usuario_logado, UsuarioAdmin):
            print("\n>> Ação disponível apenas para administradores.")
            return
        
        print("\n--- Ações de Administrador ---")
        self.usuario_logado.gerenciarUsuarios(self.usuarios_cadastrados)


    def run(self):
        while True:
            print("\n===== Revele Seu Hobbie =====")
            if self.usuario_logado:
                print(f"Logado como: {self.usuario_logado.getUsername()} ({self.usuario_logado.getRole()})")
            
            print("1. Registrar")
            print("2. Login")
            print("3. Logout")

            if isinstance(self.usuario_logado, UsuarioComum):
                print("4. Entrar em uma Comunidade")
                print("5. Publicar Post em Comunidade")
            
            if isinstance(self.usuario_logado, UsuarioAdmin):
                 print("6. Gerenciar Usuários (Admin)")

            print("0. Sair")
            
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.registrar_usuario()
            elif escolha == '2':
                self.fazer_login()
            elif escolha == '3':
                self.fazer_logout()
            elif escolha == '4' and isinstance(self.usuario_logado, UsuarioComum):
                self.entrar_em_comunidade()
            elif escolha == '5' and isinstance(self.usuario_logado, UsuarioComum):
                self.publicar_post_em_comunidade()
            elif escolha == '6' and isinstance(self.usuario_logado, UsuarioAdmin):
                self.menu_admin()
            elif escolha == '0':
                print("Saindo... Até mais!")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = AppReveleSeuHobbie()
    app.run()
```

## Referências Bibliográficas

[1]: SERRANE, Milene. **Aula - GOFs Comportamentais**. Material de aula da disciplina Arquitetura e Desenho de Software. Universidade de Brasília (UnB), 2º/2025. Disponível em: [https://aprender3.unb.br/pluginfile.php/3178396/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178396/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf). Acesso em: 23 out. 2025

[2]:  GAMMA, Erich et al. Padrões de Projeto: Soluções Reutilizáveis de Software Orientado a Objetos. Bookman, 2000.

[3]: FACTORY METHOD. In: Refactoring Guru. Disponível em: [https://refactoring.guru/design-patterns/factory-method](https://refactoring.guru/design-patterns/factory-method). Acesso em: 23 de outubro de 2025.

## Histórico de Versão

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 24/10/2025  | Criação da Modelagem e código do padrão de projeto observer | [Ruan Sobreira Carvalho](https://github.com/Ruan-Carvalho), [Arthur Augusto Rezende da Paixão](https://github.com/arthur-augusto), [Paulo Henrique L. Dantas](https://github.com/Nanashii76) e [Natan Almeida](https://github.com/natanalmeida03) | - | - | - |