import os

from openai import AsyncOpenAI

import json


class GetAPI:
    if "api_config.json" not in os.listdir():
        with open('api_config.json', 'a+') as f:
            try:
                conf = json.load(f)
                api_key = conf.get('api_key')
            except json.JSONDecodeError:
                api_key = input("Введите ключ API: ")
                json.dump({'api_key': api_key}, f)
    else:
        with open('api_config.json', 'r') as f:
            try:
                conf = json.load(f)
                api_key = conf.get('api_key')
            except json.JSONDecodeError:
                print("Ключ API не найден. Пожалуйста, обновите api_config.json")


client = AsyncOpenAI(
    api_key=GetAPI().api_key,
    base_url='https://fresedgpt.space/v1'
)
chat_history = []  # Инициализируем список для хранения сообщений
log_dir = 'Logs'  # Директория для логов
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, 'chat.md')
note_file = os.path.join(log_dir, '00_note.md')
