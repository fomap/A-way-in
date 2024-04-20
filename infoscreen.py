import pygame
import sys

def main():
    
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Info Screen")   

    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def click(self, surface):
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #draw button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action



    bg1 = pygame.image.load('assets/title/infobg.png')


    img_1 = pygame.image.load('assets/title/back.png').convert_alpha()
    button1 = Button(510, 50, img_1, 1)

    done = False

    while not done:
        pygame.time.wait(100)

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            
    
           
        screen.blit(bg1, (0,0)) 
        
        if button1.click(screen):
            import titlescreen
            titlescreen.main()
            
            
       
      

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
