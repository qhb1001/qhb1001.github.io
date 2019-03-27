def initialize(b=[]):
    for i in range(0, 10, 2):
        b.append(i)


c = []
initialize(c)

print(c)
c[0] = 10

print(c)

x = {}


a = 1
b = a
a = 2
print(id(a), id(b))
print(b)

x = "global"

dic = {}
dic['abc'] = 5
def foo():
    dic = {}
    dic['abc'] = 4
    lis = []
    tup = (1, 2, 3)
    x = 5
    def fuck():
        tup = (2, 3, 4)
        dic['abc'] = dic.get('abc', 0) + 1
        print(dic)
        lis.append(10)
    return fuck

fuck = foo()
fuck()



a = [1, 2, 3]
b = []

b.append(a)
print(b)
b.append(a[:])
print(b)


