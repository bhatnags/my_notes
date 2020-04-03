import numpy as np
from numpy import array



import numpy as np
np.array([])

np.zeros(shape=(4,2))# Make a NumPy array of four rows and two columns and filled with 0
np.ones(3)# Make a NumPy array of 1 values of three columns
np.empty(shape=(0,0)) # Make an empty NumPy array


[1 for x in range(1) for y in range(2)]


a = np.array([1,2,3,4,5])
p = np.percentile(a, 50)
np.average(a)
np.max(a)

f = open("demofile.txt", "r")
for x in f:
  print(x)

np.random.rand(1, 3)



np.flip(np.arange(1, 8, 3))
np.arange(1, 8, 3)[::-1]
np.arange(2, 2) #array([], dtype=int64)
np.arange(5)

x = np.arange(5, dtype=int) #array([0, 1, 2, 3, 4])
x.dtype
x.itemsize
y = np.arange(5.0) #array([0., 1., 2., 3., 4.])
y.dtype
y.itemsize
z = np.arange(5, dtype=np.float32) #array([0., 1., 2., 3., 4.], dtype=float32)
z.dtype
z.itemsize
2*x
2**x
x**2

a = np.arange(6).reshape((2, 3))
a.shape #(2, 3)
a.ndim

# you can create a NumPy array much faster than a list [even using list comprehension], 
# except for sequences of very small lengths
# also except
# range is often faster than arange() when used in Python for loops, especially when there’s a possibility to break out of a loop soon. This is because range generates numbers in the lazy fashion, as they are required, one at a time.
# In contrast, arange() generates all the numbers at the beginning.

import timeit
n = 1
timeit.timeit(f'x = [i**2 for i in range({n})]')
timeit.timeit(f'x = np.arange({n})**2', setup='import numpy as np')

'''
In addition to arange(), you can apply other NumPy array creation routines based on numerical ranges:

linspace() is similar to arange() in that it returns evenly spaced numbers. But you can specify the number of values to generate as well as whether to include the endpoint and whether to create multiple arrays at once.
logspace() and geomspace() are similar to linspace(), except the returned numbers are spaced evenly on the logarithmic scale.
meshgrid(), ogrid(), and mgrid() return grids of points represented as arrays.
'''
c = np.linspace(0, 1, 6)   # start, end, num-points
c

d = np.linspace(0, 1, 5, endpoint=False)
d

a = np.ones((3, 3))  # reminder: (3, 3) is a tuple
a

b = np.zeros((2, 2))
b

c = np.eye(3)
c

d = np.diag(np.arange(3))
d
d = np.diag(np.array([1, 2, 3, 4]))
d

a = np.random.rand(4)       # uniform in [0, 1]
a  


b = np.random.randn(4)      # Gaussian
b  

np.arange(6) + np.arange(0, 51, 10)
a=np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
a[(0,1,2,3),(2,3,4,5)]
a[3:, [1,3,5]]
np.vstack([array(np.zeros(5, dtype=int)), np.diag(np.arange(2,7,1))])
np.vstack([array(np.zeros(5)), np.diag(np.arange(2,7,1))])
a = np.ones((4,4), dtype=int)
a[2][3]=2
a[3][1]=6


np.random.seed(1234)        # Setting the random seed

e = np.array([True, False, False, True])
e.dtype

f = np.array(['Bonjour', 'Hello', 'Hallo'])
f.dtype     # <--- strings containing max. 7 letters 

a[::-1]

s = slice(2,7,2) 
print a[s]
b = a[2:7:2] 
print b

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
x = slice(0, 8, 3)
print(a[x])
x = slice(2)
print(a[x])



list1 = [1, 2, 3, 4 ,5, 6] 
list2 = [10, 9, 8, 7, 6, 5] 
  
# Multiplying both lists directly would give an error. 
print(list1*list2) #ERRRRRRRRRRROOOOOOOORRRRRRR

# Convert list1 into a NumPy array 
a1 = np.array(list1) 
a2 = np.array(list2) 
print(a1*a2)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x[-3:5:1]
x[-3:5:-1]

x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
x.shape #(2, 3, 1)
x[:,np.newaxis,:,:].shape

x = array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])
rows = np.array([[0, 0],
                 [3, 3]], dtype=np.intp)
columns = np.array([[0, 2],
                    [0, 2]], dtype=np.intp)
x[rows, columns]

rows = np.array([0, 3], dtype=np.intp)
columns = np.array([0, 2], dtype=np.intp)
rows[:, np.newaxis]
x[rows[:, np.newaxis], columns]
x[np.ix_(rows, columns)]

x[1:2, 1:3]
x[1:2, [1, 2]]

x = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
x[~np.isnan(x)]

x = np.array([1., -1., -2., 3])
x[x < 0] += 20
x


x = np.array([[0, 1], [1, 1], [2, 2]])
rowsum = x.sum(-1)
x[rowsum <= 2, :]

rowsum = x.sum(-1, keepdims=True)
rowsum.shape

x[rowsum <= 2]
x[rowsum <= 2, :]    # fails # IndexError: too many indices



x = array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])
rows = (x.sum(-1) % 2) == 0
rows

columns = [0, 2]
x[np.ix_(rows, columns)]
x.ndim


# one dimensional example
from numpy import array
# list of data
data = [11, 22, 33, 44, 55]
# array of data
data = array(data)
print(data)
print(type(data))

# one dimensional example
from numpy import array
# list of data
data = [11, 22, 33, 44, 55]
# array of data
data = array(data)
print(data)
print(type(data))


