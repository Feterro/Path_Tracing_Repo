import math
from Model.Segmento import Segmento
def length(v1):
    #Assumes v1 starts at (0,0)
    return math.sqrt(v1.x * v1.x + v1.y * v1.y)

def pointsDistance(v1, source):

    return math.sqrt((source.x - v1.x)**2 + (source.y - v1.y)**2)

def normalize(v1):
    #assumes v1 starts at (0,0)
    v1 = v1 / length(v1)
    return v1

def getArrayImage():
    imgName = "C:/Users/edfsedf/Documents/GitHub/Path_Tracing_Repo/Model/test.png"
    from PIL import Image
    import numpy as np

    # reference image for background color
    im_file = Image.open(imgName)
    ref = np.array(im_file)
    return ref