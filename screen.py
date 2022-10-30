import pygame


class Screen:

    def __init__(self, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height
        self.char_width = int(width / 40)
        self.char_height = int(height / 25)
        self.screen = pygame.display.set_mode((width, height))
        self.run = True
        self.palette = [(0, 0, 0) for i in range(256)]

    def set_palette(self, color, rgb):
        self.palette[color] = rgb

    def delay(self, delay):
        if self.run:
            pygame.time.delay(delay)

    def plot(self, y, x, color):
        self.screen_mem[y][x] = color

    def check_quit(self):
        if self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
            if not self.run:
                pygame.quit()
        return self.run

    def update(self, screen_mem):
        for y in range(25):
            for x in range(40):
                color = self.palette[screen_mem[y * 40 + x]]
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(x * self.char_width, y * self.char_height, self.char_width,
                                             self.char_height))
        pygame.display.update()
