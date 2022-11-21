import re


post = '1500 3'
price = '1500'
post_clear = re.sub(f'{price}\S', f'{price}', post)  # убираем знаки после цены в посте
print(post_clear)
match = re.match('1500', post)
print(match[0])

h = [1, 4]
print(h.index(1, 0))

f = [1, 5, 6, 3]
g = f[0]
print(g, f[f.index(g)+1])

print('{}'.format('f'))

g = (1,)
a = g[0]

print(a)

g_list = []
g_list.append([1, None])
print('g_list', g_list)
