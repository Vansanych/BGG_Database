"""
Создает словарь игр с датой и ID
"""

from body.BNI_json_read import post_list
from datetime import datetime

posts_text = []
post_dict = {}

for post in post_list:
    posts_text.append(post['text'])
    datestamp = post['date']
    date = datetime.fromtimestamp(datestamp)
    post_dict[post['id']] = [date, post['text']]

# print([i for i in post_dict.keys()][23])
# print(post_dict[[i for i in post_dict.keys()][23]][0])
# print(post_dict[[i for i in post_dict.keys()][23]][1])

