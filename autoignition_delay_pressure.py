import cantera as ct 
import numpy as np 
from cantera import *
import matplotlib.pyplot as plt 


pressure = np.linspace(1,5,9)   # Initial pressure in atm

T = 1100    # Initial temperature in Kelvin

species_dict = {'CH4':1, 'O2':2, 'N2':7.52}     # Species dictionary (Reactant side)

# Total time to run simulation
simulation_time = 10    # seconds
step_time = 0.002   # seconds 
time_steps = int(simulation_time/step_time)     # Calculating number of time steps 

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of pressure
for i in pressure:

	gas = ct.Solution('gri30.yaml')
	P = i * 101325     # Converting pressure from atm to Pa
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time

	states = ct.SolutionArray(gas, extra = ['time_ms'])     # Prepearing solution array for each state

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


plt.figure(2)
plt.plot(pressure, Auto_ig_time,'-o',color='blue', label='methane')
plt.grid('on')
plt.xlabel('Pressure [atm]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autoignition delay for variable initial pressure')


# ETHANE

species_dict = {'C2H6':1, 'O2':3.5, 'N2':13.16}     # ethane

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of pressure
for i in pressure:

	gas = ct.Solution('gri30.yaml')
	P = i * 101325     # Converting pressure from atm to Pa
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time

	states = ct.SolutionArray(gas, extra = ['time_ms'])     # Prepearing solution array for each state

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


plt.figure(2)
plt.plot(pressure, Auto_ig_time,'-o',color='red', label='ethane')
plt.grid('on')
plt.xlabel('Pressure [atm]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autoignition delay for variable initial pressure')


# PROPANE

species_dict = {'C3H8':1, 'O2':5, 'N2':18.8} 	# propane

Auto_ig_time = []   # Array for autoignition delay

# Loop for varying values of pressure
for i in pressure:

	gas = ct.Solution('gri30.yaml')
	P = i * 101325     # Converting pressure from atm to Pa
	gas.TPX = T, P, species_dict
	r = ct.IdealGasReactor(gas)
	sim = ct.ReactorNet([r])
	time = 0    # Initial time

	states = ct.SolutionArray(gas, extra = ['time_ms'])     # Prepearing solution array for each state

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


plt.figure(2)
plt.plot(pressure, Auto_ig_time,'-o',color='green', label='propane')
plt.grid('on')
plt.xlabel('Pressure [atm]')
plt.ylabel('Autoignition delay [ms]')
plt.title('Autoignition delay for variable initial pressure')

plt.legend()
plt.show()