import os
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data_base.data_base import DataBase
from config import db_path

memory = MemoryStorage

bot = Bot(os.getenv('TOKEN'), parse_mode='HTML')
