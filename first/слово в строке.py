# import re
string = '.... 10  пример один, строки'
# integer = re.findall('\\d+', string)
# pattern2 = re.compile('\\w+')
# word = pattern2.findall(string)
#
# print("word", word)
# print(integer)
#
# first_word = next(m.group() for m in re.finditer(r'\w+', string))
# print(first_word)
# word_my = re.findall('\\D+', string)
# print("word_my", word_my)
#
# ddd = pattern2.search(string).group()
# print(ddd)

for i in string:
    if not i.isalpha() and i != ' ':
            string = string.replace(i, '')
first_word = string.split()[0]

print("first_word: ", first_word)
