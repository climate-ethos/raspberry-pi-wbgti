import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

print(device_folders)

def read_all_temp_raw():
	files = []
	for device_folder in device_folders:
		f = open(device_folder + '/w1_slave', 'r')
		lines = f.readlines()
		files.append(lines)
		f.close()
	return files

def get_temperature_values():
	files = read_all_temp_raw()
	temperatures = []
	for lines in files:
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_all_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temperatures.append(temp_c)
	return temperatures

while True:
	print(get_temperature_values())
	time.sleep(1)
