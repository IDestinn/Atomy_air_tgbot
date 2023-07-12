from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

presentation_btn = InlineKeyboardButton(text="📊Презентация", url="https://youtu.be/qiPagGLacBw")
about_btn = InlineKeyboardButton(text="🌟О продукции", callback_data="about")
signup_btn = InlineKeyboardButton(text="✍️Регистрация", callback_data="signup")
cooperation_btn = InlineKeyboardButton(text="🤑Сотрудничество", callback_data="cooperation")
teaching_btn = InlineKeyboardButton(text="🎓Обучение", callback_data="teaching")
question_btn = InlineKeyboardButton(text="❓Есть вопросы", callback_data="question")
back_btn = InlineKeyboardButton(text="↩️Вернуться в меню", callback_data="back")

atomy_rus_btn = InlineKeyboardButton(text="⏩Перейти на сайт АТОМИ РОССИЯ",
                                     url="https://www.atomy.ru/ru/Home/Product/MallMain")
atomy_uz_btn = InlineKeyboardButton(text="⏩Перейти на сайт АТОМИ УЗБЕКИСТАН",
                                    url="https://www.atomy.uz/uz/Home/Product/MallMain")
dock_btn = InlineKeyboardButton(text="📘Посмотреть каталог", url="https://disk.yandex.ru/i/oF4yIzU3YSh2kA")
dock_download_btn = InlineKeyboardButton(text="📘Скачать каталог", callback_data="dock_download")

register_btn = InlineKeyboardButton(text="✍️Перейти на форму регистрации",
                                    url="https://docs.google.com/forms/d/e/1FAIpQLSd_"
                                        "-roASqslqJDaY_pRqPr0RPPezIvwWZHl02lUwv_tz4frSw/viewform?usp=sf_link")
about_me_btn = InlineKeyboardButton(text="📞Связаться со мной", url="t.me/air_ilmira")

watch_cooperation_btn = InlineKeyboardButton(text="⏩Посмотреть видео",
                                             url="https://www.youtube.com/watch?v=F92X_Y5HyUI")

welcome_layout = InlineKeyboardMarkup(row_width=2).add(presentation_btn, about_btn, signup_btn,
                                                       cooperation_btn, teaching_btn, question_btn)
about_layout = InlineKeyboardMarkup(row_width=1).add(atomy_rus_btn, atomy_uz_btn, dock_btn, dock_download_btn, back_btn)
signup_layout = InlineKeyboardMarkup(row_width=1).add(register_btn, about_me_btn, back_btn)
cooperation_layout = InlineKeyboardMarkup(row_width=1).add(watch_cooperation_btn, back_btn)
teaching_layout = InlineKeyboardMarkup(row_width=1).add(back_btn)
question_layout = InlineKeyboardMarkup(row_width=1).add(about_me_btn, back_btn)
