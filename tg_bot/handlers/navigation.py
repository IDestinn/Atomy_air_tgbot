from aiogram import types, Dispatcher

from tg_bot.keyboards.inline import signup_layout, teaching_layout, question_layout, \
    about_layout, cooperation_layout


async def about(call: types.CallbackQuery):
    with open("tg_bot/texts/about.txt", "r", encoding="utf-8") as f:
        photo = types.input_media.InputMediaPhoto(open("tg_bot/photos/product.jpg", "rb"))
        await call.message.edit_media(media=photo)
        await call.message.edit_caption(caption=f.read(), reply_markup=about_layout)


async def signup(call: types.CallbackQuery):
    with open("tg_bot/texts/signup.txt", "r", encoding="utf-8") as f:
        await call.message.edit_caption(caption=f.read(), reply_markup=signup_layout)


async def cooperation(call: types.CallbackQuery):
    with open("tg_bot/texts/cooperation.txt", "r", encoding="utf-8") as f:
        photo = types.input_media.InputMediaPhoto(open("tg_bot/photos/cooperation.jpg", "rb"))
        await call.message.edit_media(media=photo)
        await call.message.edit_caption(caption=f.read(), reply_markup=cooperation_layout)


async def teaching(call: types.CallbackQuery):
    with open("tg_bot/texts/teaching.txt", "r", encoding="utf-8") as f:
        await call.message.edit_caption(caption=f.read(), reply_markup=teaching_layout)


async def question(call: types.CallbackQuery):
    with open("tg_bot/texts/question.txt", "r", encoding="utf-8") as f:
        await call.message.edit_caption(caption=call.from_user.get_mention() + f.read(), reply_markup=question_layout)


def register_navigation(dp: Dispatcher):
    dp.register_callback_query_handler(about, text=["about"])
    dp.register_callback_query_handler(signup, text=["signup"])
    dp.register_callback_query_handler(cooperation, text=["cooperation"])
    dp.register_callback_query_handler(teaching, text=["teaching"])
    dp.register_callback_query_handler(question, text=["question"])
