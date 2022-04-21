import re
g = "990"
if re.findall('\d+[9]', g):
    print(g)

k = 50
if k % 10 == 0:
    print(k)

s = 60
if 5 < s < 100 and s % 10 == 0:
    print(s)
else:
    print(f"{s} не удовлетворяет условиям проверки")
d = "990"
