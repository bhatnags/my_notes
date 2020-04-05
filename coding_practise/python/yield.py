def alternate(*args):
    for iterable in args:
        yield iterable

def alternate(*args):
    for iterable in args:
        for item in iterable:
            yield item
            

for i in alternate('abcde','fg','hijk'): 
    print(i)

    

lst = ['abcde','fg','hijk']

for i in range(10):
    for l in lst:
        try:
            print(l[i])
        except IndexError:
            pass

def alternate(*args):
    max_len = max(map(len, args))
    for index in range(max_len):
        for lst in args:
            try:
                yield lst[index]
            except IndexError:
                #return # stop at first missing item
                continue # or pass will not stop
            
for i in alternate('abcde','fg','hijk'): 
    print(i)


#To stop on first "missing" item:

def alternate(*args):
    index = 0
    while True:
        for lst in args:
            try:
                yield lst[index]
            except IndexError:
                #return # stop at first missing item
                #pass or continue # goes into infinite loop
        index += 1


for i in alternate('abcde','fg','hijk'): 
    print(i)


import itertools

def alternate(*args):
    for iterable in itertools.zip_longest(*args):
        #yield iterable
        for item in iterable:
            if item is not None:
                yield item
                
for i in alternate('abcde','fg','hijk'): 
    print(i)
                
def alternate(*args):
    # note: python 2 - use izip_longest
    for iterable in zip(*args):
        for item in iterable:
            if item is not None:
                yield item

for i in alternate('abcde','fg','hijk'): 
    print(i)


from itertools import chain, cycle
def alternate(*iterables):
    "alternate('ABCD', 'EF', 'GHI') --> A E G B F H C"
    nexts = cycle(iter(it).__next__ for it in iterables)
    yield from chain.from_iterable(inext() for inext in nexts)
    

for i in alternate('abcde','fg','hijk'): 
    print(i)


iters = ('abcde','fg','hijk')
res = chain.from_iterable(j() for j in cycle(iter(j).__next__ for j in iters))
print(' '.join(res))