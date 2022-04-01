################################################################################################
#                           Team No.08
#
#   Name :  Koushik Mahanta (Roll :  002011001106)
#   Name :  Rimil Murmu     (Roll :  002011001039)
#   Name :  Prince Jain     (Roll :  002011001119)
#   Name :  Aman Kumar Shaw (Roll :  002011001136)
#
#
################################################################################################


################################################################################################
#*******************
#Assignment Details:
#*******************
#   This assignment has three parts :
#       1.  The first part is about printing the probabilities for different values of success
#   (k) for a Binomial Experiment using the probability mass function for Binomial Exeriment,  
#   the parameters n and p are provided, where n is number of times an experiment is repeated  
#   and p is probability of success for a single experiment. 
#  
#       2.  The second part is about simulating coin toss through program.Random number     
#   generator function is used for this purpose. 
#
#       3.  The third or last part of the assignment is about tossing the coin physically. To 
#   do that three unbiased coin (Rs 5 or 10) of same type are taken and tossed together. The 
#   outcome is recorded (H or T). This process is repeated 8 times. Now, the probabilities for 
#   0, 1, 2 and 3 Heads are computed
#
#
#******************
#Input Description:
#****************** 
#        Thisprogram will accept two arguments; the first one is the number of trials (n) and 
#   the second one is the probability of success (p). The value of the first argument should be 
#   at least 3. The value of the 2nd argument should be less than 1 and to be entered as 1⁄2, 
#   1⁄3, 1⁄4, 1⁄5 etc.All these arguments will be taken from command line.  
#
#
#*******************
#Output Description:
#*******************
#       This program will plot a bar diagrams taking the number of successes and Number of 
#   heads on the x axis and their corresponding probabilities on the y axis for the part1 and
#   part2 of the assingnment accordingly.
#       For part3 also a bar diagram will plotted keeping the number of heads on the x axis and 
#   their corresponding probabiolities on the y axis.
#
################################################################################################


################################################################################################
#  Put the execution sequence.
################################################################################################

################################################################################################
#*************
#Sample Input:  python3 08_2.py 10 1/2
#*************
#
#*****************
#Output generated:  This will output three plots corresponding to each of the three parts of 
#*****************  the assignment
#
################################################################################################

################################################################################################
#                       #   Importing Python Libraries   #
#
from logging import exception   #Exception class is used here as a superclass for the custom  Exception Clsses
import sys
import random
from turtle import color
import numpy
from matplotlib import style                   #This is used to genarate random numberes
import matplotlib.pyplot as plt #This library is used for data visualization


################################################################################################
                        # Custom Exception Classes #

class InvalidInput(Exception):
    """Exceptions raised due to invalid intput"""
    pass

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

class ZeroProbabilityException(Exception):
    """The second argument that indicates the probability can not be zero(0)"""
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


def getFractionNumber(index=2):
    """Processes the index-th command line argument and returns the floating point value for(x/
    y), that is if the 2nd argument is 1/2, then get_Input(2) = 0.5"""
    (numerator,denominator) = sys.argv[index].split('/')
    numerator = int(numerator)
    denominator = int(denominator)
    smallest = min(numerator, denominator)
    for i in range(2,smallest+1):
        if numerator%i == 0 and denominator%i == 0:
            while numerator%i == 0 and denominator % i == 0:
                numerator/=i
                denominator/= i
    return (float(numerator)/float(denominator))


def frandom():
    """Returns a random integer number in the range [0,                      
    denominator_of_the_2nd_Commandline_Argument-1] i.e if the second commandline argument is 1/
    4 then the function genarates random numbers from the set {0,1,2,3} that is the range [0, 
    4-1] = [0,3]"""
    (numerator,denominator) = sys.argv[2].split('/')
    numerator = int(numerator)
    denominator = int(denominator)
    smallest = min(numerator, denominator)
    for i in range(2,smallest+1):
        if numerator%i == 0 and denominator%i == 0:
            while numerator%i == 0 and denominator % i == 0:
                numerator/=i
                denominator/= i
    return random.randint(0,denominator-1)

def multiplot(x_axis1,y_axis1,x_axis2,y_axis2):
    fig , (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2)
    ax1.bar(x_axis1,y_axis1)
    ax2.bar(x_axis2,y_axis2)
    fig.show()
################################################################################################

################################################################################################
                                # Class Binomial_experiment #
class Binomial_experiment():
    """This class models a binomial experiment"""
    def __init__(self,n,p):
        """This is a constructor for the class, this initializes the two parameters of a 
        binomial experiment n and p"""
        self.n = n
        self.p = p
    
    def binomial(self,k=0):
        """This function returns the probability of getting a certain number(k) of success(es) 
        i.e. P(k) = nCk * (p^k) * ((1-p)^(n-k))"""
        nCk = combination(self.n,k)
        return (nCk * (self.p**k) * ((1-self.p)**(self.n-k)))
    
    def get_xvalues(self):
        return list(range(0,self.n+1))
    def get_yvalues(self):
        return list(self.binomial(k) for k in range(0,self.n+1))
    def plot(self):
        """This function plots the probability_mass_function of descrete random variable 
        number_of_success(k)i.e. y = p(x) = P(k = x) where, (0 <= x <= numberOfToss)"""
        x_values = self.get_xvalues()
        y_values = self.get_yvalues()
        plt.xlabel("Number of Success(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Binomial Experiment(p = "+str(self.p)+", n = "+str(self.n)+")",fontsize = 18)
        plt.bar(x_values,y_values)
        plt.show()
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
    
    def get_xvalues(self):
        return list(range(0,self.numberOfToss+1))
    def get_yvalues(self):
        return self.probabilityMassList

    def plot(self):
        """This function plots the probability_mass_function of descrete random variable 
        number_of_success(k) i.e. y = p(x) = P(k = x) where, (0 <= x <= numberOfToss)"""
        x_values = self.get_xvalues()
        y_values = self.get_yvalues()
        style.use("ggplot")
        plt.yticks(y_values)
        plt.xticks(x_values)
        plt.figure(figsize = (10,8))
        plt.bar(x_values,y_values,width=0.5,edgecolor = "w",color = "g", alpha = 0.8)
        for x in x_values:
            plt.text(x-0.14,y_values[x]+0.004,"{:.3}".format(y_values[x]),color = "black",fontweight = "bold",horizontalalignment = "center")
        plt.xlabel("Number of Heads(k)",fontsize = 15)
        plt.ylabel("Probability( P(k) )",fontsize = 15)
        plt.title("Coin Toss Simulation(Number Of Toss = "+str(self.numberOfToss)+")",fontsize = 18)
        plt.show()
################################################################################################


################################################################################################
                            # Main Body of The Program #
try:
    if( len(sys.argv)< 3):
        raise InsufficientArguments()
    elif(sys.argv[2].find('/') == -1):
        raise InvalidInput()
    elif(int(sys.argv[1])<3 or getFractionNumber(2)>=1):
        raise InapproriateValue() 
    elif(getFractionNumber(2) == 0):
        raise ZeroProbabilityException
except ZeroDivisionError:   #get_Input() function can raise a ZeroDivisionError
    print("The denominator of the second argument cannot be zero...")
    sys.exit()
except InsufficientArguments:
    print("Insufficient CommandLine arguments...")
    print("Two arguments are needed to execute the program...")
    sys.exit()
except InvalidInput:
    print("Second argument should be provided in the form p/q,")
    print("where,{p,q} belongs to set of Integer numbers and q != 0")
    sys.exit()
except InapproriateValue:
    print("Inappropriate Input...")
    print("The 1st argument should be at least 3 and the 2nd argument should be less than 1...")
    sys.exit()
except ZeroProbabilityException:
    print("The second argument that signifies the probability cannot be zero.")
except IndexError:
    print("Second argument should be provided in the form p/q,")
    print("where,{p,q} belongs to set of Integer numbers and q != 0")
else:
    #Part 1
    theoreticalExperiment = Binomial_experiment(n = int(sys.argv[1]),p = getFractionNumber(2))
    #theoreticalExperiment.plot()

    #part 2
    cointossSimulation = Coin_Toss(int(sys.argv[1]))
    cointossSimulation.toss()
    #cointossSimulation.plot()

    multiplot(theoreticalExperiment.get_xvalues,theoreticalExperiment.get_yvalues,cointossSimulation.get_xvalues,cointossSimulation.get_yvalues)