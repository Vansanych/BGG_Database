"""
filter_2 возвращает список двух первых слов из строчек поста в качестве имен игр
BNI_19_04_22[20, 44]
"""
from body.sorting_posts import sell_posts_list
import re


def filter_2(strings):
    names_list = []
    ex_list = []
    for string in strings:
        words = string.split()
        if len(words) > 1:
            if re.search(r'[0-9]', words[0]):
                words.pop(0)
            try:
                words[0] = re.sub(r'\W', '', words[0])
                words[1] = re.sub(r'\W', '', words[1])
                names_list.append([words[0], words[1]])
            except:
                ex_list.append(string)
    if ex_list:
        print('filter_3', ex_list)
    return names_list


def get_strings(post_number):
    post = sell_posts_list[post_number]
    return post.split('\n')
