#nakreslim ctverec v ctverci (jeden 150 a druhej 100)

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 50+150, 50+150)
canvas.create_rectangle(75, 75, 75+100, 75+100)
tkinter.mainloop()