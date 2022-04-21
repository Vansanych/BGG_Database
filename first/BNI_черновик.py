
import requests
import json

token = "79ad5ce9a9ac8da0b5b301bee4f6195bb3350de41ad71a56a555f39cb1de21e5459676965216297336607"
url = f"https://api.vk.com/method/wall.get?domain=baraholkanastolok&count=5&access_token={token}&v=5.131"
req = requests.get(url)
t = req.json()
print(t)
post_list = t["response"]["items"]
posts_id_list = []
post_text_list = []
i = 1
list_main = []
for post in post_list:
    posts_id = post["id"]
    posts_id_list.append(posts_id)
    post_text_list.append(post["text"])
    # print("post " + str(i) + "---------------------------------------")
    # print(post["text"]+"\n")
    list_main.append([posts_id, post["text"]])
    i += 1


