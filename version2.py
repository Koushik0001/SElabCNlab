import sys
import matplotlib.pyplot as plt
import random

##############################################################################################
def factorial(number):#returns the factorial of a number
        if number == 1:
            return 1
        elif number == 0:
            return 1
        else:
            return (number * factorial(number-1))

def combination(n,k):#returns nCr
    return (factorial(n)/(factorial(k)*factorial(n-k)))

def get_Input(index):
    return (int(sys.argv[index][0])/float(sys.argv[index][2]))

def frandom():
    return random.randint(0,int(sys.argv[2][2])-1)
##############################################################################################

class Binomial_experiment():
    def __init__(self,n,p):
        self.n = n
        self.p = p
    
    def binomial(self,k=0):
        nCk = combination(self.n,k)
        return (nCk * (self.p**k) * ((1-self.p)**(self.n-k)))
    
    def plot(self):
        x_values = list(range(0,self.n+1))
        y_values = [self.binomial(k) for k in x_values]
        plt.axis([0,self.n,0,1])
        plt.xlabel("Number of Success(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Binomial Experiment(p = "+ str(self.p) + ", n = " + str(self.n) + ")",fontsize = 18)
        plt.plot (y_values)
        plt.show()
##############################################################################################


##############################################################################################
class Coin_Toss():
    def __init__(self, n):
        self.numberOfToss = n
        self.highestIndexInList = 0
        self.probabilityMassList = list(0 for i in range(0,n+1))
    
    def toss(self):
        for i in range(0,(2**self.numberOfToss)):
            success = 0
            for j in range(0,self.numberOfToss):
                result = frandom()
                if result == 0:
                    success+=1
            self.probabilityMassList[success] += 1
        
        for i in range(0,self.numberOfToss+1):
            self.probabilityMassList[i] /= (2**self.numberOfToss)
    
    def plot(self):
        y_values = self.probabilityMassList
        plt.axis([0,self.numberOfToss,0,1])
        plt.xlabel("Number of Success(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Coin Toss Experiment(n = "+ str(self.numberOfToss) +")",fontsize = 18)
        plt.plot (y_values)
        plt.show()
##############################################################################################

coin_Toss = Binomial_experiment(n = int(sys.argv[1]),p = get_Input(2))
coin_Toss.plot()

cointoss = Coin_Toss(int(sys.argv[1]))
cointoss.toss()
cointoss.plot()

#print(str(int(1/0.25)))
