"""https://oauth.vk.com/authorize?client_id=5490057&display=page&redirect_uri=https:
//oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52
"""
import requests
import re

token = "79ad5ce9a9ac8da0b5b301bee4f6195bb3350de41ad71a56a555f39cb1de21e5459676965216297336607"
url = f"https://api.vk.com/method/wall.get?domain=baraholkanastolok&count=10&access_token={token}&v=5.131"
req = requests.get(url)
t = req.json()
post_list = t["response"]["items"]
list_main = []
counter = 1
for post in post_list:
    posts = []
    spl_text = post["text"].split('\n')
    for position in spl_text:
        integers = re.findall('(\d+)', position)
        for integer in integers:
            if int(integer) > 100 and int(integer) < 50000:
                price = integer
                print(price)

        if integers:  # if integers !=[]:
            string = position
            for i in string:
                if not i.isalpha() and i != ' ':
                    string = string.replace(i, '')
            try:
                first_word = string.split()[0] + ' ' + string.split()[1]
            except:
                pass
            posts.append([first_word, position])
    print("posts", posts)
    list_main.append([post["id"], post["date"], posts])
    print(counter)
    counter += 1

print(list_main[8])
print(list_main[9])



