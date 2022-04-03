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
#        Thisprogram will accept three arguments; the first one is the number of trials (n), 
#   the second one is the probability of success (p) and the third one is the experimental 
#   multiplier. The value of the first argument should be at least 3. The value of the 2nd 
#   argument should be less than 1 and to be entered as 1⁄2, 1⁄3, 1⁄4, 1⁄5 etc. and the third 
#   argument should be greater than or equal to 1. All these arguments will be taken from       
#   command line.  
#
#
#*******************
#Output Description:
#*******************
#       This program will plot a bar diagrams taking the number of successes and Number of 
#   heads on the x axis and their corresponding probabilities on the y axis for the part1 and
#   part2 of the assingnment accordingly.
#
################################################################################################


################################################################################################
#  Execution sequence : python3 08_2.py <number_of_experiments> <Probability_of_success> <Experimental_Multiplier>
################################################################################################

################################################################################################
#*************
#Sample Input:  python3 08_2.py 10 1/2 3
#*************
#
#*****************
#Output generated:  
#*****************
#       This will output two plots corresponding to each of the first two parts of the 
#   assignment, that is it visualizes the probabilities for each k(number of success) using the 
#   fomula and also shows the results of a coin toss simulation experiment using pythons 
#   visualisation tools.
#
################################################################################################

################################################################################################
#                       #   Importing Python Libraries   #
#
from fractions import Fraction  #Fraction method help in conversion between rational and decimal numbers
from logging import exception   #Exception class is used here as a superclass for the custom  Exception Clsses
import sys
import random                   #This is used to genarate random numberes
from matplotlib import style    #This helps to customise the plots             
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


def getProbability(index=2):
    """Processes the index-th command line argument and returns the floating point value for(x/
    y), that is if the 2nd argument is 1/2, then get_Input(2) = 0.5"""
    return (Fraction(sys.argv[2]).numerator/Fraction(sys.argv[2]).denominator)

def multiplot(x_axis1,y_axis1,x_axis2,y_axis2):
    """This function takes two sets of lists containg the x and y values that it uses toplt two 
    bar vplots in the same figure"""
    fig = plt.figure(figsize= (11,8))
    plt.suptitle("Binomial Experiment  n = "+ sys.argv[1] + " ,p = " + sys.argv[2] + " ,experiment multiplier = " + sys.argv[3])
    #plt.suptitle gives the figure object a title
    style.use("ggplot")#Determines the style of the plots

    #two different subplots are added in the figure
    ax1 = fig.add_axes([0.1,0.1,0.3,0.8])
    ax2 = fig.add_axes([0.6,0.1,0.3,0.8])

    #assigns a title to each of the sub-plots and assigns x_label and y_label to their axes
    ax1.set(title = "Theoretical Binomial Experiment", xlabel = " x = Number of success(k)", ylabel = "y = p(x) = Probability of k number of successes")
    ax2.set(title = "Simulated Coin Toss Experiment", xlabel = " x = Number of heads/ experiment",ylabel = "y = p(x) = Number of Occurences of k_number_of_Heads")

    #The following for loops prints the y_values corresponding to each bar inside or ouside of the bars
    for x in x_axis1:
        if y_axis1[x]-0.02 >0:
            ax1.text(x,y_axis1[x]-0.02,"{:.3}".format(y_axis1[x]),color = "black",fontweight = "bold",rotation = 90,va = "center",ha = "center")
        else:
            ax1.text(x,y_axis1[x],"{:.3}".format(y_axis1[x]),color = "black",fontweight = "bold",rotation = 90,va = "bottom",ha = "center")

    formatv = max(y_axis2)/10
    for x in x_axis2:
        if y_axis2[x]-formatv >0:
            ax2.text(x,y_axis2[x]-formatv,"{:d}".format(y_axis2[x]),color = "black",fontweight = "bold",rotation = 90,va = "center",ha = "center")
        else:
            ax2.text(x,y_axis2[x],"{:d}".format(y_axis2[x]),color = "black",fontweight = "bold",rotation = 90,va = "bottom",ha = "center")

    #This part provides the lists containig the x and y values to the bar() function to facilitate the plotting
    ax1.bar(x_axis1,y_axis1,width = 0.97,edgecolor = "white")
    ax2.bar(x_axis2,y_axis2,color = "green",width = 0.98,edgecolor = "white")

    #providing the x_ticks and y_ticks for ax1 Axis object
    ax1.set_xticks(x_axis1)
    ax1.set_yticks(y_axis1)
    ax1.set_yticklabels(list(Fraction(i) for i in y_axis1 ))

    #providing the x_ticks for ax2 Axis object
    ax2.set_xticks(x_axis2)

    #Showing the plots
    plt.show()
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
################################################################################################


################################################################################################
                                    # Class Coin_Toss #
class Coin_Toss():
    """This class models a coin toss experiment"""
    def __init__(self, n):
        self.numberOfToss = n
        self.ResultList = list(0 for i in range(0,n+1))
    
    def toss(self):
        """This function simultes a number of repeated coin tosses using frandom() fuction 
        defined above and calculates the probability for each k (number of success) and stores 
        the probabilities in the 'ResultList' """
        for i in range(0,(2**self.numberOfToss)*int(sys.argv[3])):
            success = 0
            for j in range(0,self.numberOfToss):
                result = random.randint(0,Fraction(sys.argv[2]).denominator-1)
                if result == 0:
                    success+=1
            self.ResultList[success] += 1
    
    def get_xvalues(self):
        return list(range(0,self.numberOfToss+1))
    def get_yvalues(self):
        return self.ResultList
################################################################################################


################################################################################################
                            # Main Body of The Program #
try:
    if( len(sys.argv)< 3):
        raise InsufficientArguments()
    elif(sys.argv[2].find('/') == -1):
        raise InvalidInput()
    elif(int(sys.argv[1])<3 or getProbability(2)>=1):
        raise InapproriateValue() 
    elif(getProbability(2) == 0):
        raise ZeroProbabilityException
    elif(int(sys.argv[3])<1):
        print("The third argument(Experimental multiplioer) must be >= 1")
        sys.exit()
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
    theoreticalExperiment = Binomial_experiment(n = int(sys.argv[1]),p = getProbability(2))

    #part 2
    cointossSimulation = Coin_Toss(int(sys.argv[1]))
    cointossSimulation.toss()

    multiplot(theoreticalExperiment.get_xvalues(),theoreticalExperiment.get_yvalues(),cointossSimulation.get_xvalues(),cointossSimulation.get_yvalues())
