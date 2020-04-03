
from enum import Enum

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        ret_str = None
        print(self._right, self._left)
        try:
        if len(self._left)<len(self._right):
            ret_str = 'Side.right'
        elif self._left>self._right:
            ret_str = 'Side.left'
        #else:
        #    ret_str = Side.right
        return ret_str

left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)




