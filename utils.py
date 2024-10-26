import os
import datetime
from openai import AsyncOpenAI
import re
import json


class GetAPI:
    if "api_config.json" not in os.listdir():
        with open('api_config.json', 'a+', encoding='utf-8') as f:
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


def log_message(content):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {content}\n"
    with open(log_file, '+a', encoding='utf-8') as f:
        f.write(log_entry)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


class NowTime:
    now_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")


def starts_with_datetime(text):
    return re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text) is not None
