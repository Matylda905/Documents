#nakreslim vlajku

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 25, 250, 75, fill="red")
canvas.create_rectangle(50, 75, 250, 125, fill="white")
canvas.create_rectangle(50, 125, 250, 175, fill="blue")
tkinter.mainloop()