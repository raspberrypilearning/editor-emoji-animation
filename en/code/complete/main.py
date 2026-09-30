from p5 import *
from random import randint

# Global variables
seed_position = 50
grow = 110

def bee():
    if frame_count > grow:
        text('🐝', frame_count - grow, 150)

def draw_background():
    BROWN = Color(185, 155, 115)
    ORANGE = Color(255, 180, 120)
    background(ORANGE)
    fill(BROWN)
    rect(0,300,400,100)

def flower():
    if seed_position >= 300:
        text('🌱', 200, 300)
    if frame_count > grow:
        draw_background()
        text('🌻', 200, 300)

def sow_seeds():
    global seed_position
    if seed_position < 300:
        seed_position = seed_position + 3
        text('🫘', 200, seed_position)

def setup():
    size(400, 400)
    no_stroke()
    text_size(100)

def draw():
    draw_background()
    flower()
    sow_seeds()
    bee()

run()
