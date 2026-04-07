#nakreslim vedle sebe dva ctverce

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150)
canvas.create_rectangle(200, 50, 300, 150)
tkinter.mainloop()
