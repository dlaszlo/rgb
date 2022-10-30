import random

from screen import Screen

screen = Screen(800, 500)
screen_mem1 = [0 for i in range(1040)]
screen_mem2 = [0 for i in range(1040)]

for i in range(42):
    screen.set_palette(i, (i * 6, 0, 0))
    screen.set_palette(i + 42, (255, i * 6, 0))
    screen.set_palette(i + 84, (255, 255, i * 6))
screen.set_palette(126, (255, 255, 255))
screen.set_palette(127, (255, 255, 255))

screen.save_palette("pattern_256x1.png")

ii = 0
# random.shuffle(pos)

while screen.check_quit():

    if ii % 4 == 0:
        for i in range(1000, 1040):
            screen_mem1[i] = random.randint(0, 127)
    ii += 1

    for p in range(400, 1000):
        if p % 2 == 0:
            screen_mem1[p] = (screen_mem1[p - 40] + screen_mem1[p + 40]) >> 1
        else:
            screen_mem1[p] = (screen_mem1[p - 1] + screen_mem1[p + 1]) >> 1

    screen.update(screen_mem1)
    screen.delay(20)
