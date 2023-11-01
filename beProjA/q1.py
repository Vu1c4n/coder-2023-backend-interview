data = [
    {
        'name':'张三',
        'age':12,
        'sex':'female'
    },
    {
        'name':'李四',
        'age':20,
        'sex':'male'
    },
    {
        'name':'王五',
        'age':22,
        'sex':'female'
    }
]


# q1: 将data中所有age > 18 并且 sex == "male" 的元素的name打印出来
# 在q1()内填写答案
def q1():
    for i in data:
        # 定义常量
        AGE_LIMIT = 18
        SEX_LIMIT = 'male'
        chkAge = i['age'] > AGE_LIMIT # 取dict的value: "[key]"
        chkSex = i['sex'] == SEX_LIMIT
        if chkAge and chkSex:
            print(i['name'])

# 主函数部分（用于单元测试）
if __name__ == '__main__':
    q1()
