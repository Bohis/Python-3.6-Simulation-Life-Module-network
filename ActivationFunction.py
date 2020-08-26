import math

def ActFncTGH(x):
    try:
        #y = (math.e**x-1)/(math.e**x+1)
        y = 1/(1+math.exp(-0.1*x))
    except:
        y = 0

    return y

#Test
if __name__ == "__main__":
    print(ActFncTGH(200))
    
