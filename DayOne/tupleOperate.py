# 元组的操作
# 元组的定义
# tupple= ("元素1", "元素2"，".......")
tupleTest = ("张三", "李四", 1,2,3)
print(tupleTest, type(tupleTest))
#tupleTest[0] = "岳云鹏"

# 元组的访问 通过 下标访问
print(tupleTest[0])
print(tupleTest[1])
print(tupleTest[2])
print(tupleTest[3])

# 查找index
print("元素1的位置是：",tupleTest.index(1))
# 如果有多个 元素的值是一样的 那么就返回 最小的 索引值


# 删除元素 报错
# del tupleTest[0]
varAddTuple = (1,2,3,4,5) + (9,9,9,9)
print(varAddTuple)

# 元素统计 count(需要统计的元素) 函数
print(varAddTuple.count(9))
# 如果有多个 元素的值是一样的 那么就返回 最小的 索引值
print(varAddTuple.index(9))
















