from body.get_list_post_text import posts_text

sell_posts_list = []
other_posts_list = []

sell_words = ['продам', 'Продам', 'ПРОДАМ']
other_words = ['куплю', 'Куплю', 'Обмен', 'аукцион']

counter = 0
counter2 = 0

for post_text in posts_text:
    if any(word in post_text for word in sell_words):
        sell_posts_list.append(post_text)
        counter2 += 1
    elif any(word in post_text for word in other_words):
        other_posts_list.append(post_text)
        counter2 += 1
    elif not post_text:
        other_posts_list.append(post_text)
        counter2 += 1
    counter += 1
    if counter2 != counter:
        print(f"при сортировке поста {counter} произошла ошибка")
        counter2 = counter
