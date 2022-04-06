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
#        This program will accept three arguments : the first one is the number of trials (n), 
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
#                                               # Part3 #
#
#   Probabilities of Getting k number of heads(H) after tossing 3 similer unbiased Coins Repeatedly:
#       p(k = 0) = 1/8 = 0.125
#       p(k = 1) = 3/8 = 0.375
#       p(k = 2) = 3/8 = 0.375
#       p(k = 3) = 1/8 = 0.125
#
#   Results Of Physical Coin Toss:
#        1 st round : H T H
#        2 nd round : T T H
#        3 rd round : H H H
#        4 th round : H H H
#        5 th round : T T H
#        6 th round : H H H
#        7 th round : T H H
#        8 th round : T H H
#
################################################################################################


################################################################################################
                       #   Importing Python Libraries   #

from fractions import Fraction  #Fraction method help in conversion between rational and decimal numbers
from logging import exception   #Exception class is used here as a superclass for the custom  Exception Clsses
import sys
import random                   #This is used to genarate random numberes
from turtle import color        #This library is for different colours used for plotting         
from matplotlib import style    #This helps to customise the plots             
import matplotlib.pyplot as plt #This library is used for data visualization

################################################################################################


################################################################################################
                        # Custom Exception Classe for Exception Handling#

class InvalidInput(Exception):
    """Exceptions raised due to invalid intput"""
    pass
################################################################################################


################################################################################################
                # General  Purpose Functions Needed for The Overall Implimentation #
def factorial(number):
    """Returns the factorial of a number i.e. factorial(n) = n!"""
    if number == 1:
        return 1        #factorial of 1 is 1, i.e. = 1! = 1
    elif number == 0:
        return 1        #factorial of 0 is defined to be 1, i.e. = 0! = 1
    else:
        return (number * factorial(number-1)) #n! = n * (n-1)!


def combination(n,k):
    """Returns the number of combinations possible by chossing k number of objects from n 
    objects i.e. combination(n,k) = nCk = n! / (k! * (n-k)!) """
    return (factorial(n)/(factorial(k)*factorial(n-k)))


def getProbability():
    """Processes the 2nd command line argument and returns the floating point value for(x/
    y), that is if the 2nd argument is 1/2, then getProbability() = 0.5"""
    return (Fraction(sys.argv[2]).numerator/Fraction(sys.argv[2]).denominator)


def multiplot(x_axis1,y_axis1,x_axis2,y_axis2):
    """This function takes two sets of lists containg the x and y values that it uses to plot 
    two bar plots in the same figure"""
    fig = plt.figure(figsize= (11,8))

    #plt.suptitle gives the figure object a title
    plt.suptitle("Binomial Experiment (n = "+ sys.argv[1] + " ,p = " + sys.argv[2] + ") ,experiment multiplier = " + sys.argv[3],fontsize = 13,fontweight = 'bold',color = 'cornflowerblue')
    style.use("ggplot")#Determines the style of the plots

    #two different subplots are added in the figure
    ax1 = fig.add_axes([0.1,0.1,0.3,0.8])
    ax2 = fig.add_axes([0.6,0.1,0.3,0.8])

    #assigns a title to each of the sub-plots and assigns x_label and y_label to their axes
    ax1.set_xlabel(xlabel = "x = Number of success(k)",color = "firebrick")
    ax1.set_ylabel(ylabel = "y = p(x) = Probability of k number of successes",color = "firebrick")
    ax1.set_title(label = "Theoretical Binomial Experiment",color = "darkorange")

    ax2.set_xlabel(xlabel = " x = Number of heads/experiment",color = "forestgreen")
    ax2.set_ylabel(ylabel = "y = p(x) = Number of Occurences of x_number_of_Heads",color = "forestgreen")
    ax2.set_title(label = "Simulated Coin Toss Experiment",color = "seagreen")

    #The following for loops print the y_values corresponding to each bar inside or ouside of the bars
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
    ax2.bar(x_axis2,y_axis2,color = "limegreen",width = 0.98,edgecolor = "white")

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
        """This function rturns a list of x values necessary for plotting the results of the 
        binomial function[Bin(n,p) = nCk * (p^k) * ((1-p)^(n-k))] for specific n and p values 
        and different k values, here the x values corresponds to k values, i.e. x = k"""
        return list(range(0,self.n+1))

    def get_yvalues(self):
        """This function rturns a list of y values i.e 'ResultList' necessary for plotting the 
        results of the binomial function[Bin(n,p) = nCk * (p^k) * ((1-p)^(n-k))] for specific n 
        and p values and different k values"""
        return list(self.binomial(k) for k in range(0,self.n+1))
################################################################################################


################################################################################################
                                    # Class Coin_Toss #
class Coin_Toss():
    """This class models a coin toss experiment"""
    def __init__(self, n):
        """This constructor initializes variable numberOfToss to be performed and a list which 
        is used to hold the results of the coin toss simulation experiment"""
        self.numberOfToss = n
        self.ResultList = list(0 for i in range(0,n+1))
    
    def toss(self):
        """This function simultes a number of repeated coin tosses using random number 
        generator and calculates the probability for each k (number of success) and stores the 
        probabilities in the 'ResultList' """
        for i in range(0,(2**self.numberOfToss)*int(sys.argv[3])):
            success = 0
            for j in range(0,self.numberOfToss):
                status = 0#this variable is set to 1 if the experiment result is success and 0 if failure

                #this generates a random number and stores it in result 
                result = random.randint(0,Fraction(sys.argv[2]).denominator-1)

                #this checks if result is present in the list, if it is present then status is 
                # set to 1 otherwise 0. For example if the second argument is 3/5 then the 
                # following list contains [0,1,2] now if the result of the random number 
                # generator is one of this three then status = 1 otherwise status = 0
                status =  list(x for x in range(0,Fraction(sys.argv[2]).numerator)).count(result)
                success+=status
            self.ResultList[success] += 1
    
    def get_xvalues(self):
        """This function rturns a list of x values necessary for plotting the results of the 
        simulation experiment"""
        return list(range(0,self.numberOfToss+1))

    def get_yvalues(self):
        """This function rturns a list of y values i.e 'ResultList' necessary for plotting the 
        results of the simulation experiment"""
        return self.ResultList
################################################################################################


################################################################################################
                            # Main Body of The Program #

# following try block checks for exceptions, if found prints the reason and terminates execution
try:
    if( len(sys.argv)< 4):
        raise InvalidInput("Insufficient CommandLine arguments.Usage : 08_2.py <numberOfTriels> <probability> <exp. multiplier>")

    elif(sys.argv[2].find('/') == -1):
        raise InvalidInput("Second argument should be provided in the form p/q, where,{p,q} belongs to set of Integer numbers and q != 0")

    elif(sys.argv[1].find('.') != -1):
        raise InvalidInput("1st argument should a non-Zero Integer...")

    elif(sys.argv[2].find('.') != -1):
        raise InvalidInput("Numerator and Denominator of the 2nd argument should be Integers...")

    elif(sys.argv[3].find('.')!= -1):
        raise InvalidInput("Third argument should be an Integer...")

    elif(int(sys.argv[1])<3):
        raise InvalidInput("1st argument should be greater than or equal to 3")

    elif(getProbability()>=1):
        raise InvalidInput("2nd argument should be less than 1...")

    elif(getProbability() <= 0):
        raise InvalidInput("2nd argument should be greater than zero...")

    elif(int(sys.argv[3])<1):
        raise InvalidInput("3rd argument should be an integer that is greater than or equalto 1")

except ZeroDivisionError:   #getProbability() function can raise a ZeroDivisionError
    print("The denominator of the second argument cannot be zero...")

except InvalidInput as eII:
    print()
    print(eII)  # prints the messege in the exception object, i.e. the reason for the exception
    print()

except ValueError: # catches value error generated by invalid input
    print()
    print("Usage : 08_2.py <numberOfTriels> <probability> <exp. multiplier>")
    print("numberOfTriels >= 3 and it must be an Integer")
    print("0 < probability < 1")
    print("exp. multiplier >= 1 and it must be an Integer")
    print()

# if no exception is caught then the following else block is executed
else: 

                                    # Part 1 #

    # Instantiating Binomial_experiment class
    theoreticalExperiment = Binomial_experiment(n = int(sys.argv[1]),p = getProbability())
                # theoreticalExperiment references an instance of class Binomial_experiment
                # Binomial_experiment(n,p) is the contructor of class Binomial_Experiment
                # n = number_of_trials, p = probability
    

                                    # Part 2 #

    # Instantiating Coin_Toss class
    cointossSimulation = Coin_Toss(n = int(sys.argv[1]))
                # cointossSimulation references an instance of class Coin_Toss
                # Coin_Toss(n) is the constructor of class Coin_Toss 
                # n = number of trials or number of tosses per experiment
    
    # toss() function is called by cointossSimulation Object to perform tosses
    cointossSimulation.toss()

    # the multiplot(x_axis1, y_axis1, x_axis2, y_axis2) is called to plot the results
    multiplot(theoreticalExperiment.get_xvalues(),theoreticalExperiment.get_yvalues(),cointossSimulation.get_xvalues(),cointossSimulation.get_yvalues())
                # get_xvalues() and get_yvalues() are called by the objects to get a list of x 
                # and y values accordingly to facilitate the plotting
