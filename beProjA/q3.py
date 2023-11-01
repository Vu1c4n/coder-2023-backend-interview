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

# q3: 创建一个Student类，类成员有（name, age, index），将data中的数据洗成Student类模板的格式，得到一个新的数组，打印
    # index 为该元素在原data数组中的 index + 29
    # “打印”步骤：需要在Student类中，自定义一个printStudent()类方法

# 答案填写在class Student和 q3()内
class Student:
    # 设置类成员，并进行类型批注
    name:str
    age:int
    index:int

    # 构造函数
    def __init__(self, name:str, age:int, index:int) -> None:
        self.name = name
        self.age = age
        self.index = index

    # 创建打印函数
    def prt(self):
        print({
            'name':self.name,
            'age':self.age,
            'index':self.index
        })

def q3():
    OFFSET = 29 # 规定偏移量为常数29（题干要求）
    newList:list[Student] = [] # 创建空list，用于接收处理后的数据
    for i in data:
        index = data.index(i) + OFFSET
        temp = Student(i['name'], i['age'], index) # 创建一个Student实例
        newList.append(temp) # 将这个实例添加入list
    for i in newList:
        i.prt()

if __name__ == '__main__':
    q3()
