from aiogram import types
from aiogram.dispatcher import Dispatcher


async def dock_download(call: types.CallbackQuery):
    file_path = "tg_bot/photos/catalog.pdf"
    # Send the compressed PDF file
    with open(file_path, "rb") as file:
        wait_message = await call.message.answer(text="Файл каталога отправляется")
        await call.bot.send_document(chat_id=call.from_user.id, document=file)
        await call.bot.delete_message(chat_id=call.from_user.id, message_id=wait_message.message_id)


def register_dock_download(dp: Dispatcher):
    dp.register_callback_query_handler(dock_download, text=["dock_download"])
