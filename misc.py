import logging
import os
from aiogram import Bot, Dispatcher
from game import Game


bot = Bot(token=os.getenv('1536436143:AAF-3hbGKoU0ty6C-wz4DuOP3d-KzIje-c4'))
dp = Dispatcher(bot)
g = Game('crocobot.db')
logging.basicConfig(level=logging.INFO)
