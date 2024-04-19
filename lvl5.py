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
    pygame.display.set_caption("Level 5")   

    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((32, 32))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.topleft = (845, 510)
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
    exit = pygame.Rect(1295, 530, 70, 20)
    
    player_sprites = pygame.sprite.Group()
    player_sprites.add(player)
    
    wallmaintop = Wall(430, 250, 1000, 15)
    wallmainright = Wall(430, 0, 15, 570)
    wallmainleft = Wall(925, 265, 15, 320)
    wallmainbottom = Wall(430, 570, 1000, 15)
    wallroom1bottom = Wall(0, 470, 440, 15)
    wallroom2right = Wall(625, 580, 15, 325)
    wallroom4right = Wall(690, 80, 15, 180)
    wallroom5right = Wall(1245, 265, 15, 320)
    wallroom6right = Wall(1050, 570, 15, 320)
    
    
    walls = pygame.sprite.Group()
    walls.add(
        wallmaintop,
        wallmainright,
        wallmainleft,
        wallmainbottom,
        wallroom1bottom,
        wallroom2right,
        wallroom4right,
        wallroom5right,
        wallroom6right
        
        )
    
    teleporter1a = Teleport(655, 540, 70, 20, 190, 385)
    teleporter1b = Teleport(170, 440, 70, 20, 190, 385)
    teleporter2a = Teleport(10, 120, 20, 70, 1310, 150)
    teleporter2b = Teleport(1370, 120, 20, 70, 1310, 150)
    teleporter3a = Teleport(1055, 220, 70, 20, 1075, 305)
    teleporter3b = Teleport(1055, 270, 70, 20, 1075, 305)
    teleporter4a = Teleport(950, 385, 20, 70, 55, 700)
    teleporter4b = Teleport(10, 680, 20, 70, 55, 700)
    teleporter5a = Teleport(595, 680, 20, 70, 770, 140)
    teleporter5b = Teleport(715, 120, 20, 70, 770, 140)
    teleporter6a = Teleport(1055, 545, 70, 20, 555, 185)
    teleporter6b = Teleport(540, 220, 70, 20, 555, 185)
    teleporter7a = Teleport(460, 120, 20, 70, 970, 695)
    teleporter7b = Teleport(1020, 680, 20, 70, 970, 695)
    teleporter8a = Teleport(650, 680, 20, 70, 815, 305)
    teleporter8b = Teleport(815, 270, 70, 20, 835, 295)
    teleporter9a = Teleport(455, 385, 20, 70, 1315, 300)
    teleporter9b = Teleport(1295, 270, 70, 20, 845, 415)
    teleporter10a = Teleport(890, 385, 20, 70, 1115, 695)
    teleporter10b = Teleport(1075, 680, 20, 70, 840, 405)
    teleporter11a = Teleport(400, 120, 20, 70, 190, 530)
    teleporter11b = Teleport(170, 500, 70, 20, 350, 135)

    teleports= pygame.sprite.Group()
    teleports.add(
        teleporter1a, 
        teleporter1b,
        teleporter2a,
        teleporter2b,
        teleporter3a,
        teleporter3b,
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
        teleporter9b,
        teleporter10a,
        teleporter10b,
        teleporter11a,
        teleporter11b
        )    


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 50
    times_up = False

    bg = pygame.image.load('assets/import/map5.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)

    debug_font = pygame.font.SysFont("comicsansms",20)
    debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
    debug_rect = debug_text.get_rect()
    debug_rect.topleft = (30, 10)

 
    noetebook = pygame.Rect(635, 110, 25, 30)
    coin = pygame.Rect(1310, 725, 15, 15)
    
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
            pygame.draw.circle(screen, (230, 182, 28), (1310, 725), 15)
            

        if player.rect.colliderect(coin):
            coint_collected = True

        if player.rect.colliderect(pygame.Rect(510, 280, 200, 100)):
            if coint_collected:
                coint_given = True
            

        if coint_given:
            player.updateSpeed()


        if player.rect.colliderect(exit):
            if noetebook_collected == True:            
                import lvl6
                lvl6.main()
                done = True

                
        pygame.draw.rect(screen, GREEN, exit)
        player_sprites.draw(screen)
        teleports.draw(screen)
        walls.draw(screen)
        
        screen.blit(shop, (510, 280))

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
