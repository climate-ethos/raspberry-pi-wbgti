import collections
import tkinter as tk
from matplotlib import animation
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import random

# from modules.calculate_wbgt import calculate_wbgt
# from modules.read_digital_probe_temp import get_temperature_values

class TemperatureDisplay(tk.Frame):
	ax = None
	ani = None
	last_wbgt_readings = collections.deque([np.nan] * 10, maxlen=10)

	def __init__(self, parent, controller) -> None:
		tk.Frame.__init__(self, parent)
		# Temperature sensor display
		for i in range(3):
			label = tk.Label(self, text="Sensor {}:\n{}℃".format(i+1, 35.27), borderwidth=1, relief="solid", padx=10, pady=10)
			label.grid(column=i, row=0)

		# WBGTI display
		wbgtiDisplay = tk.Label(self, text="WBGT:\n{}℃".format(35.27), borderwidth=1, relief="solid", padx=10, pady=10)
		wbgtiDisplay.grid(row=0, column=3)

		# Settings button
		settingsButton = tk.Button(self, text="Settings", command=lambda: controller.show_frame("SettingsPage"))
		settingsButton.grid(row=0, column=4)

		# setup WBGTI graph
		f = Figure(figsize=(10.5,5.5))
		self.ax = f.add_subplot(111)

		canvas = FigureCanvasTkAgg(f, self)
		canvas.figure.tight_layout()
		canvas.get_tk_widget().grid(column=0, row=1, columnspan=5)

		# TODO: Edit interval (ms) to change sample rate
		self.graph_animate()
		self.ani = animation.FuncAnimation(f, self.graph_animate, interval=5000)

	def graph_animate(self, *args):
		xar = np.arange(-10, 0, 1)
		# sensor_value_dict = get_temperature_values()
		# last_wbgt_readings.append(calculate_wbgt(sensor_value_dict))
		self.last_wbgt_readings.append(random.randint(0,9))
		self.ax.clear()
		self.ax.plot(xar,self.last_wbgt_readings)

