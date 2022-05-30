# for
# for 的语法
# for iterrater in squen：
# 遍历 字符串
"""
testStr = "hello"
for oneChar in testStr:
    print(oneChar)
# 遍历列表
testList = ["杨幂", "岳云鹏", "tony", "jack"]
for oneName in testList:
    print(oneName)

# range
# 打印1-10 所有的数字 range(开始数字, 结束数字-1， 步长)
for num in range(10,1,-1):#
    print(num)
"""
# 计算1-99之和(1)
import time

"""
sum = 0
for num in range(1,100, 1):
    sum = sum+num
    print(sum)
print("计算结果：", sum)
"""

# 打印乘法口诀表
"""
print("打印乘法口诀表")
for i in range(1,10):
    print("现在打印第{}行 总共{}个元素 ".format(i, i))
    for j in range(1, i+1):
        print("{}X{}={} ".format(j, i, j*i), end="")
    print("\n")
print("结束！！")
"""

# 找到100 以内的 最小能够整除 17 和9 的数字 ？
"""
start = time.time()
print("开始时间", start)
for num in range(0, 1000, 9):
    if (num%17 == 0) and (num%9 == 0):
        print("我找到了: ", num)
endTime = time.time()
print("结束时间:", endTime)
print("耗时:", (endTime - start))
print("结束！！")
"""