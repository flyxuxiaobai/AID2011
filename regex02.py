"""
re 模块使用 2
"""
import re

string = "Alex:1996,Sunny:1998"

# result = re.match("\w+", string)
# print(result.group())

#group可以传参数
# result = re.search("(\w+):(?P<year>\d+)", string)
# print(result.group(1))


result = re.finditer("\w+", string)
print(result)
#
# #迭代取值 获取每次匹配内容的match对象
for item in result:
    print("匹配内容:", item.group())
    print("匹配位置:", item.span())
