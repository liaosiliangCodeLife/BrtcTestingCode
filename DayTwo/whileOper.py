# -*- coding:utf-8 -*-
# while
# 语法 while condtion: 直到condtion 为False
import time

"""
cnt = 10
while cnt>0:
    print("我最帅！！！")
    cnt = cnt-1
print("十次就够了！！")

print(time.localtime())
# 练习显示时间：how to solove
while True:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(1)
    """

# break & return 退出
"""
cnt = 10
while cnt>0:
    print("我最帅！！")
    time.sleep(1)
    cnt = cnt-1
    if cnt==5:
        print("让开 我要执行 break")
        # break
        # return
        # chucuo
        exit(0)
print("我结束了")
"""

# echo 程序 输入什么就输出什么
"""
while True:
    inputStr = input("请输入你的问题:")
    print(inputStr)
    if inputStr.__contains__("bye"): #inputStr.__eq__("bye") # "bye" in inputStr
        break
        """
"""
while False:
    print("执行false")
print("执行结束")

while not input("请输入Bye 退出").__eq__("bye"):
    print("哈哈 我没退出！！")

print("我退出了！！")
"""

# continue直接进入下一轮循环 while 后面语句不在执行
cnt = 10
while cnt > 0:
    inputStr = input("请输你的问题！:")
    cnt = cnt -1
    if inputStr.__eq__("con"):
        continue

    print(inputStr)
    if inputStr.__eq__("bye"):
        break
print("我退出！！")