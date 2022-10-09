from filter_2 import names_list

exceptions = ['Пост', 'Незнаю', 'Цена', 'Варгейм', 'цену', 'Фишечнокарточный', 'Продам', 'Доп', 'Дополнение', 'Цена', 'Доставка']

for name in names_list:
    if name in exceptions:
        pass
