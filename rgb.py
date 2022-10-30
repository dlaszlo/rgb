import random

from screen import Screen

screen = Screen(800, 500)
screen_mem1 = [0 for i in range(1040)]
screen_mem2 = [0 for i in range(1040)]

for i in range(64):
    screen.set_palette(i, (i * 4, 0, 0))
    screen.set_palette(i + 64, (255, i * 4, 0))
    screen.set_palette(i + 128, (255, 255, i * 4))

ii = 0

while screen.check_quit():

    if ii % 4 == 0:
        for i in range(1000, 1040):
            screen_mem1[i] = random.randint(0, 192)
        ii = 0
    ii += 1

    for p in range(400, 1000):
        if p % 2 == 0:
            screen_mem1[p] = \
                max(int((screen_mem1[p - 40] + screen_mem1[p + 40]) / 2), 0)
        else:
            screen_mem1[p] = \
                max(int((screen_mem1[p - 1] + screen_mem1[p + 1]) / 2), 0)

    screen.update(screen_mem1)
    screen.delay(20)
