#字典操作
# 字典的定义
# 定义一个空字典
emptyDic = {}
print(type(emptyDic))
# 字典元素的定义 {key:vale, key:value}
person = {"ID":9527, "name":"岳云鹏","age":18}
print(person)
# 字典的访问
print(person["ID"])
print(person["name"])
# 获取 所有的key值
print(person.keys())
# 获取所有的value 值
print(person.values())

for key, value in person.items():
    print("key={}  value={}".format(key, value))

# 增加元素
person["婚姻"] = "已婚"
print(person)
# 查询
print("name" in person)
# 修改某个元素
person["age"] = 88
print(person)
# 删除
del person["婚姻"]
print(person)

# 通过value 寻找key
"""
personValues = list(person.values())# value的list
personKeys = list(person.keys()) # key list
tmpInx = personValues.index("岳云鹏")# value的索引
print(personKeys[tmpInx])# 找到了 key

kpi = {"jackma":3.25, "pony":3.5, "岳云鹏":100, "郭德纲": 60}
maxKpi= {key:value for key, value in kpi.items() if value == max(list(kpi.values()))}
print(maxKpi)

reverseKpi = {value:key for key, value in kpi.items()}
print(reverseKpi)
"""

# 字典嵌套
dicMore = {"name":"jack","cars":{"奔驰":10, "宝马":30}, "money": "不知道多少"}
print(dicMore)







