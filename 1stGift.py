import math
import pygame
from turtle import *
import time

# --- Initialize pygame mixer for music ---
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")  # ensure this file is in the same folder
pygame.mixer.music.play(-1)  # loop forever

# --- Heart formula functions ---
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# --- Turtle setup ---
speed(0)
bgcolor("black")
color("red")
pensize(3)
hideturtle()

# --- Draw the heart ---
penup()
goto(0, 0)
pendown()
for i in range(360):
    x = hearta(math.radians(i)) * 20
    y = heartb(math.radians(i)) * 20
    goto(x, y)
goto(0, 0)

# --- Strobe (glow/pulse) effect after drawing ---
def strobe_effect():
    colors = ["#ff0000", "#ff4d4d", "#ff8080", "#ffcccc", "#ff8080", "#ff4d4d"]
    pensize(4)
    while True:
        for c in colors:
            color(c)
            penup()
            goto(0, 0)
            pendown()
            begin_fill()
            for i in range(360):
                x = hearta(math.radians(i)) * 20
                y = heartb(math.radians(i)) * 20
                goto(x, y)
            end_fill()
            update()
            time.sleep(0.1)
            clear()

# --- Enable fast drawing updates ---
tracer(False)
strobe_effect()
