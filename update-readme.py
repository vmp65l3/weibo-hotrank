
import datetime
today = datetime.date.today()
f = open('README.md', 'a')
f.write('\n' + '##' + ' ' + str(today) + '\n' + '![image text](https://github.com/vmp65l3/weibo-hotrank/blob/master/' + str(today) + '.jpg)' + '\n')
