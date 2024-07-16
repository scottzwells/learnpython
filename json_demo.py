"""
演示JSON数据和Python字典的相互转换
"""

import json
data = [{"name":"张大山","age":11},{"name":"John","age":13},{"name":"王大锤","age":18}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

s= json.loads(json_str)
print(type(s))
print(s)

x= '[{"name":"张大山","age":11},{"name":"John","age":13},{"name":"王大锤","age":18}]'
print(json.loads(x))