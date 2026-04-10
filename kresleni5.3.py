#nakresli vlajku norska

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 60, 300, 225, fill="red")
canvas.create_rectangle(110, 60, 140, 225, fill="white")
canvas.create_rectangle(50, 120, 300, 150, fill="white")
canvas.create_rectangle(120, 60, 130, 225, fill="blue")
canvas.create_rectangle(50, 130, 300, 140, fill="blue")

tkinter.mainloop()