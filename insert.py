from psycopg import connect
from dotenv import load_dotenv
from os import getenv
from random import randint

load_dotenv()

creds = (
    ('host', 'PG_HOST'),
    ('port', 'PG_PORT'),
    ('user', 'PG_USER'),
    ('password', 'PG_PASSWORD'),
    ('dbname', 'PG_DBNAME')
)

creds = {var: getenv(env_var) for var, env_var in creds}

connection = connect(**creds)
cursor = connection.cursor()

# genres = (
#     ('fiction', 'students doing their homeworks just in time'),
#     ('fantasy', 'made up nonsense'),
#     ('detective', 'trying to find out how students homework works'),
#     ('horror', 'students setup.cfg.'),
# )

# for genre_info in genres:
#     cursor.execute('INSERT INTO library.genre (name, description) VALUES (%s, %s)', genre_info)

select_books = 'SELECT id FROM library.book'
cursor.execute(select_books)
books_ids = cursor.fetchall()
select_genre = 'SELECT id FROM library.genre'
cursor.execute(select_genre)
genres_ids = cursor.fetchall()

insert_link = 'INSERT INTO library.book_genre (book_id, genre_id) VALUES (%s, %s)'

for book_id in books_ids:
    book_id = book_id[0]
    genres = [genre[0] for genre in genres_ids]
    for _ in range(randint(1, 3)):
        cursor.execute(insert_link, (book_id, genres.pop(randint(0, len(genres)-1))))

connection.commit()
