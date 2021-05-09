import requests
import datetime
import lxml
import bs4


news = []
# 存放热搜的数组

hot_url = 'https://s.weibo.com/top/summary'
# 热搜链接

r = requests.get(hot_url)

bs = bs4.BeautifulSoup(r.text, 'lxml')
# 解析页面

today = datetime.date.today()
# 日期

title = bs.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')

for i in range(50):
	hot_news = {}
	# 将信息保存到字典中
	hot_news['title'] = title[i+1].get_text()
	news.append(hot_news)
	
f = open('hotrank.csv', 'a', encoding='utf-8-sig')
f.write(str(today) + ',')
for i in news:
	f.write(i['title'] + ',')
f.write('\n' + '\n')

print('OK!')


# 将上面得到的数据生成词云


#import os  
#os.environ['FONT_PATH'] = "/System/Library/fonts/PingFang.ttc"
# 使 wordcloud 支持中文

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


text_from_file_with_apath = open('hotrank.csv').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="msyh.ttf", width=1920, height=1080).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.savefig('词云图片.jpg', bbox_inches='tight', pad_inches=0, dpi=360)
#输出图片并去除白边