import datetime
from utils import *


async def create_chat_completion(prompt: str):
    try:
        chat_history.append({'role': 'user', 'content': prompt})  # Добавляем новое сообщение пользователя в историю
        stream = await client.chat.completions.create(
            messages=chat_history,  # Передаём всю историю сообщений
            model='gpt-4-turbo',
            stream=True
        )
        print(f"\n{'#' * 50}\n")
        output = ""
        async for chunk in stream:
            segment = chunk.choices[0].delta.content or ''
            output += segment
            print(segment, end='', flush=True)
        print('\n')
        print("*" * 50)  # Добавляем строку из 50 "*"
        chat_history.append({'role': 'assistant', 'content': output})  # Добавляем ответ модели в историю
        with open(log_file, 'a+') as f:  # Записываем ответ в лог
            f.write(f'{datetime.datetime.now()}: {prompt}\n')
            f.write(f'{datetime.datetime.now()}: {output}\n')
    except Exception as e:
        print(f"Error: {e}")
        with open(log_file, 'a+') as f:
            f.write(f'{datetime.datetime.now()}: {e}\n')
