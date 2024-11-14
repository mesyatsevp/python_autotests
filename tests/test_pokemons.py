import requests
import pytest

# Дефолтные значения
URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "d8e2ddfcd39229fceebfcb66a27cdfb2"
HEADER = {'Content-Type' : "application/json", 'trainer_token' : TOKEN}
TRAINER_ID = "17718"

@pytest.mark.parametrize('endpoint, expected_status', [('/trainers', 200)])

def test_get_status_code (endpoint, expected_status): # Тест на корректный статус ответа
    response = requests.get (f'{URL}{endpoint}', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == expected_status

def test_trainer_name_in_response (): # Тест на то, что в ответе приходит строчка с именем нужного тренера
    response = requests.get(f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    response_data = response.json()
    assert TRAINER_ID in response.text



