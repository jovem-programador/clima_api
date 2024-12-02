import requests # Requisições HTTP (GET, POST, PUT, DELETE)

# Chave de acesso API
API_KEY = '6d949e0dba60eba7fcfd36aca883af60'

# URL base da API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Cidade específica para a consulta
cidade = 'São Luis'

# Parâmetros da consulta
parametros = {
    'q': cidade, # Cidade
    'appid': API_KEY, # Chave da API
    'units': 'metric', # Para usar Celsius
    'lang': 'pt_br' # Idioma
}

# Fazendo a requisição
response = requests.get(BASE_URL, params=parametros)

print(response.json()) # Mostrar os dados

# Tratando a resposta
if response.status_code == 200:
    dados = response.json()

    print(f'Clima em: {dados['name']} - {dados['sys']['country']}')
    print(f'Descrição: {dados['weather'][0]['description']}')
    print(f'Temperatura: {dados['main']['temp']:.0f}°C')
    print(f'Sensação térmica: {dados['main']['feels_like']:.0f}°C')
    print(f'Umidade: {dados['main']['humidity']:.0f}%')
else:
    print(f'Erro: Não foi possível obter os dados ({response.status_code}).')