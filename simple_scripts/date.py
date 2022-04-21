from datetime import datetime
ts = int("1650259356")
print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
