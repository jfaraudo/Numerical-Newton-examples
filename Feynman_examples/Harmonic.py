# -------------------------------------------------------
# NUMERICAL SOLUTION NEWTON EQUATIONS OF MOTION
# Example Feynman book Chapter 9 section 9.6
# https://www.feynmanlectures.caltech.edu/I_09.html
# Simple harmonic motion with k/m =1
#
# Python3 code By Jordi Faraudo
# -------------------------------------------------------

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Initial condition (position and velocity)
x0=1.0
v0=0.0

#Show data of the program

print('\n--------------------------------------------------------')
print('SIMPLE MD SIMULATION OF A SINGLE PARTICLE IN HARMONIC TRAP')
print('----------------------------------------------------------')
print('Feynman Example with k/m=1')

# input time step
dt = float(input("\n Time step dt (in the book dt=0.1 sec):\n>"))
# Final time
ntot = int(input("\n Number of time steps (in the book 16 steps):\n>"))

print('Simulation time will be',dt*ntot,' sec')

# create empty array starting at zero with time, position, velocity
x = np.zeros(ntot+1)
v = np.zeros(ntot+1)
t = np.zeros(ntot+1)

#Initial conditions
t[0] = 0.0
x[0] = x0
v[0] = v0

#First step requires specific treatment
#
#  Calculate acceleration and new velocity after time dt/2
a = -x[0]
v_hk = v[0]+(dt/2.0)*a
# New position and acceleration at step 1 time t+dt (Feynman call it special equation)
x[1] = x[0]+dt*v_hk
t[1] = t[0]+dt
i=1
#  
# Time evolution Loop (see eq. 9.16)
#
print('\n Calculating time evolution...')
while i<ntot:
	#print current data
    print('Step',i,' t= ',round(t[i],3),' x=',round(x[i],3))
    # Calculate acceleration at present position x(t)
    a = -x[i]
	# Velocity change from t-dt/2 to t+dt/2
    v_hk = v_hk+a*dt
    # New position at t+dt
    x[i+1] = x[i]+dt*v_hk
    #Update time
    t[i+1] = t[i]+dt
    #update counter
    i=i+1
    
print('Final Step', i,' t= ',round(t[i],3),' x=',round(x[i],3))
# plot output
print('\nShowing plot with results')

#Calculate analytical solution
x2 = np.cos(t)

#
# Create a plot with x(t) 
# 
plt.plot(t,x, 'ro',t,x2, '-')

plt.ylabel('position x')
plt.xlabel('time')
plt.legend(['Numerical', 'Analytical'])

#Show plot in screen
plt.show()

