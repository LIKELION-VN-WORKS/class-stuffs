class ClassName:
    classVariable = 'classVariable'

    def __init__(self, param1):
        self.param1 = param1


    def method(self, param2):
        self.param2 = param2
        return (self.param1, self.param2)

a = ClassName(1)

b = a.method(2)
print(b)


print(ClassName.classVariable)
print(a.classVariable)
