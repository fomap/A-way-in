

import pygame
import sys

def main():
    
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BROWN = (122, 49, 0)
    pygame.display.set_caption("Level 6")   

    
   
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 500
    times_up = False

    bg = pygame.image.load('assets/import/bg.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)


 


    done = False
 

    while not done and times_up == False:
        

        if countdown == 0:
            times_up = True
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.USEREVENT:
                countdown -= 1
        screen.blit(bg, (0,0)) 
        
       
        
       


      
                
    
        countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
        screen.blit(countdown_text, countdown_rect)
    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
