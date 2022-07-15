from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import PickleStorage

from settings import API_KEY

storage = PickleStorage('./data.pickle')
lilabred_bot = Bot(token=API_KEY)
dp = Dispatcher(bot=lilabred_bot, storage=storage)
