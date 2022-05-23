# 字符串的操作
varStr = "abc"
print(type(varStr))

# 字符串所有的接口
#print(dir(varStr))

# "\n"换行 & \t
print("hello\n world!! \t你好！！岳云鹏")

# 格式化输出
# 用+
varStrOne = "大家好我叫: 岳云鹏，今年" + str(18) + "岁，动物园毕业！！"
print(varStrOne)

# format 函数
varStrTwo = "大叫好我叫{} 今年{}岁， 我多钱没有兴趣".format("马云", 19)
print(varStrTwo)

# 字符串的访问
varStrThree = "Hello!!"
# 通过索引来访问
print(varStrThree[0])
print(varStrThree[1])
print(varStrThree[2])
print(varStrThree[3])

#字符串的截取
print(varStrThree[0:3:1])

# 字符串的 分割 split("分割的字符")
vatStrFour = "1,2,3,4,6"
print(type(vatStrFour.split(",")), vatStrFour.split(","))

# 字符串替换
varReplace = "写情书:\n \txxx,我喜欢你很久了，xxx听说你去输液了，输的什么液？是想xxx的每一夜！！"
print("最初的字符串: " + varReplace)
print(varReplace.replace("xxx", "马化腾"))

# 字符串的定义
strDefineOne = "123444"
strDefineTwo = '123444'
strDefineThree = '"2": "3"'
strDefineMultLine = """12333
dsjdjakdasdj
ffffff
"""
print(strDefineOne)
print(strDefineTwo)
print(strDefineThree)
print(strDefineMultLine)




















