import numpy as np
import Hidden as HL
import Inpyt as IL
import Outpyt as OL
import Synapse as SL
import random,math

learRate = 4
InL = IL.InpytLayer(6)
Sy1L = SL.SynapseLayer(6,5,lambda: random.randint(-2,2),learRate)
HiL = HL.HiddenLayer(5)
Sy2L = SL.SynapseLayer(5,6,lambda: random.randint(-2,2),learRate)
OuL = OL.OutpytLayer(6)

def Calculation(string):
    for i in range(0,InL.Layer.shape[1]):
        InL.Layer[0][i] = string[i]
    HiL.Layer = np.dot(InL.Layer ,Sy1L.Layer)
    HiL.ActivationValue()
    OuL.Layer = np.dot(HiL.Layer , Sy2L.Layer)
    OuL.ActivationValue()
    return OuL.Layer

def Inheritance(baseSy1L,baseSy2L):
    Sy1L.Mutation(baseSy1L)
    Sy2L.Mutation(baseSy2L)
