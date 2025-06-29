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

def random_angle():
    x = random.randint(100, 300)
    y = random.randint(100, 500)
    characters.target = x, y
    target_angle = characters.angle_to(characters.target)
    target_angle = target_angle + 360 * ((characters.angle - target_angle + 180) // 360)
    animate(characters, angle = target_angle, duration = 0.2, on_finished = move_ship)

move_block()
clock.schedule_interval(move_block, 3)

def move_ship():
    animate(characters, tween = "accel_decel", pos = characters.target, duration = characters.distance_to(characters.target) / 200, on_finished = random_angle)



random_angle()

pgzrun.go()