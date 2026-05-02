import asyncio

from anthropic import AsyncAnthropic, DefaultAioHttpClient

from settings import API_KEY

SYSTEM_ROLE = 'You are professional python backend developer'

async def main() -> None:
    messages_history = []

    while True:
        async with AsyncAnthropic(
            api_key=API_KEY,
            http_client=DefaultAioHttpClient()
        ) as client:
            user_message = input()
            user_message_formatted = {
                'role': 'user',
                'content': user_message,
            }
            messages_history.append(user_message_formatted)

            message = await client.messages.create(
                max_tokens=1024,
                messages=messages_history,
                system=SYSTEM_ROLE,
                model='claude-haiku-4-5'
            )
            print(message.content[0].text)

            messages_history.append({
                'role': 'assistant',
                'content': message.content[0].text,
            })



if __name__ == '__main__':
    asyncio.run(main())
