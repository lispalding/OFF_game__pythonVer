# MADE BY: Lisette Spalding
# FILE NAME: main.py
# PROJECT NAME: OFF_game__pythonVer
# DATE CREATED: 04/21/2021
# DATE LAST MODIFIED: 04/21/2021
# PYTHON VER. USED: 3.x

##################### IMPORTS ######################
import pygame as pg
import random as r
from os import path

# Custom Imports #
from settings import *
from sprites import *
from camera_and_map import *
##################### FINISHED #####################

################ MAIN GAME LOOP ################
####### Game class #######
class Game(object):
    """ To use: Game()
    This class runs the main game. """
    def __init__(self):
        self.running = True

        pg.init()  # Initializing Pygame Library
        pg.mixer.init()  # Sounds

        # Initializing display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)

        # Initializing clock
        self.clock = pg.time.Clock()

        # Setting repeat variable
        pg.key.set_repeat(500, 100)

        self.loadData()

    def loadData(self):
        """ To use: self.loadData()
        This method creates data for maps. """
        self.map = Map(path.join(mapsFolder, "example_map1__large.txt"))

        # Loading player image
        # imgs = path.join(imageFolder, "Preview_110.png")
        # self.playerImage = pg.image.load(imgs).convert_alpha()

    def new(self):
        """ To use: self.new()
        This method creates a new game. """
        # Creating the sprite groups
        self.allSprites = pg.sprite.Group() # All sprites group
        self.playerGroup = pg.sprite.Group() # Player group

        self.walls = pg.sprite.Group() # The Walls group

        ## Creating the game objects

        # Spawning walls
        for row, tiles in enumerate(self.map.data): # Where the "enumerate" uses both index number and list item
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)

                if tile == "P":
                    self.player = Player(self, col, row)

                    # Adding player to sprite groups
                    self.allSprites.add(self.player)
                    self.playerGroup.add(self.player)

        # Spawning camera
        self.camera = Camera(self.map.width, self.map.height)


        # Start running game loop...
        self.run()

    def run(self):
        """ To use: self.run()
        This method runs the game. """
        ## Game loop
        self.playing = True

        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000

            # Processing input events
            self.events()

            # Processing updated variables
            self.update()

            # Creating the images on the screen
            self.draw()

    def events(self):
        """ To use: self.events()
        This method keeps track of the events that happen throughout running the game. """
        for event in pg.event.get():
            # Check for closing windows:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

                # Movement events: .. --NOT NEEDED-- ..
                # if event.key == pg.K_LEFT:
                #     self.player.move(dx = -1)
                # if event.key == pg.K_RIGHT:
                #     self.player.move(dx = 1)
                # if event.key == pg.K_UP:
                #     self.player.move(dy = -1)
                # if event.key == pg.K_DOWN:
                #     self.player.move(dy = 1)

    def update(self):
        """ To use: self.update()
        This method updates what is shown on the HUD. """
        self.allSprites.update()
        self.camera.update(self.player)

    def drawGrid(self):
        """ To use: self.drawGrid()
        This method draws a grid on the screen. Useful for tile-based games. """
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHT_GREY, (0, y), (WIDTH, y))

    def draw(self):
        """ To use: self.draw()
        This method draws the content on the screen. """
        self.screen.fill(BLACK)

        ## Customizing the draw() method for a tile-based game:
        self.drawGrid()
        ## FIN

        for sprite in self.allSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        ## This is the very last thing to happen during the draw:
        pg.display.flip()

    def showStartingScreen(self):
        """ To use: self.showStartingScreen()
        This method shows the starting screen. """
        pass

    def showGameOverScreen(self):
        """ To use: self.showGameOverScreen()
        This method shows the game over screen. """
        pass

####### Finished #######

g = Game() # Defining the game start

g.showStartingScreen() # Showing the starting screen for the new game

while g.running:
    g.new() # This kicks off the actual game loop
    g.showGameOverScreen()

# If the loop ever breaks this happens:
pg.quit()
################### FINISHED ###################