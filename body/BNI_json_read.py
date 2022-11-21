import json

with open('../files/BNI_19_04_22.json') as file:
    last_posts = json.load(file)

post_list = last_posts["response"]["items"]
if __name__ == '__main__':
    print('id:', post_list[2]['id'])
    print('date', post_list[2]['date'], '\n')
    print(post_list[2]['text'])
