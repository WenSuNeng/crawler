# coding=utf-8
import re

#pattern = re.compile('[a-zA-Z]')
#result = pattern.findall('wawakd')
pattern = re.compile('(a-zA-Z)')
result = pattern.findall('wawakd')
print result


string = "xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"
result1 = re.findall(".*entry(.*)for.*",string)
for x in result1:
    print x
