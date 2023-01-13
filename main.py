import answers
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5469183576:AAEkGZTU69_cMmx5JUPDoPwS_nHkEK6F4N4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("Хай!\nЯ RSmartBot!\nПоговори со мной")
@dp.message_handler()
async def GIF(message: types.Message):
    # bot.sendAnimation(chat_id = '@AndroidTehna', animation = 'dog-saying-no-no')
    await message.answer(answers.get_answer(message.text))

@dp.message_handler()
async def answer(message: types.Message):
    # bot.sendAnimation(chat_id = '@AndroidTehna', animation = 'dog-saying-no-no')
    await message.answer(answers.get_answer(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)