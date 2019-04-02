# class 类
# object 对象 / 或者所有类的父类

# 声明类的语法:class : 就是声明一个类;Human : 类的名字 ;(  ):括号里填 这个类的父类
class Human(object):
    # 类的初始化方法  self :就代表类  本身
    def __init__(self,name,age,sex):
        # 将入参的neme 赋值给类  类本身的name
        # 这是类的属性
        self.name = name
        self.age = age
        self.sex = sex
    # 类里面的方法  必传 self
    def myInfo(self):
        print('我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex))

    def myInfo1(self):
        return '我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex)

# 声明一个测试者 类 ,继承 Human 类
class Tester(Human):
    # 声明 一个方法
    def zhiXingCeShi(self):
        # 调用了父类的属性
        print(self.name)
        print('我在忙,别打扰我')
        # 调用了父类的方法
        self.myInfo()

if __name__ == '__main__':
    # # = 后面  调用了这个类 传入了初始化的参数 , 参数必须传 ,而且传完整,有几个参数就传几个参数; 之后你会获得一个对象
    # # = 前面是 对象名
    # # 对象是类的 实例化
    # human = Human('xxx', 18, '女')
    # print(type(human))
    # # 对象可使用 类中的方法
    # human.myInfo()    #  对象调用类的方法
    # info_str = human.myInfo1()
    # print(info_str)
    tester = Tester("xxx", 20, '女')
    tester.zhiXingCeShi()
    print(type(tester))