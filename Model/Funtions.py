import math
def length(v1):
    #assumes v1 starts at (0,0)
    return math.sqrt(v1.x*v1.x + v1.y*v1.y)

def normalize(v1):
    #assumes v1 starts at (0,0)
    v1 = v1 / length(v1)
    return v1