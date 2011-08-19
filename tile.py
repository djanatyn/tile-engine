import pygame
pygame.init()

class player:
    def __init__(self,posx,posy):
        self.position = [posx,posy] 
    def go(self,dir):
        desx = self.position[0]; desy = self.position[1]
        if dir == 'up': desy += -20
        elif dir == 'down': desy += 20 
        elif dir == 'left':  desx += -20
        elif dir == 'right': desx += 20
        if worldmap[desy/20][desx/20] == 0:
            self.position = [desx,desy]

clock = pygame.time.Clock()
size = 200, 200
screen = pygame.display.set_mode(size)

wall = pygame.image.load("wall.png")
floor = pygame.image.load("floor.png")
blob = pygame.image.load("guy.png")

worldmap = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1], 
    [1,0,0,0,1,0,0,0,0,1],
    [1,1,0,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]]

def displaymap():
    row = 0; column = 0
    for maprow in worldmap:
        column = 0
        for tile in maprow:
            if tile == 1:
                screen.blit(wall,[column * 20, row * 20])
                print "planted wall at coords (%s,%s)" % (column,row)
            elif tile == 0:
                screen.blit(floor,[column * 20, row * 20])
                print "planted floor at coords (%s,%s)" % (column,row)
            column += 1
        row += 1

character = player(20,20)

while True:
    screen.fill((255,255,255))
    displaymap()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  character.go('left')
            elif event.key == pygame.K_RIGHT: character.go('right')
            elif event.key == pygame.K_UP:    character.go('up')
            elif event.key == pygame.K_DOWN:  character.go('down')
    screen.blit(blob,character.position)
    pygame.display.flip()
