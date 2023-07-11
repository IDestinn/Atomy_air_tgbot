from aiogram import types, Dispatcher

from tg_bot.keyboards.inline import welcome_layout


async def welcome(message: types.Message):
    with open("tg_bot/texts/welcome.txt", "r", encoding="utf-8") as f:
        await message.answer_photo(photo=open("tg_bot/photos/logo.png", "rb"),
                                   caption=message.from_user.get_mention() + f.read(),
                                   reply_markup=welcome_layout)


def register_welcome(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['start'])
