from model import *

s1 = Identity(name='张三' ,age= 12,sex="male")
s2 = Identity(name='李四' ,age= 20,sex="male")
s3 = Identity(name='王五' ,age= 22,sex="female")

data = [s1,s2,s3]

# q2: 将data中所有age > 18 并且 sex == "male" 的元素的name打印出来
# 在q2内填写答案
def q2():
    # 定义常量
    AGE_LIMIT = 18
    SEX_LIMIT = 'male'
    for i in data:
        chkAge = i.age > AGE_LIMIT # 取类对象用 "."
        chkSex = i.sex == SEX_LIMIT
        if chkSex and chkAge:
            print(i.name)

if __name__ == '__main__':
    q2()

