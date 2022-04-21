from BNI_json_read import post_list
from datetime import datetime

posts_date_start = post_list[0]['date']
posts_date_end = post_list[-1]['date']

start = int(posts_date_start)
print(datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'))

end = int(posts_date_end)
print(datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S'))
