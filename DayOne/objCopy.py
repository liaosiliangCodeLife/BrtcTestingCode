# 对象的拷贝
aList = ["a", "b", "c", "d"]
bList = aList
"""
print("aList = ", aList)
print("bList = ", bList)
aList[1] = "z"
print("aList = ", aList)
print("bList = ", bList)
"""
# 浅拷贝， 只 拷贝 对象的地址
print(id(aList), id(bList))

cList = [1,2,3,4,5]
dList = cList
print(id(cList), id(dList))

# 深拷贝 .copy() 函数 
fList = ["a", "b", "c", "d"]
gList = fList.copy()
print("修改前:" , fList)
print("修改前:" , gList)
gList[0] = "Z"
print("修改后:" , fList)
print("修改后:" , gList)

print("fList的地址:", id(fList))
print("gList的地址:", id(gList))

print("fList[1]的地址:", id(fList[1]))
print("gList[1]的地址:", id(gList[1]))

# 多维 列表 深拷贝要 层层递进

hList = [[1,2,3],
         [4,5,6]]
iList = hList.copy()

print("修改前:",hList)
print("修改前:",iList)

hList[0][0] = [1000]

print("修改后:",hList)
print("修改后:",iList)

print("hList地址:", id(hList))
print("iList地址:", id(iList))

print("hList[0]地址:", id(hList[0]))
print("iList[0]地址:", id(iList[0]))

iList[0] = hList[0].copy()
iList[1] = hList[1].copy()
print("修改前:",hList)
print("修改前:",iList)
hList[0][0] = 9999
print("修改后:",hList)
print("修改后:",iList)














