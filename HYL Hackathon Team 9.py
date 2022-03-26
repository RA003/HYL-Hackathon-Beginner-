#Pygame documentation
#https://www.pygame.org/docs/

import pygame
import os
import playercode
#

img_dir = os.path.join('images')

pygame.init()

#REMEMBER to make the 'workspace' big enough so you can see the entire game window, or else the player will be cut off.

#clock for setting fps later
clock = pygame.time.Clock()

#window size 500 by 500 for now
win = pygame.display.set_mode((500, 500))

class Game:
  def __init__(self):
    pass
class Map:
  def __init__(self):
    pass


#pygame.sprite.Sprite just give the Unit class access to all the built in pygame functions for sprites
import pygame
import os

class Unit(pygame.sprite.Sprite):
  def __init__(self, img, x, y, scale):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    #Adding to groups
    all_sprites.add(self)
    units.add(self)
    
  def update(self):
    pass

class Player(Unit):
  def __init__(self, img, x, y, scale):
    Unit.__init__(self, img, x, y, scale)
    
  def update(self):
    pass  
  def playercommands():
  #code to recieve player commands entered in console prior to running the level
    pass

  
class Enemy(Unit):
  def __init__(self):
    pass
    
class Obstacle:
  def __init__(self):
    all_sprites.add(self)
    obstacles.add(self)

def main():
  
  
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #redraw background
    win.fill((255, 255, 255))
  
    all_sprites.update()
    all_sprites.draw(win)
    pygame.display.update()
    
  pygame.quit()

#GROUPS
#Allows us to do things like check for player collision against all sprites in the obstacle group

obstacles = pygame.sprite.Group()
units = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = pygame.image.load(os.path.join(img_dir, "player.png")).convert()

#creating instance of player object
P1 = Player(player, 250, 250, 1)


#Run the mainloop
if __name__ == "__main__":
  main()
