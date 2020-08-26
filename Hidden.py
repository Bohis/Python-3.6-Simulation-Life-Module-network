import numpy as np
import random,math
import ActivationFunction as AF

class HiddenLayer:
    def __init__(self,sizeValue):
       self.N = sizeValue
       self.Layer = np.zeros((1,self.N))

    def ActivationValue(self):
        for j in range(0,self.N):
               self.Layer[0][j] = AF. ActFncTGH(self.Layer[0][j])

#Test
if __name__ == "__main__":
    obj = HiddenLayer(1)
    obj.Layer[0][0] = 2
    print(obj.Layer)
    obj.ActivationValue()
    print(obj.Layer)
