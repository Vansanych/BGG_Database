import json

with open('../files/BNI_25_04_22.json') as file:
    last_posts = json.load(file)

post_list = last_posts["response"]["items"]


