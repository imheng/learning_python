class Test:
    def ppr(self):
        print(self)
        print(self.__class__)

t = Test()
t.ppr()
执行结果：
<__main__.Test object at 0x000000000284E080>    self代表的是类的实例
<class '__main__.Test'>  而self.__class__则指向类


class Parent:
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)
c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()
执行结果：
<__main__.Child object at 0x0000000002448CC0>
<__main__.Child object at 0x0000000002448CC0>
<__main__.Parent object at 0x0000000002448FD0>
解释： 
运行c.cprt()时应该没有理解问题，指的是Child类的实例。 
但是在运行c.pprt()时，等同于Child.pprt(c)，所以self指的依然是Child类的实例，由于self中没有定义pprt()方法，所以沿着继承树往上找，发现在父类Parent中定义了pprt()方法，所以就会成功调用


class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x
执行结果：
self in Test: <__main__.Test object at 0x00000000022F8C88>
self in Desc: <__main__.Desc object at 0x00000000022F89B0> 
<__main__.Desc object at 0x00000000022F89B0> <__main__.Test object at 0x00000000022F8C88> <class '__main__.Test'>
解释：
这里主要的疑问应该在：Desc类中定义的self不是应该是调用它的实例t吗？怎么变成了Desc类的实例了呢？ 
因为这里调用的是t.x，也就是说是Test类的实例t的属性x，由于实例t中并没有定义属性x，所以找到了类属性x，而该属性是描述符属性，为Desc类的实例而已，所以此处并没有顶用Test的任何方法。

那么我们如果直接通过类来调用属性x也可以得到相同的结果。

下面是把t.x改为Test.x运行的结果。
self in Test: <__main__.Test object at 0x0000000002638C88>
self in Desc: <__main__.Desc object at 0x00000000026389B0> 
<__main__.Desc object at 0x00000000026389B0> None <class '__main__.Test'>
