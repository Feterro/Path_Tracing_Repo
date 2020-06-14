
class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __truediv__(self, other):
        return Point(self.x/other, self.y/other)

    def dot(self, p2):
        #v2 (x1-x2, y1-y2) => self ( )
        #v3 (x3-x4, y3-y4) => p2 (0, -300)

        return (self.x*p2.x) + (self.y*p2.y)

    def cross(self, p2):
        return (self.x*p2.y) - (self.y*p2.x)

    def __str__(self):
        return "[ {}, {}]".format(self.x, self.y)

    def getVector(self):
        return [self.x, self.y]

    def getTuple(self):
        t = (self.x, self.y)
        return t

