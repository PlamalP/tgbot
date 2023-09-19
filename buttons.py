from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

products_cb = CallbackData()


def get_start_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Фильм', callback_data='get_all_films')],
        [InlineKeyboardButton(text='Аниме', callback_data='get_all_anime')],
        [InlineKeyboardButton(text='Сериал', callback_data='get_all_serials')],
        [InlineKeyboardButton(text='Книга', callback_data='get_all_books')],
        [InlineKeyboardButton(text='Добавить', callback_data='add_new_smth')]
    ])

    return ikb


def get_start_ikb2() -> InlineKeyboardMarkup:
    ikb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='фильм', callback_data='add_film')],
        [InlineKeyboardButton(text='аниме', callback_data='add_anime')],
        [InlineKeyboardButton(text='сериал', callback_data='add_serial')],
        [InlineKeyboardButton(text='книга', callback_data='add_book')]
    ])

    return ikb2
