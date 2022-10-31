import tkinter as tk
from tkinter import ttk

# --- classes ---

class Keypad(ttk.Frame):

	cells = [
		['1', '2', '3'],
		['4', '5', '6'],
		['7', '8', '9'],
		['', '0', ''],
	]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.target = None
		self.memory = ''

		for y, row in enumerate(self.cells):
			for x, item in enumerate(row):
				if item:
					b = ttk.Button(self, text=item, command=lambda text=item:self.append(text))
					b.grid(row=y, column=x, padx=2, pady=2, sticky='news')

		x = ttk.Button(self, text='Backspace', command=self.backspace)
		x.grid(row=0, column=10, padx=2, pady=2, sticky='news')

		x = ttk.Button(self, text='Clear', command=self.clear)
		x.grid(row=1, column=10, padx=2, pady=2, sticky='news')


	def get(self):
		if self.target:
			return self.target.get()

	def append(self, text):
		if self.target:
			self.target.insert('end', text)

	def clear(self):
		if self.target:
			self.target.delete(0, 'end')

	def backspace(self):
		if self.target:
			text = self.get()
			text = text[:-1]
			self.clear()
			self.append(text)

	def show(self, entry):
		self.target = entry

		self.grid(row=2, column=1, columnspan=2, pady=(30,0))

	def hide(self):
		self.target = None

		self.place_forget()