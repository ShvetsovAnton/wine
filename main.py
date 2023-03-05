import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def calculate_difference_years():
    foundation_year = 1920
    current_year = datetime.datetime.now()
    past_year = current_year.year - foundation_year
    if (past_year % 10 == 1) and (past_year != 11) and (past_year != 111):
        suffix = 'год'
    elif (past_year % 10 > 1) and (past_year % 10 < 5) \
            and (past_year != 12) and (past_year != 13) \
            and (past_year != 14):
        suffix = 'годa'
    else:
        suffix = 'лет'
    return past_year, suffix


def take_categories(excle_file_name):
    categories = defaultdict(list)
    category_rows = []
    categories_tabel = pandas.read_excel(excle_file_name).fillna(
        '', inplace=False
    )
    unique_drinks_categories = categories_tabel.Категория.unique()
    for drink_category in unique_drinks_categories:
        category_rows.append(
            categories_tabel[categories_tabel.Категория == drink_category]
        )
    for rows_indexes in category_rows:
        for row_index in rows_indexes.index:
            category_name = rows_indexes.loc[[row_index]].Категория[row_index]
            drink_name = rows_indexes.loc[[row_index]].Название[row_index]
            drink_sort = rows_indexes.loc[[row_index]].Сорт[row_index]
            drink_price = rows_indexes.loc[[row_index]].Цена[row_index]
            drink_image = rows_indexes.loc[[row_index]].Картинка[row_index]
            categories[category_name].append(
                {
                    'Название': drink_name,
                    'Сорт': drink_sort,
                    'Цена': drink_price,
                    'Картинка': drink_image
                }
            )
    return categories


prices = []
categories = take_categories('wine3.xlsx')
for category, descriptions in categories.items():
    for description in descriptions:
        prices.append(description['Цена'])
promotional_price = min(prices)


past_year, suffix = calculate_difference_years()
rendered_page = template.render(
    past_year=str(past_year),
    suffix=suffix,
    promotional_price=promotional_price,
    categories=take_categories('wine3.xlsx')
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()


