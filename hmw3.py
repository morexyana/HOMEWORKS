# задание 1
import pygame
 
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 500
 
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
pygame.init()
 
clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
# радиус и координаты круга
r = 30
x = 0 - r  # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали
 
while 1:
    sc.fill(WHITE)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: 
            exit()
 
    pygame.draw.rect(sc, ORANGE, (x, y, 100,100))
 
    pygame.display.update()
 
    
    if x >= WIN_WIDTH + r:
        x = 0 - r
    else:  
        x += 2  
   
 
    clock.tick(FPS)
    # задание 2
import pygame
import math
       #R  G B
red = (255,0,0)

def move_coords(angle, radius, coords):
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)
 
def main():
    pygame.display.set_caption("Oribit")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
     
    coords = (400, 200)
    angle = 0
    rect = pygame.Rect(*coords,20,20)
    speed = 50
    next_tick = 500
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        ticks = pygame.time.get_ticks() 
        if ticks > next_tick:
            next_tick += speed
            angle += 1
            coords = move_coords(angle, 2, coords)
            rect.topleft = coords
             
        screen.fill((0,0,30))
        pygame.draw.circle(screen,red, (int(coords[0]),int(coords[1])), 10)
        pygame.display.flip()
        clock.tick(30)
     
    pygame.quit()
 
if __name__ == '__main__':
    main()