import asyncio
import datetime
from utils import chat_history, log_file
from chat import create_chat_completion
from log import history_log


async def main(history: list):
    with open("help_text.txt", 'r') as h, open(log_file, 'a+') as d:
        help_text = h.read()
        d.write(f'{datetime.datetime.now()}: Сеанс начался\n')
        while True:
            try:
                prompt = input('>> ')
                match prompt.lower():
                    case 'exit':
                        print('До новых встреч!)')
                        d.write(f'{datetime.datetime.now()}: Сеанс закончился\n')
                        exit()
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
                d.write(f'{datetime.datetime.now()}: {e}\n')


if __name__ == '__main__':
    asyncio.run(main(chat_history))
