import enum
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



def log_message(content):  # Запись в лог сообщений с текущей датой
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} {CurrentModel.model} - {content}\n"
    with open(log_file, '+a', encoding='utf-8') as f:
        f.write(log_entry)


def read_file(file_path):  # Чтение файла
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(file_path, content):  # Запись в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def reset_app():  # Сброс приложения
    os.startfile("condition.bat")  # Запускаем новое приложение
    exit()  # Завершаем работу этого приложения


def starts_with_datetime(text):  # Проверка на то, что сообщение начинается с даты
    return re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text) is not None


class NowTime:  # Текущая дата и время для употребления в логах
    now_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")


class ModelGPT(enum.Enum):  # Перечисление не всех моделей доступных в OpenAI
    TURBO = 'gpt-4-turbo-2024-04-09'
    TURBO_PREVIEW = 'gpt-4-turbo-preview'
    TURBO_VISION_PREVIEW = "gpt-4-vision-preview"
    GPT_40 = "gpt-40"
    GPT_40_2024_05_13 = 'gpt-40-2024-05-13'
    GPT_40_2024_08_06 = 'gpt-40-2024-08-06'
    GPT_40_MINI = 'gpt-40-mini'
    GPT_40_MINI_2024_07_18 = 'gpt-40-mini-2024-07-18'
    GPT_40_REALTIME_PREVIEW_2024_10_01 = 'gpt-40-realtime-preview-2024-10-01'
    GPT_40_LATEST = 'chatgpt-40-latest'

    @classmethod
    def get_current_model(cls, model: 'ModelGPT') -> str:
        model = model.value
        if not os.path.exists("model_gpt.txt"):
            write_file("model_gpt.txt", model)
        return model

    @classmethod
    def print_all_models(cls):  # Печать всех моделей
        print('Доступные модели:')
        print(*[f"{num:2d}: {model.value}" for num, model in enumerate(ModelGPT, start=1)], sep='\n')
        return input("Выберите модель: ")

    @classmethod
    def change_of_model(cls, num_model: str):  # Изменение модели
        list_model = list(ModelGPT)
        if int(num_model) in range(len(list_model) + 1):
            model = list_model[int(num_model) - 1]
            model = cls.get_current_model(model)
            write_file("model_gpt.txt", model)
            reset_app()
        else:
            print("Неверный номер модели")


class CurrentModel:
    if "model_gpt.txt" in os.listdir():
        model = read_file("model_gpt.txt")
    else:
        model = ModelGPT.get_current_model(ModelGPT.TURBO)  # Тут мы устанавливаем текущую модель
