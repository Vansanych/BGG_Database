1.TeseraTop1000 получает json-файлы по 15 игр из Топ Тесеры
и складывает файлы json в папку TeseraTop5000

2. body\fromTop15toTop900
Объединяет файлы по 15 игр в один файл
и складывает в файл TopList/Top5000.json

3. body\fill_missing_keys
Заполняет словарь недостающими парами
меняет ё на е, 'Аркхэм' на 'Аркхем'
и записывает в файл TopList/Top5000_2.json

4. SQL\SQL_Top_Tesera3
Создает базу игр по ТОП Тесеры (без дубликатов)
/filters/Tesera_Top5000_1.db

read_json модуль забирает первое слово из названия игры Тесеры.
Полные названия игр в json-файлах по 15 игр с Топ Тесеры.
JSON-файлы формируются в модуле TeseraTop1000.
Формирует словарь первых слов из названий игр на русском

filter_2 возвращает список первых слов из строчек поста в качестве имен игр
BNI_19_04_22[20, 44]

и т.д.
