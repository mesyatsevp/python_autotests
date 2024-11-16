import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "d8e2ddfcd39229fceebfcb66a27cdfb2"
HEADER = {'Content-Type' : "application/json", 'trainer_token' : TOKEN}
TRAINER_ID = "17718"

def test_status_code():
    response = requests.get (url = f'{URL}/pokemons', params = {'trainser_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respinse():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'New Name'

@pytest.mark.parametrize ('key, value', [('name', 'New Name'), ('trainer_id', TRAINER_ID), ('id', '135483')])
def test_parametrize (key, value):
    response_parametrize = requests.get (url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value


