import asyncio
from aiogram.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from buttons import get_start_ikb, get_start_ikb2
import database


bot = Bot(token='6370468816:AAFM3Lol9CsTjobP4k8ifbUDqCO6WcuvRgQ')
dp = Dispatcher()


class MediaStateGroup(StatesGroup):
    title = State()
    type = State()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    if message.from_user.id == 825538712:
        await database.db_connect()
        await message.answer(f'Ку')
        await message.answer(f'Что тебе надо?',
                             reply_markup=get_start_ikb())
    else:
        await message.answer(f'Ку, {message.from_user.first_name} ')
        await message.answer(f'Пошел отсюда')


@dp.callback_query(lambda callback_query: callback_query.data == 'get_all_films')
async def cb_get_all_films(callback: CallbackQuery):
    await callback.message.delete()
    films = await database.get_all_films()
    await callback.message.answer(str(films),
                                  reply_markup=get_start_ikb())
    await callback.answer()


@dp.callback_query(lambda callback_query: callback_query.data == 'get_all_anime')
async def cb_get_all_films(callback: CallbackQuery):
    await callback.message.delete()
    anime = await database.get_all_anime()
    await callback.message.answer(str(anime),
                                  reply_markup=get_start_ikb())
    await callback.answer()


@dp.callback_query(lambda callback_query: callback_query.data == 'get_all_serials')
async def cb_get_all_films(callback: CallbackQuery):
    await callback.message.delete()
    serials = await database.get_all_serials()
    await callback.message.answer(str(serials),
                                  reply_markup=get_start_ikb())
    await callback.answer()


@dp.callback_query(lambda callback_query: callback_query.data == 'get_all_books')
async def cb_get_all_films(callback: CallbackQuery):
    await callback.message.delete()
    books = await database.get_all_books()
    await callback.message.answer(str(books),
                                  reply_markup=get_start_ikb())
    await callback.answer()


@dp.callback_query(lambda callback_query: callback_query.data == 'add_new_smth')
async def cd_add_new_smth(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer('Напиши название, потом выбери тип')


@dp.message()
async def add_smth(message: Message) -> None:
    await message.answer(text=f'{message.text}', reply_markup=get_start_ikb2())


@dp.callback_query(lambda callback_query: callback_query.data == 'add_film')
async def cd_add_new_smth(callback: CallbackQuery) -> None:
    await callback.message.delete()
    smth = str(callback.message.text)
    await database.add_film(smth)
    await callback.message.answer('Добавлено', reply_markup=get_start_ikb())


@dp.callback_query(lambda callback_query: callback_query.data == 'add_anime')
async def cd_add_new_smth(callback: CallbackQuery) -> None:
    await callback.message.delete()
    smth = str(callback.message.text)
    await database.add_anime(smth)
    await callback.message.answer('Добавлено', reply_markup=get_start_ikb())


@dp.callback_query(lambda callback_query: callback_query.data == 'add_serial')
async def cd_add_new_smth(callback: CallbackQuery) -> None:
    await callback.message.delete()
    smth = str(callback.message.text)
    await database.add_serial(smth)
    await callback.message.answer('Добавлено', reply_markup=get_start_ikb())


@dp.callback_query(lambda callback_query: callback_query.data == 'add_book')
async def cd_add_new_smth(callback: CallbackQuery) -> None:
    await callback.message.delete()
    smth = str(callback.message.text)
    await database.add_book(smth)
    await callback.message.answer('Добавлено', reply_markup=get_start_ikb())


async def main():
    await dp.start_polling(bot,
                           dispatcher=dp,
                           skip_updates=True)


asyncio.run(main())

