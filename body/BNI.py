"""https://oauth.vk.com/authorize?client_id=5490057&display=page&redirect_uri=https:
//oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52
"""
import requests

token = "79ad5ce9a9ac8da0b5b301bee4f6195bb3350de41ad71a56a555f39cb1de21e5459676965216297336607"
url = f"https://api.vk.com/method/wall.get?domain=baraholkanastolok&count=10&access_token={token}&v=5.131"
req = requests.get(url)
t = req.json()
post_list = t["response"]["items"]
list_main = []
i = 0
for post in post_list:
    list_main.append([post["id"], post["date"], post["text"]])
    i += 1

print(post)
print(i)
print(list_main[0])
print(list_main[1])



