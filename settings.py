# MADE BY: Lisette Spalding
# FILE NAME: settings.py
# PROJECT NAME: OFF_game__pythonVer
# DATE CREATED: 04/21/2021
# DATE LAST MODIFIED: 04/21/2021
# PYTHON VER. USED: 3.x

################### IMPORTS ####################
import pygame as pg
import random as r
from os import *
################### FINISHED ###################

########## VARIABLES ###########
WIDTH = 360
HEIGHT = 480
FPS = 30

# Title
title = "OFF - English Ver. Coded with Python 3.x"
########### FINISHED ###########

######### FOLDER SETUP #########
gameFolder = path.dirname(__file__) # General folder set-up

# Basic image folders
imageFolder = path.join(gameFolder, "images")
playerImages = path.join(imageFolder, "player_image")

# Basic sound folder
soundFolder = path.join(gameFolder, "sounds")

# Basic text data folder
textDataFolder = path.join(gameFolder, "text_data")
########### FINISHED ###########

###### COLORS  (R. G. B) ######
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom Colors
ORANGE = (242, 162, 41)
YELLOW_GREEN = (182, 219, 18)
MINT = (63, 232, 159)
PURPLE = (182, 103, 224)
PINK = (224, 103, 139)
LIGHT_BLUE = (100, 162, 209)
YELLOW = (245, 233, 154)
############# FIN #############