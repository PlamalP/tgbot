import sqlite3 as sq


global db, cur


async def db_connect():
    global db, cur

    db = sq.connect("media.db")
    cur = db.cursor()
    print('Подключение к базе данных выполнено успешно')
    db.commit()


async def get_all_films():
    films = cur.execute("SELECT title FROM content WHERE type = 'фильм';").fetchall()
    return films


async def get_all_anime():
    anime = cur.execute("SELECT title FROM content WHERE type = 'аниме';").fetchall()
    return anime


async def get_all_serials():
    serials = cur.execute("SELECT title FROM content WHERE type = 'сериал';").fetchall()
    return serials


async def get_all_books():
    books = cur.execute("SELECT title FROM content WHERE type = 'книга';").fetchall()
    return books


async def add_film(title, mtype='фильм'):
    cur.execute("insert into content (title, type) values (?, ?)", (title, mtype))
    db.commit()


async def add_anime(title, mtype='аниме'):
    cur.execute("insert into content (title, type) values (?, ?)", (title, mtype))
    db.commit()


async def add_serial(title, mtype='сериал'):
    cur.execute("insert into content (title, type) values (?, ?)", (title, mtype))
    db.commit()


async def add_book(title, mtype='книга'):
    cur.execute("insert into content (title, type) values (?, ?)", (title, mtype))
    db.commit()





