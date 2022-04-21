import json

with open('../files/BNI.json') as file:
    last_posts = json.load(file)

post_list = last_posts["response"]["items"]
print(post_list)


