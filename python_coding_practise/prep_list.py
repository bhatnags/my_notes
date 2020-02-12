#####################################################

my_list = ['p','r','o','g','r','a','m','i','z']
my_list.remove('r')
my_list.remove(1) # throws ValueError
my_list[2:2] = [1,2,3,4] # ['p', 'o', 1, 2, 3, 4, 'g', 'r', 'a', 'm', 'i', 'z']

#slice notation
print(my_list[2:5])
print(my_list[2::2])
print(my_list[2::5]) # start from 2 and then skip 5 and then skip 5 ...
print(my_list[1::5])
print(my_list[:-2]) # give all till -2 index

# Print your random 'list' element
from random import choice, randrange
print(choice(my_list))
# Select a random index from 'randomLetters`
randomIndex = randrange(0, len(my_list))
print(my_list[randomIndex])

helloWorld = ['hello','world','1','2']
list(zip(helloWorld))
dict(zip(helloWorld[0::2], helloWorld[1::2]))





thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist.append("guava")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)
del thislist
print(thislist)

mylist = my_list.copy()
print(mylist)
thislist = list(mylist)
print(thislist)

list_join = mylist + thislist
for x in mylist:
  thislist.append(x)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
# append() function takes an treat it as a single object.
# extend(), on the one hand, takes an iterable (that’s right, it takes a list, set, tuple or string!), and adds each element of the iterable to the list one at a time.
list1.extend(list2) # extends the original lsit
list1 + list2 # creates another variable

print(list1)


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

list1[0].next

a = ["bee", "ant", "moth", "ant"]
print(a.index("ant"))
print(a.index("ant", 1))
print(a.index("ant", 2))

a = ["bee", "ant", "moth", "ant"]
print(a.count("bee"))
print(a.count("ant"))
print(a.count("")) # returns 0

a = [3,6,5,2,4,1]
a.sort(reverse=True) # a is sorted
print(a)

a = ["bee", "wasp", "moth", "ant"]
a.sort()
print(a)

a = ["bee", "wasp", "butterfly"]
a.sort(key=len)
print(a)

a = ["bee", "wasp", "butterfly"]
a.sort(key=len, reverse=True)
print(a)


a = [3,6,5,2,4,1]
a.reverse() # O(n) # note: it's not sorting
print(a)

a = ["bee", "wasp", "moth", "ant"]
a.reverse()
print(a)


a = "bee"
print(list(a))

a = ("I", "am", "a", "tuple")
print(list(a))

a = {"I", "am", "a", "set"}
print(list(a))


min(a)
max(a)

print(list(range(10)))
print(list(range(1,11)))
print(list(range(51,56)))
print(list(range(1,11,2)))

print(["re"] * 3)

sentence = ['this','is','a','sentence']
'-'.join(sentence)
''.join(sentence)


pow2 = [2 ** x for x in range(10) if x > 5]


import itertools
a = [[1,3,3],[4,5,6],[7,8,9,10]]
lst = list(itertools.product(*a))
len(set(lst)) # gives all combinations for grid search


###################
# shallow vs deep copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy
import copy
zs = copy.deepcopy(xs)
xs.append(['new sublist']) # on xs changes
xs[1][0] = 'X' # xs and ys changes
xs
ys
zs

[x**2 for x in range(10)]
[x**2 for x in range(1,11)]
[x**2 for x in range(10) if x%2==0]
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x*x
[f(x) for x in range(10)]
[(lambda x: x*x)(x) for x in myList]
[(lambda x: x*x+1)(x) for x in myList]


from collections import Counter
lst = ["a","b","b"]
Counter(lst)

x = [1,2,3,4,5,6,7,8,9]
y = zip(*[iter(x)]*3) # Split `x` up in chunks of 3
list(y) # Use `list()` to print the result of `zip()`


# Method to split up your lists into chunks
def chunks(list, chunkSize):
    """Yield successive chunkSize-sized chunks from list."""
    for i in range(0, len(list), chunkSize):
        yield list[i:i + chunkSize]
import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))

# Flatten out your original list of lists with `sum()`
list1 = [[1,2],[3,4],[5,6]]
list2 = [[1,2,3,4,[5,6]],[7,8,[9,10]]]
sum(list1, [])
sum(sum(list1, []))
sum(list2, [])
# You can reduce the lists of lists of lists like this
from functools import reduce
print(reduce(lambda x,y: x+y,listOfLists))
print([item for sublist in listOfLists for item in sublist])

([1,2]+[3,4])+[5,6]




