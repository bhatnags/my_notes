
l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

# in dictionary, they look for keys
d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', 1: 'False'}
print(any(d))

d = {1: 'False'}
print(any(d))
d = {0: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))

s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))


'''
all()	Return True if all elements of the set are true (or if the set is empty).
any()	Return True if any element of the set is true. If the set is empty, return False.
for any.. it checks "at least"... at least one is true
'''


def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Maximum is:', max(num, key=sumDigit))

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2, key=len))

for i in range(1, 10):
    print(i)


import math
sum(num)
math.fsum(l) #If you need to add floating point numbers with exact precision
''.join(list(map(str, num)))
list(map(int, num))


grocery = ['bread', 'milk', 'butter']

enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))
print(tuple(enumerateGrocery)) #
print(dict(enumerateGrocery)) #

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
  
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sortedList = sorted(random, key=takeSecond)
sorted(random)

A = frozenset([1, 2, 3, 4])
A.add(3) # Error
list(map(lambda x:x+3, A))


x = frozenset(['foo', 'bar', 'baz'])
id(x)
s = {'baz', 'qux', 'quux'}
x &= s
id(x) # id changed, reassigning x to a new object


x1 = set(['foo'])
x2 = set(['bar'])
x3 = set(['baz'])
x = {x1, x2, x3} # TypeError: unhashable type: 'set'
x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3} # {frozenset({'bar'}), frozenset({'baz'}), frozenset({'foo'})}


x = {1, 2, 3}
y = {'a', 'b', 'c'}
d = {x: 'foo', y: 'bar'} # Dict keys shud be immutable, TypeError: unhashable type: 'set'



from sortedcontainers import SortedList
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
sl *= 10_000_000
sl.count('c')
sl[-3:]

from sortedcontainers import SortedSet
ss = SortedSet('abracadabra')
ss.bisect_left('c')

import collections
print(isinstance({}, collections.Hashable))
print(isinstance([], collections.Hashable))
print(isinstance((), collections.Hashable))
print(isinstance(0.125, collections.Hashable))



10^80

(N N/2) = sqrt(2 pi N) (N/2)^N



