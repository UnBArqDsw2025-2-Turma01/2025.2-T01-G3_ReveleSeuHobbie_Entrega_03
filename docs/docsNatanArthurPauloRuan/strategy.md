# Observer 

## Introdução

Este artefato documenta a aplicação do padrão de projeto comportamental Strategy no projeto Revele Seu Hobbie. O Strategy é um padrão de design comportamental que permite definir uma família de algoritmos, encapsulá-los em classes separadas e torná-los intercambiáveis em tempo de execução. No contexto da aplicação, o padrão foi utilizado para gerenciar diferentes formas de autenticação de usuários, permitindo que o sistema alterne entre métodos como login por e-mail e senha, autenticação via Google ou via Microsoft, sem modificar a lógica principal do serviço de autenticação.

## Metodologia

Para o desenvolvimento do trabalho, foram realizadas as seguintes etapas:

1. Estudo do padrão de projeto Factory Method com base em materiais de referência mostrado em sala de aula pela professora [1]
2. Para a modelagem, inicialmente foi feita uma chamada de vídeo com os integrantes responsáveis por este artefato, onde alinhamos as ideias e discutimos o planejamento sobre o que implementariamos dado o contexto do projeto
3. Foram feitos os diagramas em conjunto utilizando o diagrama UML, pela ferramenta [drawio](https://app.diagrams.net/#G1pcJVnAAakuv8rYM0g8ZvuhaQBeCKSzbq#%7B%22pageId%22%3A%22RUmJMx5qTw6CUYCq72ed%22%7D)
4. Elaboração deste relatório técnico para documentar a aplicação do padrão.

O desenvolvimento aconteceu em uma video chamada no teams.
Disponível [aqui](https://unbbr-my.sharepoint.com/:v:/g/personal/222006169_aluno_unb_br/EZmuOaIGDuhEm-0E5mRHDREBbccaEFDJGd7MzXDVIR_i3w?e=Dgb2XT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).

## Modelagem

A seguir, é possível visualizar a modelagem gerada:

<p align="center">Modelagem do Gof comportamental Strategy</p>

![strategy modelagem](/assets/strategy.png)

## Implementação

```python
from abc import ABC, abstractmethod

# Interface da Estratégia 
class Autenticacao(ABC):
    @abstractmethod
    def autenticar(self, **kwargs) -> bool:
        """Define o contrato de autenticação."""
        pass

# Estratégias Concretas
class LoginEmailSenha(Autenticacao):
    def autenticar(self, **kwargs) -> bool:
        email = kwargs.get("email")
        senha = kwargs.get("senha")

        print(f"[LoginEmailSenha] Tentando autenticar {email} com senha...")
        # Simula uma verificação interna (sem banco de dados)
        if email and senha:
            print(f"[LoginEmailSenha] Autenticação simulada para {email}.")
            return True
        print("[LoginEmailSenha] Falha na autenticação.")
        return False

class LoginGoogle(Autenticacao):
    def autenticar(self, **kwargs) -> bool:
        token = kwargs.get("token")

        print("[LoginGoogle] Enviando token ao endpoint fictício do Google...")
        # Simulação de chamada à API do Google
        print("→ POST https://accounts.google.com/o/oauth2/token")
        print(f"→ Dados enviados: token={token}")

        # Simula uma resposta da API
        if token == "google_valid_token":
            print("[LoginGoogle] Token validado pelo Google com sucesso.")
            return True
        print("[LoginGoogle] Token inválido pelo Google.")
        return False

class LoginMicrosoft(Autenticacao):
    def autenticar(self, **kwargs) -> bool:
        token = kwargs.get("token")

        print("[LoginMicrosoft] Enviando token ao endpoint fictício da Microsoft...")
        # Simulação de chamada à API da Microsoft
        print("→ POST https://login.microsoftonline.com/common/oauth2/v2.0/token")
        print(f"→ Dados enviados: token={token}")

        # Simula uma resposta da API
        if token == "microsoft_valid_token":
            print("[LoginMicrosoft] Token validado pela Microsoft com sucesso.")
            return True
        print("[LoginMicrosoft] Token inválido pela Microsoft.")
        return False

# Contexto (Serviço de Autenticação)
class ServicoAutenticacao:
    def __init__(self, estrategia: Autenticacao = None):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: Autenticacao):
        print(f"\n[ServicoAutenticacao] Estratégia definida: {type(estrategia).__name__}")
        self._estrategia = estrategia

    def autenticar(self, **kwargs) -> bool:
        if not self._estrategia:
            raise ValueError("Nenhuma estratégia de autenticação definida.")
        print(f"[ServicoAutenticacao] Executando autenticação via {type(self._estrategia).__name__}...")
        return self._estrategia.autenticar(**kwargs)
```

## Referências Bibliográficas

Strategy. Disponível em: <[https://refactoring.guru/design-patterns/strategy](https://refactoring.guru/design-patterns/strategy)>. acesso em: 22 de outubro de 2025.

SERRANE, milene. AULA - GOFS COMPORTAMENTAIS. Disponível em: <[https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf)>. acesso em: 22 de outubro de 2025.

## Histórico de versão

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 24/10/2025  | Criação da Modelagem e código do padrão de projeto observer | [Ruan Sobreira Carvalho](https://github.com/Ruan-Carvalho), [Arthur Augusto Rezende da Paixão](https://github.com/arthur-augusto), [Paulo Henrique L. Dantas](https://github.com/Nanashii76) e [Natan Almeida](https://github.com/natanalmeida03) | - | - | - |