from sorting_posts import sell_posts_list
import re

post = sell_posts_list[9]
print(post)
positions = post.split('\n\n')

for position in positions:
    integers = re.findall('(\d+)', position)
    if integers:
        for integer in integers:
            if int(integer) < 100:
                    position = position.replace(integer, '', 1).replace('.', '', 1)
            else:
                if int(integer) < 100000:
                    price = integer
                    print(price)
                    step1 = position.split('\d+')
                    for step2 in step1:
                        list_from_position = step2.split('"')
                        print("name2", list_from_position[0])

