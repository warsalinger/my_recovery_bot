from aiogram import Bot, Dispatcher, executor, types
token = '6131415247:AAHatmlzn_kWi0M-nytd7xqvkfAETLWSJ9Q'
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nТы в начале долгого, но важного пути!")

@dp.message_handler()
async def echo(message: types.Message):
   if message.text == 'Привет':
    await message.answer('Привет, '+str(message.from_user.first_name))
executor.start_polling(dp, skip_updates=True)
