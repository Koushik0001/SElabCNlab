################################################################################################

#   Name :  Koushik Mahanta
#   Roll :  002011001106
#   Team No.08

#   Name :  Rimil Murmu
#   Roll :  002011001039
#   Team No.08

#   Name :  Prince Jain
#   Roll :  002011001119
#   Team No.08

#   Name :  Aman Kumar Shaw
#   Roll :  002011001136
#   Team No.08

################################################################################################

################################################################################################
#ASSIGNMENT DETAILS:    
#This assignment has three parts :
#   1.The first part is about printing the probabilities for different values of success(k) for a Binomial Experiment using the probability mass function for Binomial Exeriments provided the paramenters n and p, where n of times an experiment is repeatedsthe results Input Description, Output Description.
################################################################################################

################################################################################################
#  Put the execution sequence.
################################################################################################

################################################################################################
#  Put Sample Input and Output generated
################################################################################################

################################################################################################

from decimal import Decimal
from logging import exception   #Exception class is used here as a superclass for the custom  Exception Clsses
import sys
import random                   #This is used to genarate random numberes

################################################################################################
                        # Custom Exception Classes #

class InsufficientArguments(Exception):
    """Exceptions raisd due to insufficient number of commandline arguments"""
    pass

class InapproriateValue(Exception):
    """
        Exceptions raised due to illigal input
        The first argument should be greater than or equal to  3
        The second argument should be less than 1
    """
    pass

################################################################################################

################################################################################################
                # General  Purpose Functions Needed for The Overall Implimentation #
def factorial(number):
    """Returns the factorial of a number i.e. factorial(n) = n!"""
    if number == 1:
        return 1
    elif number == 0:
        return 1
    else:
        return (number * factorial(number-1))


def combination(n,k):
    """Returns the number of combinations possible by chossing k number of objects from n 
    objects i.e. combination(n,k) = nCk = n! / (k! * (n-k)!) """
    return (factorial(n)/(factorial(k)*factorial(n-k)))


def returnDenominator(number):
    """Returns denominator after converting a floating point numbet into a rational number
        for example. if 0.5 is passed as the argument then 2 will be returned"""
    if(number == 0.33):
        return 3
    else:
        num = Decimal(number)
        (numerator, denominator) = num.as_integer_ratio()
        return denominator


def frandom():
    """Returns a random integer number in the range [0,                      
    denominator_of_the_2nd_Commandline_Argument-1] i.e if the second commandline argument is 1/
    4 then the function genarates random numbers from the set {0,1,2,3} that is the range [0, 
    4-1] = [0,3]"""
    return random.randint(0,returnDenominator(sys.argv[2])-1)
################################################################################################

################################################################################################
                                # Class Binomial_experiment #
class Binomial_experiment():
    """This class models a binomial experiment"""
    def __init__(self,n,p):
        """This is a constructor for the class, this initializes the two parameters of a 
        binomial experiment"""
        self.n = n
        self.p = p
    
    def binomial(self,k=0):
        """This function returns the probability of getting a certain number(k) of success(es) 
        i.e. P(k) = nCk * (p^k) * ((1-p)^(n-k))"""
        nCk = combination(self.n,k)
        return (nCk * (self.p**k) * ((1-self.p)**(self.n-k)))
    
    def printProbabilities(self):
        print("Binomial Experiment (Theoretical)")
        print("Number of Success           Probability")
        for k in range(0,self.n):
            print("       " + str(k) + "                    " + str(self.binomial(k)))
    
################################################################################################


################################################################################################
                                    # Class Coin_Toss #
class Coin_Toss():
    def __init__(self, n):
        """This class models a coin toss experiment"""
        self.numberOfToss = n
        self.highestIndexInList = 0
        self.probabilityMassList = list(0 for i in range(0,n+1))
    
    def toss(self):
        """This function simultes a number of repeated coin tosses using frandom() fuction 
        defined above and calculates the probability for each k (number of success) and stores 
        the probabilities in the 'probabilityMassList' """
        for i in range(0,(2**self.numberOfToss)):
            success = 0
            for j in range(0,self.numberOfToss):
                result = frandom()
                if result == 0:
                    success+=1
            self.probabilityMassList[success] += 1
        for i in range(0,self.numberOfToss+1):
            self.probabilityMassList[i] /= (2**self.numberOfToss)
    
    def printProbabilities(self):
        print("Coin Toss Experiment (Simulatoin)")
        print("Number of Success           Probability")
        for k in range(0,self.numberOfToss):
            print("       " + str(k) + "                    " + str(self.probabilityMassList[k]))
################################################################################################

################################################################################################
                            # Main Body of The Program #
try:
    if( len(sys.argv)< 3):
        raise InsufficientArguments()
    elif(int(sys.argv[1])<3 or float(sys.argv[2])>=1):
        raise InapproriateValue()
except InsufficientArguments:
    print("Insufficient CommandLine arguments...")
    print("Two arguments are needed to execute the program...")
    sys.exit()
except InapproriateValue:
    print("Inappropriate Input...")
    print("The 1st argument should be at least 3 and the 2nd argument should be less than 1...")
    sys.exit()
else:
    theoreticalExperiment = Binomial_experiment(n = int(sys.argv[1]),p = float(sys.argv[2]))
    theoreticalExperiment.printProbabilities()
    print("_______________________________________________")
    print()

    cointossSimulation = Coin_Toss(int(sys.argv[1]))
    cointossSimulation.toss()
    cointossSimulation.printProbabilities()