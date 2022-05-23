# if 语句

# 语法一 if 条件: 条件成立 就执行 不成立不执行
"""
age = 20
if age < 18:
    print("你的年纪只有{}岁,真年轻！！".format(age))

print("我有点老了！！")
"""
# 语法二 : if 条件：语句一  else： 语句二条件: 条件成立 就执行语句一
# 不成立执行语句二
"""
age = 17
if age < 18:
    print("你的年纪只有{}岁,真年轻！！".format(age))
else:
    print("我的年纪有{}岁,已经老了！！".format(age))
"""

# 语法三: if 条件一：语句一  elif 条件二： 语句二 else 语句三
# 条件一成立 执行 语句一
# 条件二成立 执行 语句二
"""
age = 35
if age < 18:
    print("你的年纪只有{}岁,你是儿童！！".format(age))
elif age>= 18 and age < 30:
    print("你的年纪只有{}岁,你是青年人！！".format(age))
else:
    print("你的年纪只有{}岁,你是老年人！！".format(age))
"""

# 语法四 if 嵌套
age = 32
if age >= 18:
    if age>= 18 and age < 30:
        print("你的年纪只有{}岁,你是青年人！！".format(age))
    else:
        print("你的年纪只有{}岁,你是老年人！！".format(age))
else:
    print("你的年纪只有{}岁,你是儿童！！".format(age))

#练习题：
# 闰年的判定
# 能被4 整除可能是闰年
# 不能被4整除一定不是闰年
# 能被4整除，但不能被100整除。
# 能被4整除，也能被400整除
"""
inputYear = int(input("请输入一个年份:"))
if (inputYear % 4) == 0:
    if (inputYear % 400) == 0: #能被400 整数肯定是闰年 
        print("年份{}，是闰年！！".format(inputYear))
    elif(inputYear % 100) == 0: # 能被100 整除且 不能被400 整除不是闰年
        print("年份{}，不是闰年！！".format(inputYear))
    else:
        print("年份{}，是闰年！！".format(inputYear)) 
else:
    print("年份{}，不是闰年！！".format(inputYear))
"""

# 输入一个字符串 1,2,3,4,5,56,4,7,77 求最大的
inputStr = input("请输出一个以逗号隔开的字符串数字:")
inputList = inputStr.split(",")
tmpList = []
for item in inputList:
    tmpList.append(int(item))
print(max(tmpList))
# 




















# 否者执行 语句三


