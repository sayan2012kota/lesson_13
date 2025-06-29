import random
import itertools
import pgzrun

WIDTH = 400
HEIGHT = 600

BLOCK_POSITIONS = [ (350, 50) , (350, 550) , (50, 550) , (50, 50) ]
SECOND_BLOCK_POSITIONS = [ (275, 125) , (275, 475) , (125, 475) , (125, 125) ]
position = itertools.cycle(BLOCK_POSITIONS)
pos_2 = itertools.cycle(SECOND_BLOCK_POSITIONS)

characters = Actor("block", center = (200,300))
second_char = Actor("block", center = (50, 50))

def draw():
    screen.clear()
    characters.draw()
    second_char.draw()

def move_block():
    animate(second_char, "bounce_end", duration = 2, pos = next(position))

def move_second_block():
    animate(characters, "bounce_end", duration = 2, pos = next(pos_2))


move_block()
clock.schedule_interval(move_block, 3)

move_second_block()
clock.schedule_interval(move_second_block, 3)


pgzrun.go()