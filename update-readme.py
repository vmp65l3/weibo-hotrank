from datetime import datetime, timedelta

utctime = datetime.utcnow()

bjtime = utctime + timedelta(hours=8)

bjtime = bjtime.strftime('%Y-%m-%d-%H-%M')



f = open('README.md', 'a')
f.write('\n' + '##' + ' ' + str(bjtime) + '\n' + '![image text](https://github.com/vmp65l3/weibo-hotrank/blob/master/fig/' + str(bjtime) + '.jpg)' + '\n')
