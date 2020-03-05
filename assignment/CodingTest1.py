# A first question focusing on your coding computational efficiency 

# Sorting:
f=lambda n:sorted(set(n),key=n.count)[::-1]
print f(arr)

for key, value in freq.iteritems(): 
	print key, " -> ", value 
print collections.Counter(arr).values(), collections.Counter(arr).keys()

# Fibonnaci
def Fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (Fibonnaci(n-1)+ Fibonnaci(n-2))
n = int(input())
print(Fibonnaci(n))

''' IN C:
int fib(int);
int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fib(n));
    return 0;
}
int fib(int n){
    if(n == 0){
        return 0;
    } else if(n == 1){
        return 1;
    } else {
        return (fib(n-1)+fib(n-2));
    }
}
'''

# Balanced Delimiters
string = input().strip()
while '()' in string or '[]' in string or '{}' in string:
    string = string.replace('()','')
    string = string.replace('[]','')
    string = string.replace('{}','')
print(len(string) == 0)


#MAP
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]


# Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# Output: [-5, -4, -3, -2, -1]


# Reduce
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# Output: 24


import pandas as pd
import numpy as np
import itertools

class StockPrices:
    # param prices dict of string to list. A dictionary containing the tickers of the stocks, and each tickers daily prices.
    # returns list of strings. A list containing the tickers of the two most correlated stocks.
    @staticmethod
    def most_corr(prices):
        #a = np.corrcoef(list(prices'GOOG'), list('FB'))
        #df = pd.DataFrame(prices.items(), columns=['GOOG', 'FB', 'MSFT', 'AAPL'])
        #df = pd.DataFrame.from_dict(prices,orient='index')
        df = pd.DataFrame(prices)#,orient='index')
        #aPrev = df.corr()
        # a = df['AAPL'].corr(df['FB'])
        # df2 = pd.DataFrame(aPrev)
        #c = df.corr().abs()
        #s = c.unstack()
        #so = s.sort_values(kind="quicksort", ascending=False)#.drop_duplicates()
        #f = list(filter(lambda x: x < 1, so))
        #a = (pd.DataFrame(so[4:5]))
        #b=a.iloc[:,0:1]
        df1 = pd.DataFrame([[(i,j),df.corr().loc[i,j]] for i,j in list(itertools.combinations(df.corr(), 2))],
                           columns=['pairs','corr'])    
        a = df1.sort_values(by='corr',ascending=False)[0:1]
        return a.pairs

#For example, with the parameters below the function should return ['FB', 'MSFT'].
prices = {
    'GOOG' : [
        742.66, 738.40, 738.22, 741.16,
        739.98, 747.28, 746.22, 741.80,
        745.33, 741.29, 742.83, 750.50
    ],
    'FB' : [
        108.40, 107.92, 109.64, 112.22,
        109.57, 113.82, 114.03, 112.24,
        114.68, 112.92, 113.28, 115.40
    ],
    'MSFT' : [
        55.40, 54.63, 54.98, 55.88,
        54.12, 59.16, 58.14, 55.97,
        61.20, 57.14, 56.62, 59.25
    ],
    'AAPL' : [
        106.00, 104.66, 104.87, 105.69,
        104.22, 110.16, 109.84, 108.86,
        110.14, 107.66, 108.08, 109.90
    ]
}

print(StockPrices.most_corr(prices))



class Palindrome:

    @staticmethod
    def is_palindrome(word):
        # reverse the string
        my_str = word
        rev_str = reversed(word)

        # check if the string is equal to its reverse
        if list(my_str) == list(rev_str):
           res = False
        else:
           res = True
        return res
print(Palindrome.is_palindrome('Deleveled'))


