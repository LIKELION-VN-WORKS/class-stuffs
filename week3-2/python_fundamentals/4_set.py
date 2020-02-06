# set(집합) :
# type 1 : {'1',2,'likelion'} / type 2 : set([1,2,3])

a = {'1', 2, 'likelion','1', (3,4), True}
b = {2, 'likelion', True, False, (5,6)}
print(a|b) # union(합집합)
print(a&b) # intersection(교집합)
print(a-b) # difference(차집합)

# An object is hashable if it has a hash value which never changes during its lifetime.(https://docs.python.org/3.9/glossary.html)
# unhashable : dictionary, list

c = set(['1',2,'likelion','1', (3,4), True])
d = set([2, 'likelion', True, False, (5,6)])

print(c|d) # union(합집합)
print(c&d) # intersection(교집합)
print(c-d) # difference(차집합)

c.add('Xin Chao')
print(c)

d.update(['vn', 8,(3,4)])
print(d)
