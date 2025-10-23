# Iterator

## Introdução

Os **padrões de projeto comportamentais** têm como objetivo definir maneiras eficientes de comunicação entre objetos e delegar responsabilidades, reduzindo o acoplamento entre eles e favorecendo a flexibilidade do sistema (GAMMA et al., 1995).

Dentre os padrões de projeto, o ***Iterator*** se destaca por encapsular o modo de acesso e travessia dos elementos de uma coleção (ou agregado), independentemente de sua representação interna (REFACTORING GURU, 2023). Essa característica torna o **GoF *Iterator*** uma solução ideal para sistemas que exigem uma forma uniforme de percorrer estruturas de dados complexas sem expor sua implementação (SOURCEMAKING, 2023).
## Metodologia

A construção do **GoF *Iterator*** foi primeiramente construída a partir dos conhecimentos adquiridos durante as aulas ministradas pela professora Milene Serrano e seus slides **GoF Comportamentais(2025)**, além da análise da literatura do livro  **Gamma et al. (2000).**
Cada integrante teve uma visão do padrão a ser implementado, por tanto houve uma reunião informal, em sala de aula, onde foi-se decidido cada um pensar em uma ideia e apresentar em reunião, ao se aprofundar algumas divergências se tornaram um concesso comum por mensagens, assim ao se realizar a reunião tudo foi feito de maneira sucinta, já tendo uma direção a ser seguida, apesar das divergências em como implementar de fato e em como realizar a modelagem durante o processo, tudo ocorreu de forma limpa e rápida.

 A gravação da reunião está a seguir: 

| Reunião | Integrantes | Data | Link |
| :---- | :---- | :---- | :---- |
| 01 | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) | 22/10/2025 | [https://www.youtube.com/watch?v=5zEgtbCzGNo](https://www.youtube.com/watch?v=5zEgtbCzGNo) |

<iframe width="750" height="432" src="https://www.youtube.com/embed/5zEgtbCzGNo" title="Criação do Iterator" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Modelagem

A seguir, é possível visualizar a da modelagem gerada:
<p align="center">Modelagem do GoF Iterator</p>

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVJ1g_CSw=/?embedMode=view_only_without_ui&moveToViewport=-802,72,2535,1245&embedId=490792907473" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

<p align = "center">Autoria de <a href="https://github.com/Gabrielfcoelho">Gabriel Flores</a>, <a href="https://github.com/igorvdaniel">Ígor Veras Daniel</a> e <a href="https://github.com/matheusdealcantara">Matheus de Alcântara</a> </p>

## Implementação

```python
import datetime
import time
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable

class Comentario:
    def __init__(self, id_usuario: str, conteudo: str):
        self.id_usuario = id_usuario
        self.conteudo = conteudo
        self.timestamp = datetime.datetime.now() # Adicionado para ordenação

    def __repr__(self):
        return (f"Comentario(por: {self.id_usuario}, "
                f"em: {self.timestamp.strftime('%H:%M:%S')}, "
                f"conteudo: '{self.conteudo[:20]}...')")


class IForum(Iterable):
    @abstractmethod
    def adicionar_comentario(self, comentario: Comentario):
        """Adiciona um item à coleção."""
        pass
    
    @abstractmethod
    def __iter__(self) -> Iterator:
        """Retorna o iterador padrão."""
        pass
    
    @abstractmethod
    def reverse_iterator(self) -> Iterator:
        """Retorna um iterador com ordem diferente."""
        pass


class Forum(IForum):
    def __init__(self, nome: str, id_comunidade: str):
        self.nome = nome
        self.id_comunidade = id_comunidade
        self._comentarios = [] 

    def adicionar_comentario(self, comentario: Comentario):
        """Adiciona um novo comentário à lista interna."""
        print(f"[Fórum {self.nome}] Novo comentário de {comentario.id_usuario}")
        self._comentarios.append(comentario)

    def __len__(self):
        """Método auxiliar para os iteradores."""
        return len(self._comentarios)
        
    def get_comentarios_list(self):
        """
        Método que os iteradores usarão para acessar 
        a coleção interna de forma controlada.
        """
        return self._comentarios

    def __iter__(self) -> Iterator:
        return IteradorComentarios(self)
        
    def reverse_iterator(self) -> Iterator:
        return IteradorComentariosReverso(self)

class IteradorComentarios(Iterator):
    def __init__(self, forum: Forum):
        self._forum = forum
        self._posicao = 0 
        self._comentarios_snapshot = self._forum.get_comentarios_list()

    def __next__(self):
        try:
            comentario = self._comentarios_snapshot[self._posicao]
            self._posicao += 1
        except IndexError:
            raise StopIteration()
        return comentario
        
    def __iter__(self):
        return self


class IteradorComentariosReverso(Iterator):
    def __init__(self, forum: Forum):
        self._forum = forum
        self._posicao = len(self._forum) - 1 
        self._comentarios_snapshot = self._forum.get_comentarios_list()

    def __next__(self):
        """Retorna o próximo item (em ordem reversa)."""
        if self._posicao < 0:
            raise StopIteration()
        else:
            comentario = self._comentarios_snapshot[self._posicao]
            self._posicao -= 1
            return comentario
            
    def __iter__(self):
        return self

if __name__ == "__main__":
    
    print("--- Padrão Iterator: Demonstração ---")
    
    # Cria a coleção (o Fórum)
    forum_de_ciclismo = Forum(nome="Clube de Ciclismo", id_comunidade="comu_cicl_01")

    # Adiciona itens
    forum_de_ciclismo.adicionar_comentario(
        Comentario("Ana", "Qual a melhor bicicleta para iniciantes?")
    )

    time.sleep(0.01) 
    forum_de_ciclismo.adicionar_comentario(
        Comentario("Bruno", "Depende. Eu prefiro mountain bike.")
    )
    time.sleep(0.01)
    forum_de_ciclismo.adicionar_comentario(
        Comentario("Carla", "Alguém quer pedalar no parque domingo?")
    )

    print("-" * 40)

    print("\nIteração Padrão (Antigo -> Novo):")
    try:
        for comentario in forum_de_ciclismo:
            print(f"  -> {comentario}")
    except Exception as e:
        print(f"Erro na iteração: {e}")
        
    print("-" * 40)

    print("\nIteração Reversa (Novo -> Antigo):")
    try:
        iterador_reverso = forum_de_ciclismo.reverse_iterator()
        for comentario in iterador_reverso:
            print(f"  -> {comentario}")
    except Exception as e:
        print(f"Erro na iteração reversa: {e}")

    print("\n--- Demonstração Concluída ---")
```

## Referências Bibliográficas

GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; et al. **Padrões de projetos: soluções reutilizáveis de software orientados a objetos**. Porto Alegre: Bookman, 2000\. *E-book.* p.99. ISBN 9788577800469\. Disponível em: [https://app.minhabiblioteca.com.br/reader/books/9788577800469/](https://app.minhabiblioteca.com.br/reader/books/9788577800469/). Acesso em: 20 out. 2025\.  
SERRANO, Milene. **AULA \- GOFS COMPORTAMENTAIS**. 2025\. Disponível em: [https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178398/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf). Acesso em: 22 out. 2025,   
  

## Tabela de Versionamento

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 22/10/2025  | Criação da Modelagem e código do padrão de projeto Iterator aplicado a classe comentario | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) | - | - | - |
