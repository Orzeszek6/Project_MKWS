import cantera as ct 
import numpy as np 
from cantera import *
import matplotlib.pyplot as plt 


temp = np.linspace(950,1250,7)    # Initial temperature in K

P = 5*101325    # Initial pressure in Pa

species_dict = {'CH4':1, 'O2':2, 'N2':7.52}     # methane

# Total time to run simulation
simulation_time = 10    #seconds
step_time = 0.002    #seconds 
time_steps = int(simulation_time/step_time)     # Calculating number of timesteps

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of initial temperature
for T in temp:

	gas = ct.Solution('gri30.yaml')
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time
	
	states = ct.SolutionArray(gas, extra = ['time_ms']) 	# Prepearing solution array for each state

	loop_counter = 0

	# Time loop (Time integration for states)
	for n in range(time_steps):
		time += step_time
		
		# Advancing time
		sim.advance(time)
		states.append(r.thermo.state, time_ms = time/step_time)

		
		# Loop to calculate ignition delay
		# Time required to ignition delay = Time for acheiving_(initial temprature + 400k)
		if ((states.T[n] >= (T + 400)) and loop_counter == 0):

			Auto_ig_time.append(states.time_ms[n])
			print (Auto_ig_time)

			loop_counter = 1


plt.figure(1)
plt.plot(temp, Auto_ig_time,'-o',color='blue', label='methane')
plt.grid('on')
plt.xlabel('Initial temperature [K]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autognition delay for variable initial temperature')


# ETHANE

species_dict = {'C2H6':1, 'O2':3.5, 'N2':13.16}  	# ethane

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of initial temperature
for T in temp:

	gas = ct.Solution('gri30.yaml')
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time
	
	states = ct.SolutionArray(gas, extra = ['time_ms']) 	# Prepearing solution array for each state

	loop_counter = 0

	# Time loop (Time integration for states)
	for n in range(time_steps):
		time += step_time
		
		# Advancing time
		sim.advance(time)
		states.append(r.thermo.state, time_ms = time/step_time)

		
		# Loop to calculate ignition delay
		# Time required to ignition delay = Time for acheiving_(initial temprature + 400k)
		if ((states.T[n] >= (T + 400)) and loop_counter == 0):

			Auto_ig_time.append(states.time_ms[n])
			print (Auto_ig_time)

			loop_counter = 1


plt.figure(1)
plt.plot(temp, Auto_ig_time,'-o',color='red', label='ethane')
plt.grid('on')
plt.xlabel('Initial temperature [K]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autoignition delay for variable initial temperature')


# PROPANE

species_dict = {'C3H8':1, 'O2':5, 'N2':18.8} 	# propane

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of initial temperature
for T in temp:

	gas = ct.Solution('gri30.yaml')
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time
	
	states = ct.SolutionArray(gas, extra = ['time_ms']) 	# Prepearing solution array for each state

	loop_counter = 0

	# Time loop (Time integration for states)
	for n in range(time_steps):
		time += step_time
		
		# Advancing time
		sim.advance(time)
		states.append(r.thermo.state, time_ms = time/step_time)

		
		# Loop to calculate ignition delay
		# Time required to ignition delay = Time for acheiving_(initial temprature + 400k)
		if ((states.T[n] >= (T + 400)) and loop_counter == 0):

			Auto_ig_time.append(states.time_ms[n])
			print (Auto_ig_time)

			loop_counter = 1


plt.figure(1)
plt.plot(temp, Auto_ig_time,'-o',color='green', label='propane')
plt.grid('on')
plt.xlabel('Initial temperature [K]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autoignition delay for variable initial temperature')

plt.legend()
plt.show()