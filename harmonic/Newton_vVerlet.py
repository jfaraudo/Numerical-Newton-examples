# -------------------------------------------------------
# NUMERICAL SOLUTION NEWTON EQUATIONS OF MOTION
# VELOCITY VERLET METHOD
# April 2020 Python3 version 
# 
# Very simple example with Harmonic oscillator
# Units (nanoSI): nm, ns, ng, ...
# By Jordi Faraudo 2018
# -------------------------------------------------------

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# Particle submitted to harmonic force
# mass
m = 1.0
# Period in ns
T = 1.0
#frequency
w = 2.0*np.pi/T
#Force constant
k=m*w*w

#Initial condition (position and velocity)
x0=0.1
v0=0.0
# initial Energy
E0=(m/2.0)*v0*v0+(k/2)*x0*x0

#Show data of the program

print('\n--------------------------------------------------------')
print('SIMPLE MD SIMULATION OF A SINGLE PARTICLE IN HARMONIC TRAP')
print('----------------------------------------------------------')
print('Force constant:',k,' N/m')
print('Particle of mass:',m,' ng')
print('Period according to analytical solution of harmonic oscillator:',T,' ns')

# input time step
dt = float(input("\n Time step dt (in ns):\n>"))
# Final time
ntot = int(input("\n Number of time steps:\n>"))
print('Simulation time will be',dt*ntot,' ns')

# create empty array starting at zero with time, position, velocity, acc
t = np.zeros(ntot+1)
x = np.zeros(ntot+1)
v = np.zeros(ntot+1)
a = np.zeros(ntot+1)

#Initial conditions
x[0] = x0
v[0] = v0

#Force and acceleration at t=0
f = -k*x[0]
a[0] = f/m 
   
# Time evolution
print('\n Calculating time evolution...')
for i in range(1, ntot+1):
    print(i)
    
    # Update time
    t[i] = t[i-1]+dt
    
    # New position
    x[i] = x[i-1]+v[i-1]*dt+(1.0/2.0)*a[i-1]*dt*dt
    
    # Calculate Force at new position
    f = -k*x[i]
    # Calculate acceleration from 2nd Law
    a[i] = f/m 
    
    # Velocity at new position
    am=(a[i-1]+a[i])/2.0
    v[i]= v[i-1]+am*dt
    
    #Update time
    t[i] = t[i-1]+dt
    
# plot output
print('Calculation finished. Showing plot with results')

#
# Create a plot with x(t) and v(t)
# 
#plt.plot(t,x, 'ro', t, v, 'bv')
plt.figure(1)

plt.subplot(211)
plt.plot(t,x)
plt.ylabel('x (nm)')

plt.subplot(212)
plt.plot(t,v)
plt.ylabel(' v (nm/ns)')
plt.xlabel('time (ns)')

#create axis
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')
#Show plot in screen
plt.show()
#Show plot of phase space
plt.plot(x,v,'k')
plt.xlabel('x (nm)')
plt.ylabel('v (nm/ns)')
#Show plot in screen
plt.show()
#Also plot energy
#energy at all steps
E=(m/2.0)*v*v+(k/2)*x*x
#Relative value (E/E0)
RE=E/E0
plt.plot(t,RE,'k')
plt.xlabel('time (ns)')
plt.ylabel('E/E0')
#Show plot in screen
plt.show()
