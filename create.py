from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

bot = Bot(token='5729459971:AAEocY-4n-2PISfSjKOV2SKR5DloZb2goVY')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)