# Facade

## Introdução

Este artefato documenta a aplicação do padrão de projeto estrutural Facade no projeto "Revele seu Hobbie". No contexto do projeto, ele foi utilizado para abstrair a complexidade do processo de publicação de um post, que envolve múltiplos serviços como autenticação, salvamento e notificação. O cliente interage apenas com a `PostFacade`, que coordena internamente as ações do subsistema.

## Metodologia

Para o desenvolvimento deste artefato, foram realizadas as seguintes etapas:

1. Estudo do padrão de projeto Factory Method com base em materiais de referência mostrado em sala de aula pela professora [1]
2. Para a modelagem, inicialmente foi feita uma chamada de vídeo com os integrantes responsáveis por este artefato, onde alinhamos as ideias e discutimos o planejamento sobre o que implementariamos dado o contexto do projeto
3. Foram feitos os diagramas em conjunto utilizando o diagrama UML, pela ferramentado do [drawio](https://app.diagrams.net/#G1pcJVnAAakuv8rYM0g8ZvuhaQBeCKSzbq#%7B%22pageId%22%3A%22RUmJMx5qTw6CUYCq72ed%22%7D)
4. Elaboração deste relatório técnico para documentar a aplicação do padrão.

O desenvolvimento aconteceu em uma video chamada no teams.
Disponível [aqui](https://unbbr-my.sharepoint.com/:v:/g/personal/222006169_aluno_unb_br/EZmuOaIGDuhEm-0E5mRHDREBbccaEFDJGd7MzXDVIR_i3w?e=Dgb2XT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).

## Modelagem

O diagrama ilustra como a classe PostFacade serve como um ponto de entrada único, encapsulando a interação com os serviços `ServicoAutenticacao`, `ServicoPostagens` e `ServicoNotificacao`. [2]

<p align="center"> Modelagem do GoF estrutural Facade </p>

![diagrama-facade](/assets/facade.png)

## Implementação

A classe PostFacade oferece um método simples, `publicar_post()`, que esconde a complexidade de coordenar esses serviços para realizar a tarefa.

```python
# Services

class Postagem:
    def __init__(self, autor, imagem_base64, descricao):
        self.autor = autor
        self.imagem_base64 = imagem_base64
        self.descricao = descricao

    def exibir_post(self):
        print("--- Post ---")
        print(f"Autor: {self.autor.getUsername()}")
        print(f"Descrição: {self.descricao}")
        print(f"Imagem: [{self.imagem_base64[:20]}...]") 
        print("------------")

class ServicoAutenticacao:
    def __init__(self):
        self._usuario_logado = None

    def autenticar(self, usuario):
        print(f"[Serviço de Autenticação] Verificando sessão para '{usuario.getUsername()}'...")
        if usuario:
            self._usuario_logado = usuario
            print("[Serviço de Autenticação] Usuário autenticado com sucesso.")
            return True
        print("[Serviço de Autenticação] Falha na autenticação.")
        return False
    
    def get_usuario_logado(self):
        return self._usuario_logado

class ServicoPostagens:
    def salvar_postagem(self, post: Postagem):
        print(f"[Serviço de Postagens] Salvando post de '{post.autor.getUsername()}' no banco de dados...")
        print("[Serviço de Postagens] Post salvo.")

class ServicoNotificacao:
    def notificar_seguidores(self, usuario, post: Postagem):
        print(f"[Serviço de Notificação] Enviando notificações sobre o novo post de '{usuario.getUsername()}'...")
        print("[Serviço de Notificação] Notificações enviadas.")


# postFacade

class PostFacade:
    def __init__(self, servico_auth: ServicoAutenticacao, servico_post: ServicoPostagens, servico_notif: ServicoNotificacao):
        print("\n[Facade] PostFacade inicializada com todos os serviços.")
        self._servico_autenticacao = servico_auth
        self._servico_postagens = servico_post
        self._servico_notificacao = servico_notif

    def publicar_post(self, usuario_tentando_postar, imagem_base64: str, descricao: str):
        print(f"\n[Facade] {usuario_tentando_postar.getUsername()} está tentando publicar um post...")
        
        if not self._servico_autenticacao.autenticar(usuario_tentando_postar):
            print("[Facade] Operação falhou: Usuário não autenticado.")
            return

        usuario_logado = self._servico_autenticacao.get_usuario_logado()
        
        nova_postagem = Postagem(autor=usuario_logado, imagem_base64=imagem_base64, descricao=descricao)
        print("[Facade] Objeto Postagem criado.")

        self._servico_postagens.salvar_postagem(nova_postagem)
        
        self._servico_notificacao.notificar_seguidores(usuario_logado, nova_postagem)
        
        print("[Facade] Processo de publicação concluído com sucesso!")
        nova_postagem.exibir_post()
```

## Interface CLI de teste

```python
from abc import ABC

class Usuario(ABC):
    def __init__(self, username):
        self.username = username
    def getUsername(self):
        return self.username

class UsuarioComum(Usuario):
    pass

if __name__ == "__main__":
    auth_service = ServicoAutenticacao()
    post_service = ServicoPostagens()
    notif_service = ServicoNotificacao()

    post_facade = PostFacade(auth_service, post_service, notif_service)

    usuario_joao = UsuarioComum("joao123")
    dados_do_post = {
        "imagem": "aW1hZ2VtIG11aXRvIGxFga2wgZW0gYmFzZTY0", # Imagem em base64
        "descricao": "Olha que legal meu novo setup de fotografia!"
    }
    
    post_facade.publicar_post(
        usuario_tentando_postar=usuario_joao,
        imagem_base64=dados_do_post["imagem"],
        descricao=dados_do_post["descricao"]
    )
```

## Referências Bibliográficas

[1]: M. Serrane, **Aula - GOFs Estruturai**, Material de aula, Arquitetura e Desenho de Software, Universidade de Brasília, Brasília, DF, 2025. Acessado em: 24 out. 2025. Disponível: [https://aprender3.unb.br/mod/page/view.php?id=1443412](https://aprender3.unb.br/mod/page/view.php?id=1443412)

[2]: "Facade," Refactoring.Guru. Acessado em: 24 out. 2025. [Online]. Disponível: [https://refactoring.guru/design-patterns/facade](https://refactoring.guru/design-patterns/facade)

## Histórico de Versão

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 24/10/2025  | Criação da Modelagem e código do padrão de projeto observer | [Ruan Sobreira Carvalho](https://github.com/Ruan-Carvalho), [Arthur Augusto Rezende da Paixão](https://github.com/arthur-augusto), [Paulo Henrique L. Dantas](https://github.com/Nanashii76) e [Natan Almeida](https://github.com/natanalmeida03) | - | - | - |