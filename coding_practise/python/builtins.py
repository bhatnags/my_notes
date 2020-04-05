import itertools

a = itertools.cycle('AB')

for it in a:
    iter(it).__next__
    
print(chain.from_iterable(inext() for inext in 'AB'))


