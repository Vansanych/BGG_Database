# a = "123456"
# b = a.replace('1', '')
# print(b)

# v = "[string \n string]"
# h = v.split('\n')
# print(h)

import re

r = re.findall('(\d+)', '9. Тайный город - карточная игра по мотивам фентези произведений в современном мире '
                        'Вадима Панова, б/у, угол коробки немного повреждён, компоненты в отличном состоянии, '
                        'карты в протекторах - 600 руб.')
print(r)

post = ['#БНИ_ПродамБУ_Новосибирск', '#БНИ_ПродамНовая_Новосибирск', '#БНИ_Почта', '#БНИ_zuzubun (+ещё игры по тегу)',
     '', '1. Age of Conan (Эра Конана) + кикстартер дополнение Adventures in Hyperborea с бонусами предзаказа '
         '- большая стратегическая игра с миниатюрами в сеттинге произведений Роберта Говарда про варвара из Киммерии, '
         'новые, в плёнке, у базы немного повреждён один угол, база - русский, дополнение - английский язык, 7500 руб.',
     '', '2. Маленький принц - семейная (но с довольно активным взаимодействием) игра на тему знаменитой сказки '
         'Экзюпери, в которой игроки составляют свои планеты из тайлов, французский язык, языконезависимая, коробка '
         'с небольшими потёртостями, компоненты в отличном состоянии - 900 руб.',
     '', '3. Micro Mutants: Evolution - игра на ловкость и координацию с юмористической темой про насекомых, немецкий '
         'язык, распечатаны правила на русском, не играна ни разу, компоненты в отличном состоянии - 900 руб.', '',
     '4. T.I.M.E Stories (Агентство «ВРЕМЯ») - приключенческая игра со сценариями про героических путешественников во'
     ' времени, б/у, английский язык, коробка с потёртостями, в хорошем состоянии - 900 руб.', '',
     '5. Locke & Key - карточная игра с рисунками из комиксов Джо Хилла, сына Стивена Кинга, б/у, английский язык, '
     'коробка потёрта, компоненты в отличном состоянии, карты в протекторах - 700 руб.', '',
     '6. Королевский двор - семейная карточная игра от известных авторов, б/у, в отличном состоянии, часть жетонов '
     'не выдавлена, карты в протекторах - 450 руб.', '',
     '7. Настолье - развитие идеи традиционной щелчковой игры в "Чапаева", б/у, русский язык, в отличном состоянии, '
     'часть наклеек не наклеены, карты в протекторах - 700 руб.', '',
     '8. Звёздные врата - игра в сеттинге известного одноимённого фантастического сериала, б/у, коробка повреждена и '
     'потёрта, компоненты в хорошем состоянии (стоит учесть, что изначальное качество не самое лучшее) - 1000 руб.', '',
     '9. Тайный город - карточная игра по мотивам фентези произведений в современном мире Вадима Панова, б/у, угол '
     'коробки немного повреждён, компоненты в отличном состоянии, карты в протекторах - 600 руб.', '',
     '10. Да, Темный Властелин! - юмористическая пати игра про Тёмного Властелина и его миньонов, б/у, коробка немного'
     ' повреждена и потёрта, карты в хорошем состоянии - 350руб.', '',
     'Продаю предпочтительно в Новосибирске, но могу и отправить транспортной компанией или почтой. С покупателя '
     'полная предоплата на карту Сбербанка за игру и пересылку.']
posts = []
for position in post:
    integers = re.findall('(\d+)', position)
    for integer in integers:
        if int(integer) > 100:
            price = integer
            # print(price)
            if integers:  # if integers !=[]:
                string = position
                for i in string:
                    if not i.isalpha() and i != ' ':
                        string = string.replace(i, '')
                first_word = string.split()[0] + ' ' + string.split()[1]
                # print(first_word)
                # print(position)
                posts.append([first_word, price, position])
print(posts)
