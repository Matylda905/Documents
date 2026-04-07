#nakreslim pomoci obdelniku a ctvercu pyramidu (jeden ctverec a dva obdelniky)

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(125, 50, 175, 100)
canvas.create_rectangle(100, 100, 200, 150)
canvas.create_rectangle(75, 150, 225, 200)
canvas.create_rectangle(50, 200, 250, 250)

tkinter.mainloop()