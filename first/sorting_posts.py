from get_list_post_text import posts_text

sell_posts_list = []
other_posts_list = []

sell_words = ['продам', 'Продам', 'ПРОДАМ']
other_words = ['куплю', 'Куплю', 'Обмен', 'аукцион']

for post_text in posts_text:
    if any(word in post_text for word in sell_words):
        sell_posts_list.append(post_text)
    elif any(word in post_text for word in other_words):
        other_posts_list.append(post_text)
    elif not post_text:
        other_posts_list.append(post_text)

if len(posts_text) == len(sell_posts_list) + len(other_posts_list):
    print("сортировка прошла успешно")
else:
    print("сортировка прошла с ошибкой")
