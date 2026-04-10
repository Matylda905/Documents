#nakreslim obdelnik kde se ze ctyr dalsich uzkych obdelniku udela ohraniceni
 

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 250, 200, fill="lightgray")
canvas.create_rectangle(70, 180, 240, 190, fill="red")
canvas.create_rectangle(230, 60, 240, 180, fill="blue")
canvas.create_rectangle(60, 60, 230, 70, fill="red")
canvas.create_rectangle(60, 70, 70, 190, fill="blue")

tkinter.mainloop()