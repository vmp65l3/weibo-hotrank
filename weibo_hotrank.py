import requests
import datetime
from bs4 import BeautifulSoup


today = datetime.date.today()
# 日期

news = []
# 存放热搜的数组

hot_url = 'https://s.weibo.com/top/summary'
# 热搜链接

r = requests.get(hot_url)

bs = BeautifulSoup(r.text, 'lxml')
# 解析页面

title = bs.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')

for i in range(10):
	hot_news = {}
	# 将信息保存到字典中
	hot_news['title'] = title[i+1].get_text()
	news.append(hot_news)
	
f = open('hot.csv', 'a', encoding='utf-8-sig')
f.write(str(today) + ',')
for i in news:
	f.write(i['title'] + ',')
f.write('\n' + '\n')

print('OK!')