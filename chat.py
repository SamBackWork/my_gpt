from utils import chat_history, log_file, note_file, client
import aiofiles
import datetime


async def create_chat_completion(prompt: str):
    try:
        chat_history.append({'role': 'user', 'content': prompt})  # Добавляем новое сообщение в историю
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
        async with (aiofiles.open(log_file, 'a+', encoding='utf-8') as log,
                    aiofiles.open(note_file, 'w', encoding='utf-8') as note):  # Записываем ответ
            await log.write(f'{'*' * 50}\n')
            await log.write(f'{datetime.datetime.now()}: {prompt}\n')
            await log.write(f'{'*' * 50}\n')
            await log.write(f'{datetime.datetime.now()}: {output}\n')
            await note.write(f"{prompt}\n {'*' * 50}\n{output}\n")
    except Exception as e:
        print(f"Error: {e}")
        async with aiofiles.open(log_file, 'a+', encoding='utf-8') as log:
            await log.write(f'{datetime.datetime.now()}: {e}\n')
