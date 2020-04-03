# https://codingbat.com/prob/p118406
'''
binary search
matching parenthesis

hash tables-> matrix-> traverse and keep track of all nodes visited
to cache values.. memoization and fibonacci

variables/pointers... traverse string in parallel
--- longest palindromic substring in a string

'''

'''
algoexpert.io/techlead

reversing a linked list

recursion

suffix tree type data structure

'''

s='stresseddesserts'
out1=[]
def substring(x):
    for i in range(len(x)):
        a=x[i:]
        b=x[:-i]
        out1.append(a)
        out1.append(b)        
        print(out1)
    return out1

for i in range(len(s)):
    substring(s[i:])

final=set([item for item in out1 if len(item)>2])
palind={item:len(item) for item in final if item==item[::-1]}
print(palind)
sorted(palind.items(),reverse=True, key=lambda x: x[1])[0]


######################################if changing one charater the string could be palindrome
import math as ma 
def change(s): 
    n = len(s) 
    cc = 0
    for i in range(n//2):
        if(s[i]== s[n-i-1]): 
            continue  
        cc+= 1
        # Changing the character with higher  
        # ascii value with lower ascii value 
        if(s[i]<s[n-i-1]): 
            s[n-i-1]= s[i] 
        else: 
            s[i]= s[n-i-1] 
  
    return int(cc) 

def modifyCheckPalindrome(s):
    c = change(s)
    if c>1:
        return True
    else:
        return False

def isPalindrome(s): 
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False
  
def isAlmostPalindrome(str):
    if isPalindrome(str) or modifyCheckPalindrome(str):
        return 'true'
    else:
        return 'false'

# test
s = "abccba"
print(isPalindrome(s)) 
print(modifyCheckPalindrome(s)) 
print(isAlmostPalindrome(s))

str = "abccbx"
print(isPalindrome(s)) 
print(modifyCheckPalindrome(s)) 
print(isAlmostPalindrome(s))

str = "abccfg"
print(isPalindrome(s)) 
print(modifyCheckPalindrome(s)) 
print(isAlmostPalindrome(s))



################################search algos

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])] # (vertex, path)
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path():
    try:
        return next(bfs_path())
    except StopIteration:
        return None


###################################################
string = "[([])()({})]"
PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  # too many closing symbols
            return False
        if s != PAIRINGS[expected_opening_symbol]:  # mismatch
            return False
    return len(stack) == 0  # false if too many opening symbols

is_balanced(string)



def splitz(seq, smallest):    
    group = []    
    for num in seq:
        if num != smallest:
            group.append(num)
        elif group:
            yield group
            group = []

numbers = [1, 3, 3, 5, 1, 5, 5, 5, 1, 6, 5, 4, 1, 10]
min_val = min(numbers)
print(list(splitz(numbers, min_val)))



#####################################grid search optimization
from typing import Dict, Tuple, Callable, Iterable
import numpy

def model_quadratic(model_parameters: dict):
    """
    This is a quadratic model with a minimum at a=0.5, b=0.75, c=0.25.
    """
    a = model_parameters['a']
    b = model_parameters['b']
    c = model_parameters['c']

    return 1.75 + (a - 0.5) ** 2 + (b - 0.75) ** 2 + (c - 0.25) ** 2

class Problem:
    @staticmethod
    def grid_search(search_space: Dict[str, Iterable],
                    scoring_func: Callable[[Dict[str, float]], float]) -> Tuple[float, Dict[str, float]]:
        """
        This function accepts a search space, which is a dictionary of arrays.

        For each key in the dictionary, the respective array holds the numbers
        in the search space that should be tested for.

        This function also accepts a scoring_func, which is a scoring function 
        which will return a float score given a certain set of parameters.  
        The set of parameters is given as a simple dictionary. As an example, 
        see model_quadratic above.
        """
        lst_lst = []
        for k,v in search_space.items():
            lst_lst.append(list(v))
        lsts = list(itertools.product(*lst_lst))
        print(len(lsts))
        res = 10000000
        for i in lsts:
            dct = {'a':i[0], 'b':i[1], 'c':i[2]}
            res1 = model_quadratic(dct)
            if res1<res:
                res = res1
                res_dct = dct
        return res, res_dct

print(Problem.grid_search({
    'a': numpy.arange(0.0, 1.0, 0.05),
    'b': numpy.arange(0.0, 1.0, 0.05),
    'c': numpy.arange(0.0, 1.0, 0.05),
}, model_quadratic))



########################################Moving total

def moving_total(prices_list, window_size):
    return sum(prices_list[-window_size:]) / window_size


class MovingTotal:

    def __init__(self, size):
        self.numbers = list()
        self.size = size
    
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.numbers.extend(numbers)
        while(len(self.numbers)>self.size):
            self.numbers.pop(0)

    def total_list(self):
        self.total = sum(self.numbers)
        
    def contains(self, t):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        print(t, self.numbers)
        self.total_list()
        return True if t == self.total else False
    
movingtotal = MovingTotal(3)
movingtotal.append([1, 2, 3])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([4])
print(movingtotal.contains(9))



########################### most common

from collections import Counter
def get_most_freq(lst, count):
    return Counter(lst).most_common(1)[0][0]

get_most_freq([34,31,34,77,82], 5)    
print(get_most_freq([22, 101, 102, 101, 102, 525, 88], 7)) 
print(get_most_freq([66], 1))
print(get_most_freq([14, 14, 2342, 2342, 2342], 5)) 
 
def find_unique_numbers(numbers):
    return [k for k, v in Counter(numbers).items() if v==1]
    return a

print(find_unique_numbers([1, 2, 1, 3]))

########################################



from numpy import median
from collections import defaultdict
def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the 
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following 
      elements: Class name (string), median grade for students in the class (float).
    """
    a = defaultdict(list)
    for i in students:
        a[i[1]].append(i[2])
    for i in a.items():
        print(i[0], median(i[1:]))

students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
class_grades(students)

