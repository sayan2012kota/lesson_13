import random
import itertools
import pgzrun

WIDTH = 400
HEIGHT = 600

BLOCK_POSITIONS = [ (350, 50) , (350, 550) , (50, 550) , (50, 50) ]

position = itertools.cycle(BLOCK_POSITIONS)

characters = Actor("rocket", center = (200,300))
second_char = Actor("block", center = (50, 50))

def draw():
    screen.clear()
    characters.draw()
    second_char.draw()

def move_block():
    animate(second_char, "bounce_end", duration = 2, pos = next(position))


move_block()
clock.schedule_interval(move_block, 3)

def move_ship():
    animate(characters, tween = "accel_decel")


pgzrun.go()