# -------------------------------------------------------
# NUMERICAL SOLUTION NEWTON EQUATIONS OF MOTION
# Example Feynman book Chapter 9 section 9.7
# https://www.feynmanlectures.caltech.edu/I_09.html
# Planetary motion with GM=1
#
# Python3 code By Jordi Faraudo
# -------------------------------------------------------

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Initial condition (position and velocity)
x0=0.5
y0=0.0
vx0=0.0
vy0=1.63

#Show data of the program

print('\n----------------------------------')
print('NUMERICAL SOLUTION PLANETARY MOTION')
print('-----------------------------------')
print('Feynman Example 9.7 (arb. units with GM=1)')

# input time step
dt = float(input("\n Time step dt (in the book dt=0.1):\n>"))
# Final time
ntot = int(input("\n Number of steps (in the book 22 steps):\n>"))

print('Simulation time will be',dt*ntot,' time arb. units')

# create empty array starting at zero with time, position, velocity
x = np.zeros(ntot+1)
y = np.zeros(ntot+1)
vx = np.zeros(ntot+1)
vy = np.zeros(ntot+1)
t = np.zeros(ntot+1)

#Initial conditions
t[0] = 0.0
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

#
#First step requires specific treatment
#
#  Calculate acceleration and new velocity after time dt/2
r_sun=np.sqrt(x[0]*x[0]+y[0]*y[0])
ax = -x[0]/(r_sun**3.0)
ay = -y[0]/(r_sun**3.0)
vx_hk = vx[0]+(dt/2.0)*ax
vy_hk = vy[0]+(dt/2.0)*ay
# New position and acceleration at step 1 time t+dt
x[1] = x[0]+dt*vx_hk
y[1] = y[0]+dt*vy_hk
t[1] = t[0]+dt
i=1
#  
# Time evolution Loop (see eq. 9.16)
#
print('\n Calculating time evolution...')
while i<ntot:
	#print current data
    print('t= ',round(t[i],3),' x=',round(x[i],3),' y=',round(y[i],3))
    # Calculate acceleration at present position x(t)
    r_sun=np.sqrt(x[i]*x[i]+y[i]*y[i])
    ax = -x[i]/(r_sun**3.0)
    ay = -y[i]/(r_sun**3.0)
	# Velocity change from t-dt/2 to t+dt/2
    vx_hk = vx_hk+ax*dt
    vy_hk = vy_hk+ay*dt
    # New position at t+dt
    x[i+1] = x[i]+dt*vx_hk
    y[i+1] = y[i]+dt*vy_hk
    #Update time
    t[i+1] = t[i]+dt
    #update counter
    i=i+1
    
print('Step', i,' t= ',round(t[i],3),' x=',round(x[i],3),round(y[i],3))
# plot output
print('\nShowing plot with results')

#
# Create a plot with x(t) 
# 
plt.plot(x,y, 'ro')

plt.xlabel('x')
plt.ylabel('y')

#Show plot in screen
plt.show()

