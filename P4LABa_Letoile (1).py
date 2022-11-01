import turtle
win = turtle.Screen()
t = turtle.Turtle()

for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    
for i in range(3):
    t.forward(100)
    t.left(120)
    t.forward(100)
    
win.mainloop()
