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




