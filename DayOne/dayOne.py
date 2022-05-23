# 输出
"""
print("print hello!!")


# 变量
years = 18
name = "小廖"

print(name)
print(years)

# 版本一
print("我的名字叫{}， 今年{}".format(name, years))

# 版本二
print("我的名字叫：", name , "今年", years, "岁！！")

# 练习 a=5 b=7, 交换 a = 7 b =5 的值
# 方法一
"""
"""
a=5
b=7
print("a=", a, "b=", b)
c=a
a=b
b=c
print("a=", a, "b=", b)
"""

# 方法二
"""
a=5
b=7
print("a=", a, "b=", b)
a = a+b
b = a-b
a = a-b
print("a=", a, "b=", b),
"""

"""a,b,c,d =1,2,3,4
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))

# 输入
name = input("请输入你的名字：")
print("我的名字叫：", name)
"""
# 数据类型
"""
a = 5
print("a的类型是:",type(a))

b= "吴彦祖"
print("b的类型是:",type(b))

f = 3.141596
print("f的类型是:",type(f))

g = True
print("g的类型是:", type(g))


n = None
#print(id(k), "K的类型是:", type(k))
print(id(n),"N的类型是:", type(n))


# str - > int
numStr = "1234"
print("numStr 的类型是：", type(numStr))
numInt = int(numStr)
print(numInt, type(numInt))
# 异常转换
"""
"""
errorStr = "dhjdjdsh"
errorInt = int(errorStr)# 报错
"""

# int - > str
numTwo = 1234
print("numTwo 的类型是:", type(numTwo))
strTwo = str(numTwo)
print("strTwo 的类型是:", type(strTwo), strTwo)

# float -str
fTwo = 3.141596
srtTree = str(fTwo)
print("srtTree 的类型是:", type(srtTree), srtTree)

# str --> float
strFour = "1.14"
fThree = float(strFour)
print("fThree 的类型是:", type(fThree), fThree)
# 异常转换
"""
errorStrTwo = "3.36iyy"
errFloat = float(errorStrTwo)
"""

# float --> int 注意 负数是向上取整， 整数是向下取整
fFive = 3.9
intA = int(fFive)
print("intA 的类型是:", type(intA), intA)


# int --> float
intB = 3
fSix = float(3)
print("fSix 的类型是:", type(fSix), fSix)

# 运算符
# +
sumOne = 3+4
print("3+4 的结果是：", sumOne)

"""
# 练习 输入 两个数字 求和

# 第一步将受到的字符串 转换成 int 型
inputOne = int(input("请输入第一个数字:"))
inputTwo = int(input("请输入第二个数字:"))

# 第二步 求和
inputSum = inputOne + inputTwo
print("求和：", inputSum)
"""

# 减法
sub = 3400-786
print("3400-786 = ", sub)

# 乘法
mult = 3*8
print("3*8 = ", mult)

# 除法
div = 4/3
print("4/2 = ", div)

# 地板除 (取整符号)// 6//7正数 负数都是向下 取整
print("4//3 = ", -5//3)


# 求余 %
print("7%3 =", 7%3)
if 7%3 == 0:
    print("7能整除3")
else:
    print("7能不能整除3")

# 求幂 ** 5**3 5的三次方
print("5的三次方等于:", 5**3)

# 逻辑运算符号
# and and 两边都为Ture 返回True 否则返回false
andOne = 1 and 0
print(andOne)
# or 两边有一个为Ture 返回Ture
print("Or 运算", True or False)

# 运算符的优先级 逻辑运算符的优先级 > 比较操作的 > 算数操作 > 幂运算

# 练习 如何判断 一个 数字是奇数 还是偶数 能被2 整除就是 偶数 否者就是奇数

# 方法一:

num = int(input("请输入一个整数："))
if num & 1 == 0:#num % 2 == 0
    print("num ", num, "是偶数")
else:
    print("num ", num, "是奇数")
















