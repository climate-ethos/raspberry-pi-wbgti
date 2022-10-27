import os
import glob
import time

import numpy as np

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

print(device_folders)

def read_temp_raw(id):
	try:
		f = open(base_dir + id + '/w1_slave', 'r')
		lines = f.readlines()
		f.close()
		return lines
	except:
		print("Cant find sensor id:", id)
		return False

def extract_temp_from_lines(lines, id):
	if lines:
		# Extract temperature C from lines
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_temp_raw(id)
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			return temp_c
	# If sensor not found or error return NaN
	return np.nan


def get_temperature_values():
	sensors = {
		"wet_bulb_sensor": "28-1",
		"globe_sensor": "28-2",
		"dry_bulb_sensor": "28-3"
	}
	for key, value in sensors.items():
		lines = read_temp_raw(value)
		sensors[key] = extract_temp_from_lines(lines, value)
	return sensors
