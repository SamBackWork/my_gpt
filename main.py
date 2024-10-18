import asyncio
import datetime
from utils import chat_history, log_file
from chat import create_chat_completion
from log import history_log
import aiofiles


async def main(history: list):
    async with aiofiles.open("help_text.txt", 'r') as h:
        help_text = await h.read()
    async with aiofiles.open(log_file, 'a+') as d:
        await d.write(f'{datetime.datetime.now()}: Сеанс начался\n')
        while True:
            try:
                prompt = await asyncio.to_thread(input, '>> ')
                match prompt.lower():
                    case 'exit':
                        print('До новых встреч!)')
                        await d.write(f'{datetime.datetime.now()}: Сеанс закончился\n')
                        return
                    case 'off':
                        history.clear()  # Очищаем историю
                        print('Контекст отчищен')
                        continue
                    case 'help':
                        print(help_text)
                        continue
                    case 'history':
                        history_log(log_file)
                        continue
                    case _:
                        await create_chat_completion(prompt)
            except Exception as e:
                print(f"Error: {e}")
                await d.write(f'{datetime.datetime.now()}: {e}\n')


if __name__ == '__main__':
    asyncio.run(main(chat_history))

