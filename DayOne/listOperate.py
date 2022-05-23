#  列表操作
"""
# varList
varList = ["岳云鹏", "吴彦祖", 3.14359, True, 37]
print(varList, len(varList))

# 列表的访问
# 下标访问
print(varList[0])
print(varList[4])
# 异常访问
#print(varList[5])

# 追加
varList.append("于一饭")
print(varList, len(varList))


# 截取访问list[开始的元素坐标:取到最后但不包括:间距]
print("第一次截取:",varList[0:3:2])

#print("第二次截取:",varList[0::])
#print(dir(varList))

# 列表翻转
varList.reverse()
print(varList)



# 二维列表
varTwo = [[1,2,3],
          [4,5,6]]
print(varTwo[1][2])

# 求最大值
varListInt = [3,4,6,11,77,118]
print(max(varListInt))

# 求最小值
print(min(varListInt))

# appnend()

# 删除列表元素
del varListInt[0]
print(varListInt)

# 修改元素 通过下标修改
varListInt[0] = 1000
print(varListInt)

# 查找某个元素是否存在列表中
# 方法1 in 关键字
print(1000 in varListInt)

# 通过insert 插入元素
varListInt.insert(0, 333377)
print(varListInt)

# 方法二 index函数 如果存在则返回索引值 不存在 报错
#print(varListInt.index(67))# 报错
repeatList = [1,1,1,3,33,4,4,4,6]

# 重复的元素返回的是第一个元素的索引值
print("重复元素索引返回:",repeatList.index(4))

# 排序 升序排列
varListInt.sort()
print(varListInt)

# 降序
varListInt.reverse()
print(varListInt)
"""
"""
listTest = [11,22,33,44,55,66]
print(listTest[0])
print(listTest[1])
print(listTest[2])
print(listTest[3])
print(listTest[4])
# index函是你要查找的元素
print("元素55 的索引值是：",listTest.index(55))
"""





































