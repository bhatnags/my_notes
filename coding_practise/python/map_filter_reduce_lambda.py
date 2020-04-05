# map gives list or set, etc
# reduce, reduces the list or set or... 

from functools import reduce


# map(function, iterables)


def newfunc(a):
    return a*a

x = map(newfunc, (1,2,3,4)) #x is the map object
print(x)
print(set(x))
print(list(x))
print(tuple(a))

[2, 4, 5] + [1,2,3]

def func(a, b):
    return a + b

def funct(c):
    print(c[0] , c[1])
    return c[0] + c[1]

a = map(funct, [2, 4, 5], [1,2,3])

print(a)
print(tuple(a))


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x*x
[f(x) for x in range(10)]
[(lambda x: x*x)(x) for x in myList]
[(lambda x: x*x+1)(x) for x in myList]


from functools import reduce
import functools, operator, itertools

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="s") 
print (functools.reduce(lambda a,b : a+b,myList)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,myList)) 


# using reduce to compute sum of list 
# using operator functions 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,myList)) 
  
# using reduce to compute product 
# using operator functions 
print ("The product of list elements is : ",end="") 
print (functools.reduce(operator.mul,myList)) 
  
# using reduce to concatenate string 
print ("The concatenated product is : ",end="") 
print (functools.reduce(operator.add,["geeks","for","geeks"]))

operator.add,["geeks","for","geeks"][1]



# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(myList,lambda x,y : x+y))) 
list(itertools.accumulate(myList,lambda x,y : x+y))[-1]

# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,myList)) 



def func(a):
    return set(a.keys())

graph = {
'A':{'B':1,'C':1,'E':1},
'B':{'A':1,'D':1,'F':1},
'C':{'A':1,'G':1},
'D':{},
'E':{'A':1,'F':1},
'F':{'B':1,'E':1},
'G':{}
}

for k in graph:
    print(set(graph[k]))

for item in graph.items():
    print(item)
    print(type(item))
    
graph1 = {}
for key, value in graph.items():
    graph1[key] = set(value.keys())

x = map(func, graph.keys()) #x is the map object






####################################################
############################################
###################################
# Optimiation 

a = [1,2,3]
b = [4,5,6]

c = a[1:].append(a[0])

#list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))

list(map(lambda x, y: 2*x+3*y, a, b))








###########################################

contests = [(1,1),(3,0),(5,1),(6,0),(2,1),(4,0)]

a = [(lambda x:x[1])(x) for x in contests]
a = map(lambda x:x[1], contests)

a = filter(lambda x:x[1]==1, contests)

a = reduce(lambda x,y:x*y[1], contests)

print(list(a))



##############################

numbers = [55, 92, 27, 48, 34, 62, 71, 18, 28, 43]

def numCheck(n):
  if n < 10:
    return False
  else:
    return True
#passing through the filter function
result = filter(numCheck, numbers)

def learn(n):
    yield True

result = filter(learn, [1,2,3,4])

#displaying the result
for n in result:
  print(n)



len(filter(lambda x:x<50, numbers)) # throws TypeError

a = filter(lambda x:x<50, numbers)
for _ in a:
    print(_)






n=map(int, input("Enter the numbers you want to add: ").split())
reduce(lambda x,y:x+y, n) #import from functools





# FACTORIAL
import operator
from operator import mul
n = 10
reduce(mul,range(1,n),1)
reduce(lambda accValue,curItem:accValue*curItem,range(1,n),1)




def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value






