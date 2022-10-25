import tkinter as tk

import collections

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# Animation
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')

import numpy as np

# from read_digital_probe_temp import get_temperature_values
# from helper_functions import calculate_wbgt

class limitedList:
	def __init__(self, size):
		self.size = size
	myList = []
	size = 0
	def addItem(self, number):
		self.myList.append(number)
		if len(self.myList) > self.size:
			self.myList.pop(0)



class Root(tk.Tk):
	def __init__(self):
		super(Root,self).__init__()

		self.title("WBGTI ")
		self.minsize(500,400)

root = Root()

# configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.columnconfigure(3, weight=1)
# root.columnconfigure(4, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=3)

# setup temperature sensors
temperature_sensors = ["", "", ""]
for i, sensor in enumerate(temperature_sensors):
	label = tk.Label(root, text="Sensor {}:\n{}℃".format(i+1, 35.27), borderwidth=1, relief="solid", padx=10, pady=10)
	label.grid(column=i, row=0)

# WBGTI display
wbgtiDisplay = tk.Label(root, text="WBGT:\n{}℃".format(35.27), borderwidth=1, relief="solid", padx=10, pady=10)
wbgtiDisplay.grid(row=0, column=3)

# Settings button
settingsButton = tk.Button(root, text="Settings")
settingsButton.grid(row=0, column=4)

# setup WBGTI graph
f = Figure()
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

canvas = FigureCanvasTkAgg(f, root)
canvas.get_tk_widget().grid(column=0, row=1, columnspan=5)

last_wbgt_readings = collections.deque(maxlen=10)
# def animate():
# 	xar = np.arrange(-10, -1, 1)
# 	sensor_value_dict = get_temperature_values()
# 	last_wbgt_readings.append(calculate_wbgt(sensor_value_dict))
# 	yar = np.random.rand(4)
# 	a.clear()
# 	a.plot(xar,yar)

# TODO: Edit interval (ms) to change sample rate
# ani = animation.FuncAnimation(f, animate, interval=5000)

root.mainloop()
