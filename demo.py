
class Demo:
    age = 10
    def __init__(self, maths):
        #instance variables
        self.tamil = 50
        self.english = 100
        self.Maths = maths
        print("Constructor")

    # functions
    '''
    instance method
    static method
    class method'''
    # variables
    '''
    Local variables
    instance variables
    static or class variables
    global variables
    '''
    #Constructor def __init__()

    # instance method
    def add(self, a):
        # local variable
        global b
        b =a

    @staticmethod
    def sub():
        print("sub", b)
        return 1-2


    @classmethod
    def avg(cls):
        return 5/3

d = Demo(88)
print(d.Maths)

d1 = Demo(77)

print(d1.Maths)
print(d.Maths)
# instance content(instance variable and instance methods can be accessed by usign object)

print(Demo.age)
Demo.age = 100

print(Demo.age)
print(d.avg())
print(d.add(44))
print(Demo.sub())