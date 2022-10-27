import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

print(device_folders)

def read_temp_raw(id):
	f = open(base_dir + id + '/w1_slave', 'r')
	lines = f.readlines()
	f.close()
	return lines

def get_temperature_values():
	sensors = {
		"wet_bulb_sensor": "28-1",
		"globe_sensor": "28-2",
		"dry_bulb_sensor": "28-3"
	}
	for key, value in sensors:
		lines = read_temp_raw(value)
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_temp_raw(value)
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			sensors[key] = temp_c
	return sensors

while True:
	print(get_temperature_values())
	time.sleep(1)
