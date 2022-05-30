# set 学习
"""
testSet = {}# 不能 创建一个空的集合 这是一个 空的 字典
print(type(testSet))
"""
emptySet = set()
print(type(emptySet))
constructSet = {"张三", "李四", "王五", "Jack"}
print(constructSet)
#print(constructSet[0])# 会报错
# 增加
constructSet.add("pony")
print(constructSet)
# set的长度
print(len(constructSet))
# 判断是否存在某个元素
print("pony" in constructSet)
print("pony123" in constructSet)

# set自动去重
numSet = {1,1,1,1,1,5,5,5,6,6,6,7,1,2,3,9,10}
print(numSet)

# 列表去重
numList = [1,1,1,1,1,5,5,5,6,6,6,7,1,2,3,9,10]
tmpNumSet = set(numList)# list->set 自动去重
tmpNumList = list(tmpNumSet)# 去重后的set -> list
print(tmpNumList, type(tmpNumList))

#输入 [183,0,1,2,-184,367] 求这个 列表中两个元素相加和为183 的所有元素对 {(183,0),(-184,367)}
parList = [183,0,1,2,-184,367]
resSet = set()
for i in range(0, len(parList)):
    for j in range(0, len(parList)):
        if parList[i] + parList[j] == 183:
            oneRes = (parList[i], parList[j])
            twoRes = (parList[j], parList[i])
            if not (oneRes in resSet or twoRes in resSet):
                resSet.add(oneRes)
print(resSet)













