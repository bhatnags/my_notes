a = set()

A = {1, 2, 3}
A = set('qwerty')
print(A)


# set do not have duplicates
A = {1, 2, 3}
B = {3, 2, 3, 1}
print(A == B)

sorted(B)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# max(my_set) Error

# set cannot have mutable items
# here [3, 4] is a mutable list

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)

my_set = {1,3}
print(my_set)
my_set.add(2) # add an element
print(my_set)
my_set.update([2,3,4]) # add multiple elements
print(my_set)
my_set.update([4,5], {1,6,8}) # add list and set
print(my_set)

# next you will get an error: TypeError: 'set' object does not support indexing
#my_set[0]

# remove an element
my_set.discard(4)
print(my_set)
my_set.remove(6) #returns error when not present
print(my_set)
my_set.discard(6) # doesn't returns error when not present
print(my_set)


A = {1, 2, 3}
print(1 in A, 4 not in A)

my_set = set("HelloWorld")
print(my_set)
print(my_set.pop()) # pop the first (in this case, it'll be random)

my_set.clear()
print(my_set) #Output: set()

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)
A.union(B)
B.union(A)

print(A & B)
A.intersection(B)
B.intersection(A)

print(A ^ B)
A.symmetric_difference(B)
B.symmetric_difference(A)

print(A - B)
A.difference(B)

B - A
B.difference(A)

A.difference_update(B)

A.isdisjoint(B)
A.issubset(B)
A.issuperset(B)

'''
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
update()	Updates the set with the union of itself and others
A | B A.union(B) Returns a set which is the union of sets A and B.
A |= B A.update(B) Adds all elements of array B to the set A.
A & B
A.intersection(B)
Returns a set which is the intersection of sets A and B.
A &= B
A.intersection_update(B)
Leaves in the set A only items that belong to the set B.
A - B
A.difference(B)
Returns the set difference of A and B (the elements included in A, but not included in B).
A -= B
A.difference_update(B)
Removes all elements of B from the set A.
A ^ B
A.symmetric_difference(B)
Returns the symmetric difference of sets A and B (the elements belonging to either A or B, but not to both sets simultaneously).
A ^= B
A.symmetric_difference_update(B)
Writes in A the symmetric difference of sets A and B.
A <= B
A.issubset(B)
Returns true if A is a subset of B.
A >= B
A.issuperset(B)
Returns true if B is a subset of A.

A < B Equivalent to A <= B and A != B
A > B Equivalent to A >= B and A != B

'''

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1 | ('baz', 'qux', 'quux')
#TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

x1.union(('baz', 'qux', 'quux'))
# {'baz', 'quux', 'qux', 'bar', 'foo'}



a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.union(b, c, d)
a | b | c | d
a.intersection(b, c, d)
a & b & c & d


a.difference(b, c)
a - b - c


a ^ b ^ c
a.symmetric_difference(b, c)
# TypeError: symmetric_difference() takes exactly one argument (2 given)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1.isdisjoint(x2) #False
x1.isdisjoint(x2 - {'baz'}) #True



vowels = {'a', 'e', 'i', 'o', 'u'}
'e' in vowels #True
letters = set('alice')
letters.intersection(vowels)
vowels.add('x')
len(vowels)


vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
vowels.add('p') #AttributeError: "'frozenset' object has no attribute 'add'"


from collections import Counter
inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot) #Counter({'bread': 3, 'sword': 1})
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot) #Counter({'bread': 3, 'sword': 2, 'apple': 1})


len(inventory) #3  # Unique elements
sum(inventory.values()) #6


