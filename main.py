import pygame, time, random
from pygame.locals import *
from pytmx.util_pygame import load_pygame

class Teleport(pygame.sprite.Sprite):
    def __init__(self, x, y, exitx, exity):
        super().__init__()
        self.image = pygame.Surface((20, 31))  # Adjust size as needed
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.exit_location = (exitx, exity)

def main():
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    done = False
    x = 100
    y = 100

    countdown = 300
    times_up = False

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Timelet {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (width // 2, 50)
    
    teleporter = Teleport(100, 100, 500, 500) 

    
    player_image = pygame.Surface((32, 32))
    player_image.fill((255, 0, 0))  # Red color
    player_rect = player_image.get_rect()
    player_rect.topleft = (100, 100)
    player_speed = 10

    while not done and times_up == False:
        window.fill((0,0,0))            

        if countdown == 0:
            times_up = True

        for event in pygame.event.get():  
            if event.type == QUIT:
                done = True
            if event.type == pygame.USEREVENT:
                countdown -= 1

        pressed_keys = pygame.key.get_pressed()

        
        if pressed_keys[K_a] and x > 0:
            player_rect.x -= player_speed
        elif pressed_keys[K_d] and x < window.get_width()-30:
            player_rect.x += player_speed
        elif pressed_keys[K_w] and y > 80:
            player_rect.y -= player_speed
        elif pressed_keys[K_s] and y < window.get_height()-30:
            player_rect.y += player_speed
    
        if player_rect.colliderect(teleporter.rect):
            player_rect.topleft = teleporter.exit_location

        window.blit(player_image, player_rect)
        window.blit(teleporter.image, teleporter.rect)


        countdown_text = countdown_font.render(f"Timeleft {countdown}", True, (255,255,255))
        window.blit(countdown_text, countdown_rect)


        pygame.display.update()                             
        clock.tick(60)                                  


if __name__ == "__main__":
    width, height = 1400, 800                            
    pygame.init()                                       
    start_tick = pygame.time.get_ticks()
    pygame.display.set_caption("Game Jam")   
    window = pygame.display.set_mode((width, height))  
    clock = pygame.time.Clock()                         
    main()
    pygame.quit()