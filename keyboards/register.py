from telegram import (ReplyKeyboardMarkup,KeyboardButton,
                    
)


 
def get_register_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="Ro'yxatdan o'tish"),
            KeyboardButton(text="🏠 Bosh sahifa "),
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
















# def get_language_keyboard()-> InlineKeyboardMarkup:
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text='Uzbek',callback_data='lang:uz'),
#             InlineKeyboardButton(text='English',callback_data='lang:en')
#         ]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard)
