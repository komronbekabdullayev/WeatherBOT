from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes

from loader import dp
from utils.project_files.weatherapi import weather


# @dp.message_handler(content_types=ContentTypes.LOCATION)
@dp.message_handler(content_types='location')
async def get_weather(message: types.Message):
    location = message.location
    lat = location.latitude
    long = location.longitude
    data = weather(lat, long)

    await message.answer_photo(photo="https://t.me/botsrc/24",
                               caption=f"{data['name']}, {data['region']}, {data['country']}\n"
                                       f"Bugungi havo: {data['text']}\n"
                                       f"Harorat: {data['temp_c']}\n"
                                       f"Shamol tezligi: {data['wind']}\n"
                                       f"Shamol yo'nalishi: {data['wind_dir']}\n"
                                       f"\n"
                                       f"Yangilangan vaqt: {data['last_update_time']}")
