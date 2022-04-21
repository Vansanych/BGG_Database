import json

with open('BNI_19_04_22.json') as file:
    last_posts = json.load(file)

post_list = last_posts["response"]["items"]


