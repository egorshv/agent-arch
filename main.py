import os
import asyncio
from anthropic import AsyncAnthropic, DefaultAioHttpClient

from settings import API_KEY


async def main() -> None:
    async with AsyncAnthropic(
        api_key=API_KEY,
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-opus-4-7",
        )
        print(message.content)


asyncio.run(main())
