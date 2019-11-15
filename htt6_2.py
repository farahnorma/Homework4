#Norma
#htt6_2.py

import turtle

def single_square(l, t, n, d, m):
    t.penup()
    t.forward(d)
    t.pendown()
    t.left(n)
    t.forward(l/2)
    for count in range(m-1):
        t.left(n)
        t.forward(l)
    t.left(n)
    t.forward(l/2)
    t.penup()
    t.right(n)
    return

def all_squares(n, l, t, d, m, x):
    for count in range(x):
        single_square(l, t, n, d, m)
        l = l+20

    return

def main():
    l = int(input("Enter length of sides: "))   #20
    m = int(input("Enter number of sides: "))
    n = 360/m  #360/4
    d = int(input("Enter distance between polygons: "))  #10
    x = int(input("Enter number of polygons: "))
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    t = turtle.Turtle()
    t.pencolor("pink")
    t.stamp()
    all_squares(n, l, t, d, m, x)
    wn.exitonclick()




main()