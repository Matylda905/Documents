#nakreslim tri ctverce, vsechny maji spolecny bod v bode (x,y) a postupne se zmensuji  (cerveny ma delku 100, modry 60 a bily 20) souradnice x,y jsou ulozeny ve stejnojmennych promennych

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 50
y = 50
canvas.create_rectangle(20, 20, 350, 300, fill="lightgray")
canvas.create_rectangle(x, y, x+100, y+100, fill="red")
canvas.create_rectangle(x+20, y+20, x+80, y+80, fill="blue")
canvas.create_rectangle(x+40, y+40, x+60, y+60, fill="white")

tkinter.mainloop()