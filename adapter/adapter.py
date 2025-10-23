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
    print(f"Não foi possível encontrar as coordenadas para '{evento.localizacao}'.")    print(f"Não foi possível encontrar as coordenadas para '{evento.localizacao}'.")