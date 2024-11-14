import requests # Добавление библиотеки для отправки запросов

# Дефолтные значения
URL = 'https://api.pokemonbattle.ru/v2'
Trainer_token = 'd8e2ddfcd39229fceebfcb66a27cdfb2'
HEADER = {'Content-Type':'application/json', 'trainer_token' : Trainer_token}


# 1. Тест – создание покемона
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)

new_pokemon_id = response_create_pokemon.json().get("id") # Сохранить в переменную id созданного покемона

# 2. Тест – смена имени покемона
body_change_name = {
    "pokemon_id": new_pokemon_id,
    "name": "New Name",
    "photo_id": 8
}

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

# 3. Тест – поймать покемона в покебол
body_add_pokeball = {
    "pokemon_id": new_pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_change_name.text)


# Проверка корректности полученного статуса ответа

RED = '\033[91m' # Добавление цветов, для отображения на консоле значения с цветом
GREEN = '\033[92m'
RESERT = '\033[0m'

if response_create_pokemon.status_code == 201:
    print(f'Создание покемона – {GREEN}OK{RESERT}')
else:
    print(f'Создание покемона – {RED}ERROR{RESERT}')


if response_change_name.status_code == 200:
    print(f'Смена имени покемона – {GREEN}OK{RESERT}')
else:
    print(f'Смена имени покемона – {RED}ERROR{RESERT}')

if response_add_pokeball.status_code == 200:
    print(f'Поймать покемона в покебол – {GREEN}OK{RESERT}')
else:
    print(f'Поймать покемона в покебол – {RED}ERROR{RESERT}')