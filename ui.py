import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()

        self.title("WBGTI ")
        self.minsize(500,400)

root = Root()

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

# setup temperature sensors
temperature_sensors = ["", "", ""]
for i, sensor in enumerate(temperature_sensors):
    label = tk.Label(root, text="Sensor {}:\n{}℃".format(i+1, 35.27), borderwidth=1, relief="solid", padx=10, pady=10)
    label.grid(column=i, row=0)

# setup WBGTI graph
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

canvas = FigureCanvasTkAgg(f, root)
canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)

root.mainloop()
