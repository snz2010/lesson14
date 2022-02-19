import sqlite3

DB_FILE = "data/netflix.db"

# 1. Поиск по названию
def search_film(search_txt):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    search_string = f"AND `title` LIKE '%{search_txt}%' "
    query = """
        SELECT `title`, `country`, `release_year`, `listed_in`, `description`, `show_id` FROM netflix
        WHERE `type` = 'Movie'
        """ + search_string + """
        ORDER BY `release_year` DESC
        LIMIT 1
        """
    cur.execute(query)
    result = cur.fetchall()
    film_found = {}
    for item in result:
        film_found["title"] = item[0]
        film_found["country"] = item[1]
        film_found["release_year"] = item[2]
        film_found["listed_in"] = item[3]
        film_found["description"] = item[4]
        film_found["show_id"] = item[5]
    return film_found


# 2. Поиск по годам выпуска
def from_to(min_year, max_year):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    min_year = int(min_year)
    max_year = int(max_year)
    search_string = f"AND `release_year` >= {min_year} AND `release_year` <= {max_year} "
    query = """
        SELECT `title`, `release_year` FROM netflix
        WHERE `type` = 'Movie'
        """ + search_string + """
        ORDER BY `release_year`
        LIMIT 100
        """
    cur.execute(query)
    result = cur.fetchall()
    film_found = {}
    films = []
    for item in result:
        film_found["title"] = item[0]
        film_found["release_year"] = item[1]
        films.append(film_found)
        film_found = {}
    return films

# 3. Поиск по рейтингу
def get_rating(rating):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    if rating == 'children':
        search_string = f"AND `rating` LIKE 'G' "
    elif rating == 'family':
        search_string = f"AND `rating` LIKE '%G%' "
    elif rating == 'adult':
        search_string = f"AND `rating` LIKE 'NC-17' OR `rating` LIKE 'R' "
    else:
        return []
    query = """
        SELECT `title`, `rating`, `description` FROM netflix
        WHERE `type` = 'Movie'
        """ + search_string + """
        ORDER BY `rating`
        LIMIT 100
        """
    cur.execute(query)
    result = cur.fetchall()
    film_found = {}
    films = []
    for item in result:
        film_found["title"] = item[0]
        film_found["rating"] = item[1]
        film_found["description"] = item[2]
        films.append(film_found)
        film_found = {}
    return films


# 4. Поиск по жанру
def get_genre(genre):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    search_string = f"WHERE `type` = '{genre}' "
    query = """
        SELECT `title`, `description`, `release_year` FROM netflix
        """ + search_string + """
        ORDER BY `release_year` DESC
        LIMIT 10
        """
    cur.execute(query)
    result = cur.fetchall()
    film_found = {}
    films = []
    for item in result:
        film_found["title"] = item[0]
        film_found["description"] = item[1]
        films.append(film_found)
        film_found = {}
    return films


# 6. Поиск по типу картины (фильм или сериал), году выпуска и ее жанру
def by_type_year_listed(m_genre, m_year, m_listed):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    search_string = f"WHERE `type` = '{m_genre}' AND `release_year` = '{m_year}' AND `listed_in` LIKE '%{m_listed}%' "
    query = """
         SELECT `title`, `description`, `listed_in` FROM netflix
         """ + search_string + """
         LIMIT 40
         """
    cur.execute(query)
    result = cur.fetchall()
    film_found = {}
    films = []
    for item in result:
        film_found["title"] = item[0]
        film_found["description"] = item[1]
        films.append(film_found)
        film_found = {}
    return films


# 5. Поиск CAST по именам 2х актеров
def by_2names(name1, name2):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    search_string = f"WHERE `cast` LIKE '%{name1}%' AND `cast` LIKE '%{name2}%' "
    query = """
        SELECT `title`, `cast` FROM netflix
        """ + search_string + """
        """
    cur.execute(query)
    result = cur.fetchall()
    films = []
    for item in result:
        films.append(item[1])
    return films