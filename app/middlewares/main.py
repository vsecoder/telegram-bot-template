from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app import bot, client, config, dp


class MainMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.config = config
        self.bot = bot
        self.client = client

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["bot"] = self.bot
        data["client"] = self.client
        await handler(event, data)


md = MainMiddleware()
dp.message.middleware(md)
dp.callback_query.middleware(md)
