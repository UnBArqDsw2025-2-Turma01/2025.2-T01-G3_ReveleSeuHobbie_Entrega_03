# Adapter

## Introdução

Os **padrões de projeto estruturais** têm como objetivo definir maneiras eficientes de compor objetos para que possam formar estruturas maiores (GAMMA et al., 1995).

Dentre os padrões de projeto, o **_Adapter_** se destaca por permitir que classes com interfaces incompatíveis colaborem entre si (REFACTORING GURU, 2023). Essa característica torna o **GoF _Adapter_** uma solução ideal para sistemas que exigem a integração de componentes legados com novas implementações ou serviços externos (SOURCEMAKING, 2023).

## Metodologia

A construção do **GoF _Adapter_** **baseou-se** primeiramente nos conhecimentos adquiridos durante as aulas ministradas pela professora Milene Serrano e seus slides **GoF Estruturais(2025)**, além da análise da literatura do livro **Gamma et al. (2000).**

Os participantes tiveram uma visão do padrão a ser implementado, com isso foi realizada uma reunião síncrona de forma remota para discutir as ideias e realizar a modelagem e implementação do padrão. Durante a reunião, cada integrante apresentou suas ideias e contribuições, o que levou a um consenso sobre a abordagem a ser adotada. A colaboração foi facilitada por meio de mensagens assíncronas, permitindo que todos os membros contribuíssem de maneira eficaz.

Como ferramenta de apoio, foi utilizado o [Miro](https://miro.com/app/dashboard/) para a criação do diagrama de classes, o [Microsoft VS Code](https://code.visualstudio.com/) para implementação do código em Python e o [Microsoft Teams](https://teams.microsoft.com/v2/) para a realização da reunião. A escolha dessas ferramentas foi motivada pela familiaridade dos integrantes com as mesmas e pela facilidade de uso em um ambiente remoto.

A gravação da reunião está a seguir:

| Reunião | Integrantes                                                                                                                                                              | Data       | Link                                                                                       |
| :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :----------------------------------------------------------------------------------------- |
| 01      | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) | 22/10/2025 | [https://www.youtube.com/watch?v=5zEgtbCzGNo](https://www.youtube.com/watch?v=5zEgtbCzGNo) |

<iframe width="750" height="432" src="https://www.youtube.com/embed/5zEgtbCzGNo" title="Criação do Iterator" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Modelagem

A seguir, é possível visualizar a da modelagem gerada:

<p align="center">Modelagem do GoF Iterator</p>

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVJ13Ld9g=/?embedMode=view_only_without_ui&moveToViewport=-2175,-1215,2333,1144&embedId=843316950452" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

<p align = "center">Autoria de <a href="https://github.com/Gabrielfcoelho">Gabriel Flores</a>, <a href="https://github.com/igorvdaniel">Ígor Veras Daniel</a> e <a href="https://github.com/matheusdealcantara">Matheus de Alcântara</a> </p>

## Implementação

```python
# import googlemaps

class Evento():
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao  # Ex: "Avenida Paulista, São Paulo"

class ServicoLocalizacao():
    def obter_coordenadas(self, endereco):
        pass

class GoogleMapsAdapter(ServicoLocalizacao):
    def __init__(self, api_key):
        try:
            self.gmaps = googlemaps.Client(key=api_key)
        except Exception as e:
            print(f"Erro ao inicializar o cliente Google Maps: {e}")
            self.gmaps = None

    def obter_coordenadas(self, endereco):
        if not self.gmaps:
            print("Cliente Google Maps não inicializado.")
            return None

        try:
            resultado = self.gmaps.geocode(endereco)
            if resultado:
                return resultado[0]['geometry']['location']  # {'lat': ..., 'lng': ...}
        except googlemaps.exceptions.ApiError as e:
            print(f"Erro na API do Google Maps: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        return None

# Stub para testes
class ServicoLocalizacaoStub(ServicoLocalizacao):
    """
    Um Stub para o serviço de localização.
    Não faz chamadas de rede e retorna dados fixos.
    Ótimo para testes unitários e desenvolvimento.
    """
    def __init__(self):
        print("STUB: Inicializado (Simulação local, sem custo).")
        self.coordenadas_falsas = {
            "Faculdade de Ciência e Tecnologia em Engenharia, Brasília": {'lat': -15.9901192, 'lng': -48.0432468}
        }

    def obter_coordenadas(self, endereco):
        print(f"STUB: Buscando '{endereco}' localmente...")
        return self.coordenadas_falsas.get(endereco, {'lat': 0, 'lng': 0})

def gerar_html_mapa_embed(coordenadas, api_key, zoom=17):
    """
    Gera o código HTML <iframe> para o Maps Embed API usando coordenadas.
    """
    if not coordenadas:
        return "<p>Localização não encontrada.</p>"

    lat = coordenadas['lat']
    lng = coordenadas['lng']

    url_mapa = f"https://www.google.com/maps/embed/v1/view?key={api_key}&center={lat},{lng}&zoom={zoom}"

    html_embed = f'<iframe \n  width="600" \n  height="450" \n  style="border:0" \n  loading="lazy" \n  allowfullscreen \n  src="{url_mapa}">\n</iframe>'

    return html_embed

# Execução no cliente
API_KEY = 'MinhaChaveAPI'
# 1. Use seu adapter para obter as coordenadas
adapter = ServicoLocalizacaoStub()
evento = Evento("Aula", "Faculdade de Ciência e Tecnologia em Engenharia, Brasília")
coordenadas = adapter.obter_coordenadas(evento.localizacao)

if coordenadas:
    print(f"Coordenadas do evento '{evento.nome}': {coordenadas}")


    html_para_exibir = gerar_html_mapa_embed(coordenadas, API_KEY)

    print("\n--- Para ver o mapa ---")
    print("Copie o código HTML abaixo, salve em um arquivo (ex: 'mapa.html') e abra no seu navegador:\n")
    print(html_para_exibir)
else:
    print(f"Não foi possível encontrar as coordenadas para '{evento.localizacao}'.")
```

## Execução

```HTML
STUB: Inicializado (Simulação local, sem custo).
STUB: Buscando 'Faculdade de Ciência e Tecnologia em Engenharia, Brasília' localmente...
Coordenadas do evento 'Aula': {'lat': -15.9901192, 'lng': -48.0432468}

--- Para ver o mapa ---
Copie o código HTML abaixo, salve em um arquivo (ex: 'mapa.html') e abra no seu navegador:

<iframe
  width="600"
  height="450"
  style="border:0"
  loading="lazy"
  allowfullscreen
  src="https://www.google.com/maps/embed/v1/view?key=MinhaChaveAPI&center=-15.9901192,-48.0432468&zoom=17">
</iframe>
```

## Conclusão

A implementação do padrão de projeto **GoF _Adapter_** demonstrou sua eficácia na integração de sistemas com interfaces incompatíveis. Ao utilizar o **_Adapter_**, foi possível adaptar a interface do serviço de localização do Google Maps para atender às necessidades específicas do sistema desenvolvido, facilitando a obtenção de coordenadas geográficas a partir de endereços.

## Referências Bibliográficas

GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; et al. **Padrões de projetos: soluções reutilizáveis de software orientados a objetos**. Porto Alegre: Bookman, 2000\. _E-book._ p.99. ISBN 9788577800469\. Disponível em: [https://app.minhabiblioteca.com.br/reader/books/9788577800469/](https://app.minhabiblioteca.com.br/reader/books/9788577800469/). Acesso em: 20 out. 2025\.  
SERRANO, Milene. **AULA \- GOFS Estruturais**. 2025\. Disponível em: [https://aprender3.unb.br/pluginfile.php/3178397/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178397/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf). Acesso em: 22 out. 2025,
SOURCEMAKING. _Builder Design Pattern_. Disponível em: [https://sourcemaking.com/design_patterns/builder](https://sourcemaking.com/design_patterns/builder). Acesso em: 20 out. 2025\.

## Tabela de Versionamento

| Versão | Data       | Descrição                                                                                                                                  | Autor(es)                                                                                                                                                                | Revisor(es) | Comentário do revisor | Data da revisão |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | --------------------- | --------------- |
| `1.0`  | 22/10/2025 | Criação da Modelagem e código do padrão de projeto Adapter aplicado ao evento que possui localização obtida a partir da API do Google Maps | [Gabriel Flores](https://github.com/Gabrielfcoelho), [Ígor Veras Daniel](https://github.com/igorvdaniel) e [Matheus de Alcântara](https://github.com/matheusdealcantara) |        [Ana Luiza Soares](https://github.com/Ana-Luiza-SC)   | Não foi encontrado nenhum erro durante a revisão.                    | 23/10/2025               |
