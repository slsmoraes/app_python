import requests
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    #print(response.json())
    #print(type(response.json()))
    dados_cep = response.json()
    print('Logradouro: {}'.format(dados_cep['logradouro']))
    print('CEP: {}'.format(dados_cep['complemento']))

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    print(response.status_code)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('22041001')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)
    # print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://globallabs.academy/')
    print(response)