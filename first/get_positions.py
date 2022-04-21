from sorting_posts import sell_posts_list
import re

post = sell_posts_list[1]
print(post)
positions = post.split('\n')

for position in positions:
    integers = re.findall('(\d+)', position)
    if integers:
        print(integers)
        name = position.split('-')
        print(name[0])
