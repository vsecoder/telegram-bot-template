from aiogram import Router
import os
from importlib import import_module


def get_dialog_router() -> Router:
    router = Router()
    for module in os.listdir(os.path.dirname(__file__)):
        if module == "__init__.py" or module[-3:] != ".py":
            continue
        router.include_router(
            getattr(import_module(f".{module[:-3]}", __package__), "ui", None)
        )
    return router
