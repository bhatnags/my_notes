'''
Problem:
    You live in a remote settlement where bread sellers come through periodically at irregular
    intervals. Whenever you buy fresh bread, it lasts for 30 days until it becomes too stale to eat.
    Your family eats one loaf of bread per day.
    You are given a calendar of when the bread sellers will be visiting over the coming days and the
    price each bread seller will charge per loaf. You currently have 10 fresh loaves, and at the end
    of the calendar you'll get a bunch of free bread, so you won't need to have any left on hand.
    Write a function that tells you how much bread to buy from each of the sellers

Input:
    total_days, an integer, the number of days in the calendar until the free bread arrives
    sellers, a list of pairs of integers (day, price). Each pair represents one bread seller
    The day is how many days from the start until the seller arrives
    The price is the price to buy each loaf of bread from this seller, in pennies
Output:
    purchases, a list of integers of the same length as sellers. Each integer is how many
    loaves you should buy from each seller
    Or None, if there is no solution that does not force your family to eat stale bread at some point

You should output the purchase plan that minimizes the total cost. In case of ties, output the
plan that requires buying from the fewest number of different sellers, and within those choose
the plan that buys more bread earlier

'''





a = { "a" : 1, "b" : 2 }
b = { "c" : 3, "d" : 4 }
c = {**a, **b}
# c = { "a" : 1, "b" : 2, "c" : 3, "d" : 4 }
a.keys()
a.values()



from sortedcontainers import SortedDict
dict_one = {'c': 3, 'a': 1, 'b': 2, 'ab':5}
sorted(dict_one) # ['a', 'ab', 'b', 'c'] #dict_one still remains the same
sd = SortedDict(dict_one) #this sorts
sd.popitem(index=-1) # error



d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted(d.items(), key=lambda x: x[1])
sorted(d.items(), key=lambda x: x[1], reverse=True)

d = {1: 5, 3: 4, 4: 3, 2: 1, 0: 0}
sorted(d.values()) #[0, 1, 3, 4, 5]
sorted(d.items()) #[(0, 0), (1, 5), (2, 1), (3, 4), (4, 3)]


a = [1, 2, 3, 4, 5]
i = iter(a)
print(dict(zip(i, i)))


import collections 
  
# Declaring namedtuple() 
Student = collections.namedtuple('Stud',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
S1 = Student('Nandi','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name) 
  
# Access using getattr() 
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB')) 

# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict()) 
  
# using ** operator to return namedtuple from dictionary 
print ("The namedtuple instance from dict is  : ") 
print (Student(**di)) 

print ("All the fields of students are : ") 
print (S._fields) 
  
# using _replace() to change the attribute values of namedtuple 
print ("The modified namedtuple is : ") 
print(S._replace(name = 'Manjeet')) 

