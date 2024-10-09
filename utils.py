import os

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key='fresed-NQUmtrwXXd4RreAJKJGS52UiLsToUo',
    base_url='https://fresedgpt.space/v1'
)
chat_history = []  # Инициализируем список для хранения сообщений
log_dir = 'logs'  # Директория для логов
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, 'chat.md')
note_file = os.path.join(log_dir, '00_note.md')