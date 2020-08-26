import numpy as np
import random

class SynapseLayer:
    def __init__(self,previosSize,nextSize,functionStartValue,rangeValue):
       self.N = previosSize
       self.M = nextSize
       self.functionStartValue = functionStartValue
       self.Layer = np.zeros((self.N,self.M))
       self.rangeValue = rangeValue
       for i in range(0,self.N):
           for j in range(0,self.M):
               self.Layer[i][j] = self.functionStartValue()

    def Mutation(self,baseLayer):
        for i in range(0,self.N):
           for j in range(0,self.M):
               self.Layer[i][j] = baseLayer[i][j] + random.randint(-self.rangeValue,self.rangeValue)

#Test
if __name__ == "__main__":
    obj = SynapseLayer(4,4,lambda: random.randint(-100,100),4)
    print(obj.Layer)
    obj.Mutation(obj.Layer)
    print(obj.Layer)


    
               
