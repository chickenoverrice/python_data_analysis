#For this problem you are going to simulate growth of fox and rabbit population in a forest.
import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP =300

rabbit = [0]*CURRENTRABBITPOP
fox = [0]*CURRENTFOXPOP

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global rabbit 
    
    for item in rabbit:
        prob = 1.0-float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
        if prob>random.random() and CURRENTRABBITPOP<MAXRABBITPOP:
            rabbit.append(0)
            CURRENTRABBITPOP = len(rabbit)            
        else:
            pass    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global fox

    if CURRENTFOXPOP<10:
        pass
    else:
        for ind in range(len(fox)-1,-1,-1):
            p_hunt = float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
            if p_hunt>random.random() and CURRENTRABBITPOP>10:
                rabbit.pop()
                if float(1)/float(3)>random.random():
                    fox.append(0)
            else:
                if 0.1>random.random():
                    fox.pop(ind)
            CURRENTFOXPOP = len(fox)
            CURRENTRABBITPOP = len(rabbit)                
            
           
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations,fox_populations)

r,f=runSimulation(200)
#pylab.plot(range(len(r)),r)
#pylab.show()
coeff = pylab.polyfit(range(len(r)), r, 2)
print coeff
pylab.plot(pylab.polyval(coeff, range(len(r))))
pylab.show()
#foxGrowth()
#print CURRENTFOXPOP
#
#foxGrowth()
#print CURRENTFOXPOP