# 函数学习
# 函数的定义
# def 函数名(函数参数)：
#    函数体
#    返回值
# 无参函数
"""
def getConfigure():
    return "192.168.1.1:80"
print(getConfigure())
# 有参函数
def spaekOut(name, money):
    print("我的名字叫{}，有钱的很, 有{}亿".format(name, money))
spaekOut("Jack Ma", 100)
# 和不可变参数
# int float str 元组
def changeTest(num):
    num = 10
    print(num, id(num))
a = 20
print("a id=", id(a))
changeTest(a)
print(a)
#可变参数
# 可修改的 list 字典
def changeList(pList):
    pList[0] = 1000
    print(pList, id(pList))
testList = [1,2,3,4,56]
print("testList id", id(testList))
changeList(testList)
print(testList)
"""
# 不定长参数
# 如果我的参数前面有个* 号就表示以元组的方式传递产参数
"""
def varAgrs(a, *b):
    print("a=", a)
    print("b=", b)
    print(b[0])
    print(b[1])

varAgrs(1,2,3,4,5,6,7,8,9)
# 如果说参数前面有两个** 表示以 字典传递参数
def varDictAgrs(a, **b):
    print("a=", a)
    print("b=", b)

varDictAgrs(3, x=1, y=2, z=3)

# 默认参数
def defaultArgs(name="tony", age=18):
    print("name = {}, age= {}".format(name, age))
defaultArgs()
defaultArgs("jack ma")
defaultArgs("jack ma", 988)

#def defaultError(age=18, name): 默认参数必须在飞默认参数后面
"""
# 全局变量
# 可以在文件任何使用的变量叫全局变量 变量变面 global 就是全局变量
""""
age = 18
def testGlobal():
    global age
    age =10
    print("my age", age)

testGlobal()
print(age)
"""

# 实现max函数 max(list)
def myMax(pList):
    tmpMax = pList[0]
    for num in pList:
        if num > tmpMax:
            tmpMax = num
    return tmpMax

testList = [1,45,99,273,998,7,9,1,4,3]
print("最大的元素:",myMax(testList))

# 冒泡排序
def myBubble(pList):
    for i in range(0, len(pList) -1):#固定第一个要比较函数
        for j in range(i+1, len(pList)):# 每个元素跟第一个 元素比较
            if pList[i] > pList[j]:#交换如果比第一个元素小 则 交换位置
                tmp = pList[i]
                pList[i] = pList[j]
                pList[j] = tmp
print(myBubble(testList))
print(testList)

# [[1,2,3],[2,3,4],[1,1,1]] 按照 元素的和进行排序

