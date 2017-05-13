# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    final = [0.0 * num for num in range(numTrials)]


    for i in range(numTrials):
        total = 0.0
        virus = [ ResistantVirus(0.1, 0.05,{'guttagonol': False},0.005) for _ in range(100)]
        patient = TreatedPatient(virus, 1000)
        for _ in range(150):
            total = patient.update()
        patient.addPrescription("guttagonol")   
        for _ in range(150):
            total = patient.update()
        final[i] = total
      
    num_bins = 10
    pylab.hist(final, num_bins)
    pylab.show()   


#simulationDelayedTreatment(300)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    final = [0 * num for num in range(numTrials)]
    count = 0
    delay = 300
    for i in range(numTrials):
        total = 0
        virus = [ ResistantVirus(0.1, 0.05,{'guttagonol': False, 'grimpex': False},0.005) for _ in range(100)]
        patient = TreatedPatient(virus, 1000)
        for _ in range(150):
            total = patient.update()
        patient.addPrescription("guttagonol")   
        for _ in range(delay):
            total = patient.update()
        patient.addPrescription("grimpex")   
        for _ in range(150):
            total = patient.update()
        if total <= 50:
            count+=1
                 
        final[i] = total
    print "delay:", delay
    print "var:",numpy.var(final)
    print "count:",count
    #num_bins = 10
    #pylab.hist(final, num_bins)
    #pylab.show()   

#simulationTwoDrugsDelayedTreatment(200)
pylab.plot([0,75,150,300],[170,94,20,9])
pylab.show()