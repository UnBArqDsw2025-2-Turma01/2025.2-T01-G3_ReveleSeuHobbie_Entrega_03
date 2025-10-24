# Observer 

## Introdução

Este artefato documenta a aplicação do padrão de projeto comportamental Observer no projeto Revele seu Hobbie. O Observer é um padrão de design comportamental que permite definir um mecanismo de assinatura para notificar vários objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

## Metodologia

Para o desenvolvimento do trabalho, foram realizadas as seguintes etapas:

1. Estudo do observer com videos e material da professora;
2. Elaboração do diagrama utilizando o draw.io;
3. Desenvolvimento do código;
4. Desenvolvimento deste artefato

O desenvolvimento aconteceu em uma video chamada no teams.
Disponível [aqui](https://unbbr-my.sharepoint.com/:v:/g/personal/222006169_aluno_unb_br/EZmuOaIGDuhEm-0E5mRHDREBbccaEFDJGd7MzXDVIR_i3w?e=Dgb2XT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).

## Modelagem

A seguir, é possível visualizar a modelagem gerada:

<p align="center">Modelagem do Gof comportamental Observer</p>

![observer modfelagem](/assets/observer.png)

## Implementação

```python
from abc import ABC, abstractmethod
from typing import List

# Interface Notificacao 
class Notificacao(ABC):
    @abstractmethod
    def notificacao(self):
        pass


#  Interface Observer 
class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


#  Classe ServicoNotificacao  
class ServicoNotificacao(Notificacao):
    def __init__(self):
        self._observers: List[Observer] = []
        self._mensagens: List[str] = []

    def adicionar_observer(self, observer: Observer):
        self._observers.append(observer)

    def remover_observer(self, observer: Observer):
        self._observers.remove(observer)

    def adicionar_mensagem(self, mensagem: str):
        self._mensagens.append(mensagem)
        self.notifica(mensagem)

    def notificacao(self):
        print("Nova notificação adicionada ao serviço.")

    def notifica(self, mensagem: str):
        for observer in self._observers:
            observer.atualizar(mensagem)


# Observers 
class NotificacaoWeb(Observer):
    def atualizar(self, mensagem: str):
        print(f"[WEB] Nova mensagem: {mensagem}")


class NotificacaoMobile(Observer):
    def atualizar(self, mensagem: str):
        print(f"[MOBILE] Nova mensagem: {mensagem}")


if __name__ == "__main__":
    servico = ServicoNotificacao()

    web = NotificacaoWeb()
    mobile = NotificacaoMobile()

    servico.adicionar_observer(web)
    servico.adicionar_observer(mobile)

    servico.adicionar_mensagem("Bem-vindo ao sistema")
    servico.adicionar_mensagem("Você tem uma nova notificação.")

```

## Referências Bibliográficas

Observer. Disponível em: <[https://refactoring.guru/design-patterns/observer](https://refactoring.guru/design-patterns/observer)>. acesso em: 22 de outubro de 2025.

SERRANE, milene. AULA - GOFS COMPORTAMENTAIS. Disponível em: <[https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf)>. acesso em: 22 de outubro de 2025.

## Histórico de versão

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 24/10/2025  | Criação da Modelagem e código do padrão de projeto observer | [Ruan Sobreira Carvalho](https://github.com/Ruan-Carvalho), [Arthur Augusto Rezende da Paixão](https://github.com/arthur-augusto), [Paulo Henrique L. Dantas](https://github.com/Nanashii76) e [Natan Almeida](https://github.com/natanalmeida03) | [Matheus de Alcântara](https://github.com/matheusdealcantara) | - | - |