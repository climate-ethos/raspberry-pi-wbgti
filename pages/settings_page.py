import tkinter as tk

class SettingsPage(tk.Frame):
	def __init__(self, parent, controller) -> None:
		tk.Frame.__init__(self, parent)
		settingsButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("TemperatureDisplay"))
		settingsButton.grid(row=0, column=0)