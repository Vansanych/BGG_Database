from get_list_post_text import posts_text

sell_posts_list = []
buy_posts_list = []
auction_posts_list = []
empty_posts_list = []
change_posts_list = []

counter = 0

for post_text in posts_text:
    if 'продам' in post_text:
        sell_posts_list.append(post_text)
    elif 'Продам' in post_text:
        sell_posts_list.append(post_text)
    elif 'ПРОДАМ' in post_text:
        sell_posts_list.append(post_text)
    elif 'куплю' in post_text:
        buy_posts_list.append(post_text)
    elif 'Куплю' in post_text:
        buy_posts_list.append(post_text)
    elif 'Обмен' in post_text:
        change_posts_list.append(post_text)
    elif 'аукцион' in post_text:
        auction_posts_list.append(post_text)
    elif not post_text:
        empty_posts_list.append(post_text)
    counter += 1

if len(posts_text) == len(sell_posts_list) + len(buy_posts_list) + len(auction_posts_list) + \
        len(empty_posts_list) + len(change_posts_list):
    print("сортировка прошла успешно")
else:
    print("сортировка прошла с ошибкой")

print(len(sell_posts_list))
print(len(sell_posts_list) + len(buy_posts_list) + len(auction_posts_list) + len(empty_posts_list)
     + len(change_posts_list))
