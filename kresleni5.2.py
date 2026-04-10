#nakreslim vlajku irska

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 15, 150, 150, fill="green")
canvas.create_rectangle(150, 15, 250, 150, fill="white")
canvas.create_rectangle(250, 15, 350, 150, fill="orange")

tkinter.mainloop()