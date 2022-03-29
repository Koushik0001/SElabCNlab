import sys
import matplotlib.pyplot as plt #This package is used for data visualization
import random #This is used to genarate random numberes

##############################################################################################
                        # General Functions Needed for The Overall Implimentation #
def factorial(number):
    """Returns the factorial of a number i.e. factorial(n) = n!"""
    if number == 1:
        return 1
    elif number == 0:
        return 1
    else:
        return (number * factorial(number-1))


def combination(n,k):
    """Returns the number of combinations possible by chossing k number of objects from n objects i.e. combination(n,k) = nCk = n! / (k! * (n-k)!) """
    return (factorial(n)/(factorial(k)*factorial(n-k)))


def get_Input(index):
    """Processes the index-th command line argument and returns the floating point value for(x/y), that is if the 2nd argument is 1/2, then get_Input(2) = 0.5"""
    return (int(sys.argv[index][0])/float(sys.argv[index][2]))


def frandom():
    """Returns a random integer number in the range [0,                      denominator_of_the_2nd_Commandline_Argument-1] i.e if the second commandline argument is 1/4 then the function genarates random numbers from the set {0,1,2,3} that is the range [0, 4-1] = [0,3]"""
    return random.randint(0,int(sys.argv[2][2])-1)
##############################################################################################

##############################################################################################
                                # Class Binomial_experiment #
class Binomial_experiment():
    """This class models a binomial experiment"""
    def __init__(self,n,p):
        """This is a constructor for the class, this initializes the two parameters of a binomial experiment"""
        self.n = n
        self.p = p
    
    def binomial(self,k=0):
        """This function returns the probability of getting a certain number(k) of success(es) i.e. P(k) = nCk * (p^k) * ((1-p)^(n-k))"""
        nCk = combination(self.n,k)
        return (nCk * (self.p**k) * ((1-self.p)**(self.n-k)))
    
    def plot(self):
        """This function plots the probability_mass_function of descrete random variable number_of_success(k)i.e. y = p(x) = P(k = x) where, (0 <= x <= numberOfToss)"""
        x_values = list(range(0,self.n+1))
        y_values = [self.binomial(k) for k in x_values]
        plt.axis([0,self.n,0,1])
        plt.xlabel("Number of Success(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Binomial Experiment(p = "+ str(self.p) + ", n = " + str(self.n) + ")",fontsize = 18)
        plt.scatter (x_values,y_values)
        plt.show()
##############################################################################################


##############################################################################################
                                    # Class Coin_Toss #
class Coin_Toss():
    def __init__(self, n):
        """This class models a coin toss experiment"""
        self.numberOfToss = n
        self.highestIndexInList = 0
        self.probabilityMassList = list(0 for i in range(0,n+1))
    
    def toss(self):
        """This function simultes a number of repeated coin tosses using frandom() fuction defined above and calculates the probability for each k (number of success) and stores the probabilities in the 'probabilityMassList' """
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
        """This function plots the probability_mass_function of descrete random variable number_of_success(k) i.e. y = p(x) = P(k = x) where, (0 <= x <= numberOfToss)"""
        x_values = list(range(0,self.numberOfToss+1))
        y_values = self.probabilityMassList
        plt.axis([0,self.numberOfToss,0,1])
        plt.xlabel("Number of Success(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Coin Toss Experiment(n = "+ str(self.numberOfToss) +")",fontsize = 18)
        plt.scatter(x = x_values,y = y_values)
        plt.show()
##############################################################################################

coin_Toss = Binomial_experiment(n = int(sys.argv[1]),p = get_Input(2))
coin_Toss.plot()
#
cointoss = Coin_Toss(int(sys.argv[1]))
cointoss.toss()
cointoss.plot()


