
# Kitters - Platform Game
import pygame as pg
import random
from settings import *

class Game:
    def __init__(self):
        # initialize game window
        # initialize Pygame & create window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game/resets Game
        self.all_sprites = pg.sprite.Group()
        self.run()


    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # game loop - update
        self.all_sprites.update()

    def events(self):
        # game loop - events
        # Process input / events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # game loop - drawing
        # Draw / Render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        #game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()


pg.quit()
