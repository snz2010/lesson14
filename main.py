from pprint import pprint

# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------

from utils import by_type_year_listed, by_2names
from app import app

def main():
    # 5 Поиск по именам 2х актеров
    cast = by_2names('Rose McIver', 'Ben Lamb')
    #cast = by_2names('Jack Black', 'Dustin Hoffman')
    if len(cast) > 2:
        my_array = []
        for item in cast: # создаем множества
            my_list = item.split(', ')
            my_set = set(my_list)
            my_array.append(my_set)
        # ищем пересечения
        a = my_array[0].intersection(my_array[1])
        b = my_array[1].intersection(my_array[2])
        c = a.intersection(b)
        print("Играют в паре больше 2 раз:", c)
    else:
        print("Никто не играет с ними в паре больше 2 раз")

    # 6 Поиск по типу картины (фильм или сериал), году выпуска и ее жанру
    pprint(by_type_year_listed('Movie', 2010, 'Comedies'))
    # pprint(by_type_year_listed('TV Show', 2015, 'Kids'))
    return 0


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
    #main()
