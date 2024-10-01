import asyncio
import textwrap
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key='fresed-NQUmtrwXXd4RreAJKJGS52UiLsToUo',
    base_url='https://fresedgpt.space/v1'
)

# Инициализируем список для хранения сообщений
chat_history = []


async def test_create_chat_completion(prompt: str):
    # Добавляем новое сообщение пользователя в историю
    chat_history.append({'role': 'user', 'content': prompt})

    stream = await client.chat.completions.create(
        messages=chat_history,  # Передаём всю историю сообщений
        model='gpt-4',
        stream=True
    )

    output = ""
    async for chunk in stream:
        output += chunk.choices[0].delta.content or ''

    # Ограничиваем вывод 100 символами с переносом по словам
    wrapped_output = "\n".join(textwrap.fill(line, width=100, replace_whitespace=False) for line in output.splitlines())

    print(wrapped_output)
    print('\n')

    # Добавляем ответ модели в историю
    chat_history.append({'role': 'assistant', 'content': output})


async def main():
    while True:
        prompt = input('>> ')
        await test_create_chat_completion(prompt)


if __name__ == '__main__':
    asyncio.run(main())
