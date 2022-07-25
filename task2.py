"""
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита.
"""

import wikipediaapi

# кладем членов категории в список cat_members
wiki_wiki = wikipediaapi.Wikipedia('ru')
page_py = wiki_wiki.page('Категория:Животные_по_алфавиту')
cat_members = page_py.categorymembers.keys()

dict_animals = {}
for member in cat_members:
    if 'Категория' not in member: # извлекаем имена подкатегорий
        first_letter = member[0]
        if first_letter in dict_animals:
            dict_animals[first_letter] += 1
        else:
            dict_animals[first_letter] = 1

print(sorted(dict_animals))
