import collections
import tkinter as tk
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FormatStrFormatter

from modules.calculate_wbgt import calculate_wbgt
from modules.read_digital_probe_temp import get_temperature_values

class TemperatureDisplay(tk.Frame):
	controller = None
	figure = None
	ax = None
	ani = None
	sensorLabels = []
	samplingInterval = 1
	wbgtLabel = None
	last_wbgt_readings = collections.deque([np.nan] * 10, maxlen=10)

	def __init__(self, parent, controller) -> None:
		tk.Frame.__init__(self, parent)
		self.controller = controller
		# Temperature sensor display
		for i in range(3):
			label = tk.Label(self, borderwidth=1, relief="solid", padx=10, pady=10)
			label.grid(column=i, row=0)
			self.sensorLabels.append(label)

		# WBGTI display
		self.wbgtLabel = tk.Label(self, borderwidth=1, relief="solid", padx=10, pady=10)
		self.wbgtLabel.grid(row=0, column=3)

		# Settings button
		settingsButton = tk.Button(self, text="Settings", command=lambda: controller.show_frame("SettingsPage"))
		settingsButton.grid(row=0, column=4)

		# setup WBGTI graph
		self.figure = Figure(figsize=(7,4), dpi=100)
		self.ax = self.figure.add_subplot(111)

		canvas = FigureCanvasTkAgg(self.figure, self)
		canvas.figure.tight_layout()
		canvas.get_tk_widget().grid(column=0, row=1, columnspan=5, padx=15, pady=10)

		# TODO: Edit interval (ms) to change sample rate
		self.graph_animate()

	def graph_animate(self, *args):
		print("Updating graph...")
		sensor_value_dict = get_temperature_values()
		# Update sensor labels
		for index, item in enumerate(sensor_value_dict.items()):
			key, value = item
			self.sensorLabels[index].configure(text="{}:\n{:.2f}℃".format(key, value))
		# Calculate wbgt
		wbgtValue = calculate_wbgt(sensor_value_dict)
		# Update wbgt label
		self.wbgtLabel.configure(text="WBGT:\n{:.2f}℃".format(wbgtValue))
		# Update live graph
		xar = np.arange(-10, 0, 1)
		self.last_wbgt_readings.append(wbgtValue)
		self.ax.clear()
		self.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
		self.ax.plot(xar,self.last_wbgt_readings)
		self.controller.after(self.samplingInterval*1000, self.graph_animate)


	def get_sampling_interval(self):
		return self.samplingInterval

	def set_sampling_interval(self, samplingInverval):
		self.samplingInterval = samplingInverval


