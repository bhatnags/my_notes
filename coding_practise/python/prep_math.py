abs(21-2)
abs(21-22)


# Leibniz Formula
def make_pi():
  pi = 0
  accuracy = 100000
  for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))
  i = 0
  lst = []
  while i<4:
    if len(str(pi)[i].strip('.'))>0:
      lst.append(int(str(pi)[i]))
    i = i + 1
  return lst#(map(int, str(pi).strip()))[:3]
  #return pi

make_pi()



#https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

powTwo = PowTwo(5)
powTwoIter = iter(powTwo)
list(powTwo)
print(list(powTwoIter))

