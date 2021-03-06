# MADE BY: Lisette Spalding
# FILE NAME: settings.py
# PROJECT NAME: OFF_game__pythonVer
# DATE CREATED: 04/21/2021
# DATE LAST MODIFIED: 04/21/2021
# PYTHON VER. USED: 3.x

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path
################### FINISHED ###################

############### BASIC VARIABLES ################
WIDTH = 1024
HEIGHT = 768
FPS = 60

# Title
title = "OFF - English Ver. Coded with Python 3.x"
################### FINISHED ###################

############### GAME VARIABLES ################
TILE_SIZE = 64

GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE
################### FINISHED ###################

############## PLAYER VARIABLES ################
PLAYER_SPEED = 250

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

PLAYER_IMAGE = ""
################### FINISHED ###################

################# FOLDER SETUP #################
gameFolder = path.dirname(__file__) # General folder set-up

# Map folder
mapsFolder = path.join(gameFolder, "maps")

## Individual maps folders
map1File = path.join(mapsFolder, "map.txt")

# Basic image folders
imageFolder = path.join(gameFolder, "images")

# Basic sound folder
soundFolder = path.join(gameFolder, "sounds")

# Basic text data folder
textDataFolder = path.join(gameFolder, "text_data")
################### FINISHED ###################

############## COLORS  (R. G. B) ###############
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom Colors
ORANGE = (242, 162, 41)
MINT = (63, 232, 159)
PURPLE = (182, 103, 224)
PINK = (224, 103, 139)
YELLOW = (245, 233, 154)

LIGHT_GREY = (100, 100, 100)
YELLOW_GREEN = (182, 219, 18)
LIGHT_BLUE = (100, 162, 209)
################### FINISHED ###################