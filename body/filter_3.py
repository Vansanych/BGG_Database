"""
filter_2 возвращает список двух первых слов из строчек поста в качестве имен игр
BNI_19_04_22[20, 44]
"""
from sorting_posts import sell_posts_list
import re


def filter_2(strings):
    names_list = []
    for string in strings:
        words = string.split()
        if len(words) > 1:
            print(words)
            if re.search(r'[0-9]', words[0]):
                words.pop(0)
            try:
                words[0] = re.sub(r'\W', '', words[0])
                words[1] = re.sub(r'\W', '', words[1])
                names_list.append([words[0], words[1]])
            except Exception as ex:
                print(ex, ' - after delete digits in words')
    return names_list


def get_strings(post_number):
    post = sell_posts_list[post_number]
    print(post)
    return post.split('\n')


# names = filter_2(get_strings(1))
# print(names)
