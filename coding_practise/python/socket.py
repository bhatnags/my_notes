import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

try:
    socket.inet_aton(IPAddr)
    print('valid')
except socket.error:
    print('invalid')    

import IPy
from IPy import IP
IP(IPAddr)


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
