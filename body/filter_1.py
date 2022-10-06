"""
filter_1 возвращает список первых слов из строчек поста в качестве имен игр
BNI_19_04_22[23]
"""
from sorting_posts import sell_posts_list
import re


def filter_1(strings):
    for string in strings:
        words = string.split()
        if re.search(r'\W|[0-9]', words[0]):
            words.pop(0)
        if len(words) > 1:
            if re.search(r'\W', words[0]):
                words[0] = words[0][:-1]
            names_list.append(words[0])
    return names_list


post_number = 23
post = sell_posts_list[post_number]
post = post.replace('\n \n', '\n')
post = post.replace('\n \n', '\n')
strings = post.split('\n')
names_list = []

print(filter_1(strings))
