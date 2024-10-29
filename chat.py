
from utils import *


async def create_chat_completion(prompt: str):
    try:
        chat_history.append({'role': 'user', 'content': prompt})  # Добавляем новое сообщение пользователя в историю
        stream = await client.chat.completions.create(
            messages=chat_history,  # Передаём всю историю сообщений
            model=CurrentModel.model,  # Используем текущую модель
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
        with (open(log_file, 'a+', encoding='utf-8') as l,
              open(note_file, 'w', encoding='utf-8') as n):  # Записываем ответ в лог
            l.write(f'{'*' * 50}\n')
            l.write(f'{NowTime.now_time}: {prompt}\n')
            l.write(f'{'*' * 50}\n')
            l.write(f'{NowTime.now_time}: {output}\n')
            n.write(f"{prompt}\n {'*' * 50}\n{output}\n")
    except Exception as e:
        print(f"Error: {e}")
        with open(log_file, 'a+', encoding='utf-8') as l:
            l.write(f'{NowTime.now_time}: {e}\n')
