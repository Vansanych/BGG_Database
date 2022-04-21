import json

with open('data.txt') as json_file:
    data = json.load(json_file)
post_list = data["response"]["items"]
posts_id_list = []
i = 1
for post in post_list:
    posts_id = post["date"]
    posts_id_list.append(posts_id)
    print("post " + str(i) + "---------------------------------------")
    print(post["text"] + "\n")
    i += 1
print(posts_id_list)
