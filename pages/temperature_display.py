import collections
import tkinter as tk
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# from modules.calculate_wbgt import calculate_wbgt
# from modules.read_digital_probe_temp import get_temperature_values

# def animate():
# 	xar = np.arrange(-10, -1, 1)
# 	yar = np.random.rand(4)
# 	sensor_value_dict = get_temperature_values()
# 	last_wbgt_readings.append(calculate_wbgt(sensor_value_dict))
# 	a.clear()
# 	a.plot(xar,yar)

class TemperatureDisplay(tk.Frame):
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
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.figure.tight_layout()
		canvas.get_tk_widget().grid(column=0, row=1, columnspan=5)

		last_wbgt_readings = collections.deque(maxlen=10)

		# TODO: Edit interval (ms) to change sample rate
		# ani = animation.FuncAnimation(f, animate, interval=5000)

