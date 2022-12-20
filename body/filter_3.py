"""
Возвращает список двух первых слов из строчек поста в качестве имен игр
"""

from body.sorting_posts import sell_posts_list, sell_posts_dict
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
    return names_list


def filter_22(strings):
    names_list = []
    ex_list = []
    for string in strings:
        string = re.sub(r'["()+.\-:]', '', string)
        name_list = []
        words = string.split()
        if len(words) > 1:
            if re.search(r'[0-9]', words[0]):
                words.pop(0)
            try:
                for word in words:
                    name_list.append(word)
            except:
                ex_list.append(string)
            names_list.append(name_list)
    # print(names_list)
    return names_list


def get_strings(post_number):
    post = sell_posts_list[post_number]
    return post.split('\n')


def get_strings_from_dict(post):
    return post.split('\n')


if __name__ == '__main__':
    for i in range(len(sell_posts_list)):
    # for i in range(2, 3):
        # print('strings', (get_strings(i)))
        names = filter_22(get_strings(i))
        print(i, names, '\n')
        # print('\n', sell_posts_list[2])
