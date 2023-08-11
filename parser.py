# picked up from
# https://github.com/gil9red/SimplePyScripts/blob/2c6306c575f58d5ee970c70a690a2ad46ba6c928/parse_en_ru_words/www.7english.ru_dictionary.php_id=2000_letter=all/main.py#L18

import json

import requests
from bs4 import BeautifulSoup

from config import source_filename, site_words_url

rs = requests.get(site_words_url)
root = BeautifulSoup(rs.content, 'html.parser')

en_ru_items = []

for tr in root.select('tr[onmouseover]'):
    td_list = [td.text.strip() for td in tr.select('td')]

    # Количество ячеек в таблице со словами -- 9
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue

    en = td_list[1]

    # Русские слова могут быть перечислены через запятую 'ты, вы',
    # а нам достаточно одного слова
    # 'ты, вы' -> 'ты'
    ru = td_list[5]

    en_ru_items.append((en, ru))

file_handler = open(source_filename, 'w+')
json.dump(en_ru_items, file_handler)
file_handler.close()
