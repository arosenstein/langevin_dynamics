# -*- coding: utf-8 -*-
import random
from math import sqrt
#from scipy.constants import k as k_b

def langevin_dynamics(x_0, v_0, temp, damp, time_step, total_time, mass, potential_energy_filepath, output_file = 'output.txt'):
	'''Completes a 1 dimensional Langevin Dynamics Simulation dependant on an input file of the form:

	INDEX TIME POTENTIAL_ENERGY FORCE 
	
	Input
	-----
	x_0 : float
		initial position

	v_0 : float
		initial velocity

	temp : float
		temperature at which the simulation runs

	damp : float
		dampening coefficient

	time_step : float
		length of the time steps for the simulation

	total_time : float
		total amount of time to run the simulation for

	mass : float
		mass of the simulation particle

	potential_energy_filepath : String
		Relative filepath to the file containing data on potential energy

	output_file : String
		Relative filepath to the output file containing position and velocity data

	Return
	------
	position : float
		final position of the particle after simulation has been run

	velocity : float
		final velocity of the particle after simulation has been run
	'''
	file = read_file(potential_energy_filepath)

	position = x_0
	velocity = v_0

	count = 0

	output = []

	for i in range(int(total_time/time_step)):
		
		index = int(file[count][0])
		time = file[count][1]
		if not count == 0:
			delta_time = time - file[count-1][1]
		else:
			delta_time = 0

		#Calculate the 3 forces:
		drag_force = -velocity * damp
		random_force = random.gauss(0,sqrt(2 * temp * damp))
		potential_force = file[index][3]

		acceleration = (drag_force + random_force + potential_force)/mass

		velocity += delta_time * acceleration
		position += delta_time * velocity

		#index time position velocity
		output.append([index, time, position, velocity])

		count += 1

	write_file(output_file, output)

	return position, velocity

def read_file(filepath):
	'''Read a file of data and parse columns
	
	Input
	-----
	filepath : String
		relative path to file that is being read

	Return
	------
	data : List
		2-D list of information broken up by line and white-space
	'''
	with open(filepath, 'r') as f:
		data = []
		for line in f:
			data.append([float(x) for x in line.split()])
		return data

def write_file(filepath, data):
	'''Write a file of data and parse columns
	
	Input
	-----
	filepath : String
		relative path to file that is being written to

	data : List
		2-D list of information broken up by line and white-space
	'''

	with open(filepath, 'w') as f:
		for line in data:
			f.write('{} {} {} {}\n'.format(line[0], line[1], line[2], line[3]))