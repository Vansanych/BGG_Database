from BNI_json_read import post_list

posts_text = []
for post in post_list:
    posts_text.append(post['text'])

