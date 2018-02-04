# coding: utf-8

from bs4 import BeautifulSoup
import re
import sys  
 
# ascii编码问题
reload(sys)  
sys.setdefaultencoding('utf8')

html_doc = '''
	<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <a href="test1.org">t</a>
  <a href="regtest.org">reg</a>
  <div class="className">获取text</div>
</body>
</html>
'''

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print '获取所有a标签'
all_a_node = soup.find_all('a')
for a in all_a_node:
	print a.name, a['href'], a.get_text()

print '获取某一个a标签'
a_link = soup.find('a', href='test1.org')
print a_link.name, a_link['href'], a_link.get_text()

print '正则匹配'
reg_a_node = soup.find('a', href=re.compile(r'reg'))
print reg_a_node

print '获取className'
div = soup.find('div', class_='className')
print div.name, div.get_text()