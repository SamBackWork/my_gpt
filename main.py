import asyncio

from utils import chat_history, log_file, log_message, read_file, reset_app, ModelGPT, CurrentModel
from chat import create_chat_completion
from log import history_log


async def main(history: list):
    help_text = read_file('help_text.txt')
    log_message('Сеанс начался\n')
    actions = {
        'exit': lambda: (print('До новых встреч!)'), log_message("Сеанс закончился\n"), exit()),
        'off': lambda: (history.clear(), print('Контекст отчищен')),
        'help': lambda: print(help_text),
        'history': lambda: history_log(log_file),
        'reset': lambda: reset_app(),
        'model': lambda: ModelGPT.change_of_model(ModelGPT.print_all_models())
    }
    while True:
        try:
            prompt = input('>> ')
            if prompt in actions:
                actions[prompt]()
            else:
                await create_chat_completion(prompt)
        except Exception as e:
            print(f"Error: {e}")
            log_message(f'{e}\n')


if __name__ == '__main__':
    print(f"Текущая модель: {CurrentModel.model}\n")
    asyncio.run(main(chat_history))
