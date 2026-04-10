#nakreslim ctverce ktere jsou pres sebe (prbni z nich ma souradnice leveho vrcholu 50, 50)

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(20, 20, 350, 300, fill="lightgray")
canvas.create_rectangle(50, 50, 150, 150, fill="red")
canvas.create_rectangle(100, 100, 200, 200, fill="blue")
canvas.create_rectangle(150, 150, 250, 250, fill="green")
canvas.create_rectangle(200, 200, 300, 300, fill="yellow")

tkinter.mainloop()