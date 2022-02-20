"""There is some needed objects and types"""
from dataclasses import dataclass

from aiogram import Router

from app.config_parser import Config
from app.db.functions import DB


@dataclass
class FMT:
    db: DB
    config: Config


class FRouter(Router):
    def init(self):
        self.message.bind_filter()  # // self.filters.extend(filters)