from urllib import request
import re
import chardet
html=request.urlopen("http://www.163.com").read()
html2=html.decode('gbk')
# encode_type=chardet.detect(html)
# print(encode_type)
# html1=html.decode('gbk')
# htm2=html1.encode('utf-8')
# html2=html.decode('utf-8')
# print(html
# encode_type=chardet.detect(html)
# html2=html.decode(encode_type['encoding'])

# print(encode_type)
# print(html)
title=re.findall(r'<title>(.*?)</title>',html2)
print(title)
# html1=html.decode('gbk')
# print(html1)
