#coding:utf-8
#简单的豆瓣爬虫程序
#Python2.7
import requests
from lxml import html

url='https://movie.douban.com/' #this is the target
page=requests.session().get(url)
tree=html.fromstring(page.text)

#<td class="title">
# <a onclick="moreurl(this, {from:'mv_rk'})" href="https://movie.douban.com/subject/4920389/">头号玩家</a></td>

result=tree.xpath('//td[@class="title"]//a/text()')#根据想要的内容，建议正确的正则公式


a=[]
a=result

for b in a:
    print b.encode('utf-8')##默认是ascII，不这样写中文可能会乱码

#输出获得的数据到一个TXT
fout=open('result.txt','w')
for b in a:
    fout.write('%s' % b.encode('utf-8'))
fout.close()
