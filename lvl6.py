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

    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((32, 32))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.topleft = (685, 715)
            self.speed = 5

        def updateSpeed(self):
            self.speed = 7

        def update(self, keys):
            dx, dy = 0, 0
            if keys[pygame.K_a] and self.rect.x > 0:
                dx -= self.speed
            if keys[pygame.K_d] and self.rect.x < screen.get_width()-30:
                dx += self.speed
            if keys[pygame.K_w] and self.rect.y > 80:
                dy -= self.speed
            if keys[pygame.K_s] and self.rect.y < screen.get_height()-30:
                dy += self.speed

            
            self.rect.x += dx
            for wall in walls:
                if pygame.sprite.collide_rect(self, wall):
                    if dx > 0:
                        self.rect.right = wall.rect.left
                    elif dx < 0:
                        self.rect.left = wall.rect.right

            self.rect.y += dy
            for wall in walls:
                if pygame.sprite.collide_rect(self, wall):
                    if dy > 0:
                        self.rect.bottom = wall.rect.top
                    elif dy < 0:
                        self.rect.top = wall.rect.bottom

    # Teleporter class
    class Teleport(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, exit_x, exit_y):
            super().__init__()
            self.image = pygame.Surface((width, height))
            self.image.fill(BROWN)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.exit_pos = (exit_x, exit_y)

    # Wall class
    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height):
            super().__init__()
            self.image = pygame.Surface((width, height))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

    
    player = Player()
    exit = pygame.Rect(670, 165, 70, 15)
    
    player_sprites = pygame.sprite.Group()
    player_sprites.add(player)
    
    wallmainbottom = Wall(385, 560, 650, 15)
    wallmainleft = Wall(385, 80, 15, 480)
    wallmainright = Wall(1020, 80, 15, 480)
    wallroomonebottom = Wall(0, 385, 400, 15)
    wallroomfourbottom = Wall(1020, 385, 400, 15)
    wallroomtworight = Wall(190, 400, 15, 480)
    wallroomfiveright = Wall(1225, 400, 15, 480)
  
    
    walls = pygame.sprite.Group()
    walls.add(
        wallmainbottom,
        wallmainleft,
        wallmainright,
        wallroomonebottom,
        wallroomfourbottom,
        wallroomtworight,
        wallroomfiveright
        )
    

    teleporter1a = Teleport(1190, 690, 20, 70, 80, 435)
    teleporter1b = Teleport(60, 405, 70, 20, 80, 435)
    teleporter2a = Teleport(155, 555, 20, 70, 1080, 115)
    teleporter2b = Teleport(1050, 105, 20, 70, 1080, 115)
    teleporter3a = Teleport(1050, 280, 20, 70, 505, 305)
    teleporter3b = Teleport(480, 290, 20, 70,505, 305)
    teleporter10a = Teleport(900, 290, 20, 70, 685, 615)
    teleporter10b = Teleport(665, 585, 70, 20, 685, 615)
    teleporter4a = Teleport(1370, 185, 20, 70, 280, 440)
    teleporter4b = Teleport(260, 405, 70, 20, 280, 440)
    teleporter5a = Teleport(325, 770, 70, 20, 80, 730)
    teleporter5b = Teleport(60, 770, 70, 20, 80, 730)
    teleporter6a = Teleport(15, 555, 20, 70, 300, 135)
    teleporter6b = Teleport(350, 105, 20, 70, 55 , 580)
    teleporter7a = Teleport(15, 105, 20, 70, 1300, 450)
    teleporter7b = Teleport(1280, 405, 70, 20, 1300, 450)
    teleporter8a = Teleport(1280, 775, 70, 20, 180, 310)
    teleporter8b = Teleport(160, 355, 70, 20, 180, 310)
    teleporter9a = Teleport(1370, 555, 20, 70, 690, 465)
    teleporter9b = Teleport(665, 520, 70, 20, 690, 465)



    teleports= pygame.sprite.Group()
    teleports.add(
        teleporter1a, 
        teleporter1b,
        teleporter2a,
        teleporter2b,
        teleporter3a,
        teleporter3b,
        teleporter10a,
        teleporter10b,
        teleporter4a,
        teleporter4b,
        teleporter5a,
        teleporter5b,
        teleporter6a,
        teleporter6b,
        teleporter7a,
        teleporter7b,
        teleporter8a,
        teleporter8b,
        teleporter9a,
        teleporter9b
        )    


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 500
    times_up = False

    bg = pygame.image.load('assets/import/map6.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)

    debug_font = pygame.font.SysFont("comicsansms",20)
    debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
    debug_rect = debug_text.get_rect()
    debug_rect.topleft = (30, 10)

 
    noetebook = pygame.Rect(35, 290, 25, 30)
    coin = pygame.Rect(1125, 430, 15, 15)
    
    transparent_color = RED
    alpha = 0
    shop = pygame.Surface((200, 100), pygame.SRCALPHA)
    shop.fill((transparent_color[0], transparent_color[1], transparent_color[2], alpha))
    
    global noetebook_collected
    global coint_collected
    global coint_given
    


    done = False
    coint_collected = False
    coint_given = False
    noetebook_collected = False

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
        
        keys = pygame.key.get_pressed()
        player.update(keys)

        
        for teleporter in teleports:
            if player.rect.colliderect(teleporter.rect):
                player.rect.topleft = teleporter.exit_pos


        if not noetebook_collected:
            pygame.draw.rect(screen, GREEN, noetebook)
            

        if player.rect.colliderect(noetebook):
            noetebook_collected = True

        if not coint_collected:
            pygame.draw.circle(screen, (230, 182, 28), (1125, 430), 15)
            

        if player.rect.colliderect(coin):
            coint_collected = True

        if player.rect.colliderect(pygame.Rect(395, 590, 200, 100)):
            if coint_collected:
                coint_given = True
            

        if coint_given:
            player.updateSpeed()


        if player.rect.colliderect(exit):
            if noetebook_collected == True:   
                import test
                test.main()         
                done = True

                
        pygame.draw.rect(screen, GREEN, exit)
        player_sprites.draw(screen)
        teleports.draw(screen)
        walls.draw(screen)
        
        screen.blit(shop, (395, 590))

        countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
        screen.blit(countdown_text, countdown_rect)
        debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
        screen.blit(debug_text, debug_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
