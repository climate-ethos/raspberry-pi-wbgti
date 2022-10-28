import collections
from tkinter import ttk
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = '#333333'
plt.rcParams['figure.facecolor'] = '#333333'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FormatStrFormatter

from modules.calculate_wbgt import calculate_wbgt
from modules.read_digital_probe_temp import get_temperature_values
import modules.colors as colors

class TemperatureDisplay(ttk.Frame):
	controller = None
	figure = None
	ax = None
	ani = None
	sensorLabels = []
	samplingInterval = 1
	wbgtLabel = None
	last_wbgt_readings = collections.deque([np.nan] * 10, maxlen=10)

	def __init__(self, parent, controller) -> None:
		ttk.Frame.__init__(self, parent)
		self.controller = controller
		# Temperature sensor display
		for i in range(3):
			label = ttk.Label(self, borderwidth=1, relief="solid", padding=10)
			label.grid(column=i, row=0)
			self.sensorLabels.append(label)

		# WBGTI display
		self.wbgtLabel = ttk.Label(self, borderwidth=1, relief="solid", padding=10)
		self.wbgtLabel.grid(row=0, column=3)

		# Settings button
		settingsButton = ttk.Button(self, text="Settings", command=lambda: controller.show_frame("SettingsPage"))
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
		# Calculate what color line should be
		if (wbgtValue <= 25):
			line_color = colors.green
		elif (wbgtValue > 25 or wbgtValue <= 28):
			line_color = colors.yellow
		elif (wbgtValue > 28 or wbgtValue <= 31):
			line_color = colors.orange
		else:
			line_color = colors.red
		# Update live graph
		#FIXME: Update no longer works after using .after for delay
		xar = np.arange(-10, 0, 1)
		self.last_wbgt_readings.append(wbgtValue)
		self.ax.clear()
		self.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
		self.ax.plot(xar, self.last_wbgt_readings,  color=line_color)
		self.controller.after(self.samplingInterval*1000, self.graph_animate)


	def get_sampling_interval(self):
		return self.samplingInterval

	def set_sampling_interval(self, samplingInverval):
		self.samplingInterval = samplingInverval


