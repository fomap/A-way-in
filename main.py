import pygame, time, random
from pygame.locals import *
from pytmx.util_pygame import load_pygame

def draw_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            x_px = tile[0] * 70 + world_offset[0]
            y_px = tile[1] * 70 + world_offset[1]
            window.blit(tile[2], (x_px, y_px))



def main():
    
    player = pygame.image.load("assets/p3_walk01.png").convert_alpha()
    player = pygame.transform.scale(player, (50,70))

    player_anims = [
        pygame.image.load("assets/p3_walk01.png").convert_alpha(),
        pygame.image.load("assets/p3_walk02.png").convert_alpha(),
        pygame.image.load("assets/p3_walk03.png").convert_alpha(),
        pygame.image.load("assets/p3_walk04.png").convert_alpha(),
        pygame.image.load("assets/p3_walk05.png").convert_alpha(),
        pygame.image.load("assets/p3_walk06.png").convert_alpha(),
        pygame.image.load("assets/p3_walk07.png").convert_alpha(),
        pygame.image.load("assets/p3_walk08.png").convert_alpha(),
        pygame.image.load("assets/p3_walk09.png").convert_alpha(),
        pygame.image.load("assets/p3_walk10.png").convert_alpha(),
        pygame.image.load("assets/p3_walk11.png").convert_alpha()
    ]

    player_anims = [pygame.transform.scale(img, (50,70)) for img in player_anims]
    frame = 0
    player_anims_l = [pygame.transform.flip(img, True, False) for img in player_anims]
    framel = 0
    
    direction = ("still")
    done = False
    x = 0
    y = 0
 
    while not done:
        window.fill((0,0,0))                           
     
        for event in pygame.event.get():  
            if event.type == QUIT:
                done = True

        pressed_keys = pygame.key.get_pressed()

        
        if pressed_keys[K_a] and x > 0:
            x = x - 10
            direction = "l"
        elif pressed_keys[K_d] and x < window.get_width()-50:
            x = x + 10
            direction = "r"
        elif pressed_keys[K_w] and y > 0:
            y = y - 10
        elif pressed_keys[K_s] and y < window.get_height()-70:
            y = y + 10
        else:
            direction = "still"


           
        # player = Rect(x, y, 50, 50)
        # pygame.draw.rect(window, (204,0,255), player)

        # window.blit(player, (x,y))
    
        if direction == "still":
            window.blit(player, (x, y))
        elif direction == "r":
            window.blit(player_anims[frame], (x, y))
            frame += 1
            if frame >= len(player_anims):
                frame = 0
        elif direction == "l":
            window.blit(player_anims_l[framel], (x, y))
            framel += 1
            if framel >= len(player_anims_l):
                framel = 0

        pygame.display.update()                             
        clock.tick(30)                                  


if __name__ == "__main__":
    width, height = 800, 600                            
    pygame.init()                                       
    pygame.mixer.init()                                 
    pygame.display.set_caption("Game Jam")   
    window = pygame.display.set_mode((width, height))  
    clock = pygame.time.Clock()                         
    main()
    pygame.quit()