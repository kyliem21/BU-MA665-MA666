
"""
Created on Fri Sep 28 10:56:55 2018

@author: Wilmerding

This code models the F-I curve of the Leaky Integrate and Fire Neuron
as discussed in class. 

Leaky integrator model: 
    dV/dt = -(Vin + V*)/Tau

Solved for v(t) and transformed into instantaneous firing rate, fRate:
    fRate = 1.0/((Tau)*ln(R*I/(R*I-Vth)))

I pulled this version of the equation from: 
    http://www.cns.nyu.edu/~eorhan/notes/lif-neuron.pdf
    
I am not 100% clear on the calculus/algebra needed to arrive at this form
of the equation -- perhaps our more mathematically minded people could help 
by posting a solution?
As it is, this equation nicely models the F-I curve of the LIF.

As can be seen in the graph, the function is nonlinear. I introduced
conditional statements to prevent division by zero in cases where the input
current I is not high enough to provoke 'spiking' activity and thus the 
fRate is manually set to 0. See annotations in the code.

For fun, variables can be experimented with to examine the effect on the firing
rate of the model.

"""

#Import modules
import numpy as np
import matplotlib.pyplot as plt

#Initialize variables 
R = 1.0     #Resistance
C = 1.0     #Capacitance
Vth = 1.0   #'spike' threshold

#Create holder variable for each output fRate
fRateVector = []
#Define the range of current (I) values to test and plot
iRange = np.linspace(0,10,100)

#Test each I value
for i in range(0,len(iRange)):
    ri = R*i    #Define Resistance * Current
    if ri == 0 or ri-Vth == 0:
        #In cases where current does not bring membrane voltage to threshold...
        fRateVector = fRateVector + [0] #Set firing rate manually to 0
    else:
        fRate = 1.0/((R*C)*np.log(ri/(ri-Vth))) #Calculate firing rate
        fRateVector = fRateVector + [fRate]     #Store fRate in holder
    
#Create graphs...
plt.figure()
plt.plot(iRange,fRateVector)
plt.ylabel('Firing Rate (spike frequency)')
plt.xlabel('Current (Amps)')
plt.title('F-I Curve for Leaky Integrator')
