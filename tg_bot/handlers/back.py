from aiogram import types, Dispatcher

from tg_bot.keyboards.inline import welcome_layout


async def back_to_welcome(call: types.CallbackQuery):
    with open("tg_bot/texts/welcome.txt", "r", encoding="utf-8") as f:
        photo = types.input_media.InputMediaPhoto(open("tg_bot/photos/logo.png", "rb"))
        await call.message.edit_media(media=photo)
        await call.message.edit_caption(caption=call.from_user.get_mention() + f.read(), reply_markup=welcome_layout)


def register_back(dp: Dispatcher):
    dp.register_callback_query_handler(back_to_welcome, text=["back"])
