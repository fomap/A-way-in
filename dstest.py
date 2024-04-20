import pygame
import sys

def main(correct_ans):
    
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BROWN = (122, 49, 0)
    pygame.display.set_caption("Discrete structures")   

    newans = correct_ans


#button class
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




    #linear algebruh
    img_1 = pygame.image.load('assets/quiz/ds1.png').convert_alpha()
    button1 = Button(290, 540, img_1, 1)

    img_2 = pygame.image.load('assets/quiz/ds2.png').convert_alpha()
    button2 = Button(290, 640, img_2, 1)
    
    img_3 = pygame.image.load('assets/quiz/ds3.png').convert_alpha()
    button3 = Button(700, 540, img_3, 1)

    img_4 = pygame.image.load('assets/quiz/ds4.png').convert_alpha()
    button4 = Button(700, 640, img_4, 1)
  
    



    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 50
    times_up = False

    bg1 = pygame.image.load('assets/quiz/P3.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)

    


    done = False


    while not done and times_up == False:
        pygame.time.wait(100)

        if countdown == 0:
            times_up = True
            import pptest
            pptest.main(newans)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.USEREVENT:
                countdown -= 1
    
           
        screen.blit(bg1, (0,0)) 
        
        if button1.click(screen):
            newans +=1
            print(newans)
            import pptest
            pptest.main(newans)
            
            
        if button2.click(screen):
            newans += 0
            print(newans)
            import pptest
            pptest.main(newans)
            
        if button3.click(screen):
            newans += 0
            print(newans)
            import pptest
            pptest.main(newans)

        if button4.click(screen):
            newans += 0
            print(newans)
            import pptest
            pptest.main(newans)








        countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
        screen.blit(countdown_text, countdown_rect)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
