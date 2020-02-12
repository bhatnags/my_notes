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

