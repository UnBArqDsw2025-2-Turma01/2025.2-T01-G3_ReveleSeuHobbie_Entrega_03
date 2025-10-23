# Abstract Factory

## Introdução

Os **padrões de projeto criacionais** têm como objetivo fornecer mecanismos de criação de objetos que aumentam a flexibilidade e a reutilização do código, abstraindo o processo de instanciação de objetos (GAMMA et al., 1995).

Dentre os padrões de projeto, o ***Abstract Factory*** se destaca por fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas (REFACTORING GURU, 2023). Essa característica torna o **GoF *Abstract Factory*** uma solução ideal para sistemas que precisam ser independentes de como seus objetos são criados, compostos e representados (SOURCEMAKING, 2023).

## Metodologia

A construção do **GoF *Abstract Factory*** **baseou-se** primeiramente nos conhecimentos adquiridos durante as aulas ministradas pela professora Milene Serrano e seus slides **GoF Criacionais(2025)**, além da análise da literatura do livro **Gamma et al. (2000).**

Cada integrante teve uma visão do padrão a ser implementado, portanto, houve uma reunião informal, em sala de aula, onde se decidiu que cada um pensasse em uma ideia e a apresentasse em reunião. Ao se aprofundar no assunto, algumas divergências deram lugar a um consenso comum por mensagens. Assim, ao se realizar a reunião, tudo foi feito de maneira sucinta, já tendo uma direção a ser seguida. Apesar das divergências em como implementar de fato e em como realizar a modelagem durante o processo, tudo ocorreu de forma limpa e rápida.

 A gravação da reunião está a seguir: 

| Reunião | Integrantes | Data | Link |
| :---- | :---- | :---- | :---- |
| 01 | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) | 22/10/2025 | [https://www.youtube.com/watch?v=p1Aoxzym0Dk](https://youtu.be/p1Aoxzym0Dk) |

<iframe width="768" height="640" src="https://miro.com/app/live-embed/uXjVJ1he4VE=/?focusWidget=3458764632024456495&embedMode=view_only_without_ui&embedId=88483689390" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

## Modelagem

A seguir, é possível visualizar a modelagem gerada:
<p align="center">Modelagem do GoF Abstract Factory</p>

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVJ1g_CSw=/?embedMode=view_only_without_ui&moveToViewport=-802,72,2535,1245&embedId=490792907473" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

<p align = "center">Autoria de <a href="https://github.com/Gabrielfcoelho">Gabriel Flores</a>, <a href="https://github.com/igorvdaniel">Ígor Veras Daniel</a> e <a href="https://github.com/matheusdealcantara">Matheus de Alcântara</a> </p>

## Implementação

```python
from abc import ABC, abstractmethod

# Produtos Abstratos
class Forum(ABC):
    @abstractmethod
    def exibir(self): pass

class Publicacao(ABC):
    @abstractmethod
    def exibir(self): pass

class Comentario(ABC):
    @abstractmethod
    def exibir(self): pass


# Produtos Concretos: Comunidade Pública
class ForumPublico(Forum):
    def exibir(self): print("Fórum público visível a todos")

class PublicacaoPublica(Publicacao):
    def exibir(self): print("Publicação pública aberta para leitura e comentários")

class ComentarioPublico(Comentario):
    def exibir(self): print("Comentário público visível para todos os usuários")


# Produtos Concretos: Comunidade Privada
class ForumPrivado(Forum):
    def exibir(self): print("Fórum privado restrito a membros convidados")

class PublicacaoPrivada(Publicacao):
    def exibir(self): print("Publicação privada acessível apenas a membros")

class ComentarioPrivado(Comentario):
    def exibir(self): print("Comentário privado visível somente a membros do grupo")


# Fábrica Abstrata
class ComunidadeFactory(ABC):
    @abstractmethod
    def criar_forum(self): pass

    @abstractmethod
    def criar_publicacao(self): pass

    @abstractmethod
    def criar_comentario(self): pass


# Fábricas Concretas
class ComunidadePublicaFactory(ComunidadeFactory):
    def criar_forum(self): return ForumPublico()
    def criar_publicacao(self): return PublicacaoPublica()
    def criar_comentario(self): return ComentarioPublico()

class ComunidadePrivadaFactory(ComunidadeFactory):
    def criar_forum(self): return ForumPrivado()
    def criar_publicacao(self): return PublicacaoPrivada()
    def criar_comentario(self): return ComentarioPrivado()


# Código Cliente
def exibir_conteudo(factory: ComunidadeFactory):
    forum = factory.criar_forum()
    publicacao = factory.criar_publicacao()
    comentario = factory.criar_comentario()
    forum.exibir()
    publicacao.exibir()
    comentario.exibir()


# Escolhendo o tipo de comunidade
print("=== Comunidade Pública ===")
exibir_conteudo(ComunidadePublicaFactory())

print("\n=== Comunidade Privada ===")
exibir_conteudo(ComunidadePrivadaFactory())

```

## Referências Bibliográficas

GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; et al. **Padrões de projetos: soluções reutilizáveis de software orientados a objetos**. Porto Alegre: Bookman, 2000\. *E-book.* p.99. ISBN 9788577800469\. Disponível em: [https://app.minhabiblioteca.com.br/reader/books/9788577800469/](https://app.minhabiblioteca.com.br/reader/books/9788577800469/). Acesso em: 20 out. 2025\.  
SERRANO, Milene. **AULA \- GOFS CRIACIONAIS**. 2025\. Disponível em: [https://aprender3.unb.br/pluginfile.php/3178396/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178396/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf). Acesso em: 22 out. 2025,
SOURCEMAKING. *Abstract Factory Design Pattern*. Disponível em: [https://sourcemaking.com/design_patterns/abstract_factory](https://sourcemaking.com/design_patterns/abstract_factory). Acesso em: 20 out. 2025\.  

  

## Tabela de Versionamento

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 22/10/2025  | Criação da Modelagem e código do padrão de projeto Abstract Factory aplicado a comunidades | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) | - | - | - |
| `1.1` | 23/10/2025  | Criação da documentação|  [Gabriel Flores](https://github.com/Gabrielfcoelho)| - | - | - |