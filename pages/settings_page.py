import tkinter as tk
class SettingsPage(tk.Frame):
	controller = None
	intervalInput = None

	def __init__(self, parent, controller) -> None:
		tk.Frame.__init__(self, parent)
		self.controller = controller

		intervalLabel = tk.Label(self, text="Sampling rate (s):")
		intervalLabel.grid(row=1, column=1)

		self.intervalInput = tk.Entry(self)
		self.intervalInput.grid(row=1, column=2)

		samplingInterval = str(controller.get_frame("TemperatureDisplay").get_sampling_interval())
		self.intervalInput.insert(tk.END, samplingInterval)

		backButton = tk.Button(self, text="Back", command=self.save_and_return)
		backButton.grid(row=0, column=0)

	def save_and_return(self):
		print("GO BACK")
		newSamplingInterval = int(self.intervalInput.get())
		self.controller.get_frame("TemperatureDisplay").set_sampling_interval(newSamplingInterval)
		self.controller.show_frame("TemperatureDisplay")