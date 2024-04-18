import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BROWN = (122, 49, 0)
    pygame.display.set_caption("Level 3")   

    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((32, 32))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.topleft = (80, 150)
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
    exit = pygame.Rect(820, 435, 20, 70)
    
    player_sprites = pygame.sprite.Group()
    player_sprites.add(player)
    
    wallhorizontal = Wall(1000, 0, 15, 650)
    walltop = Wall(0, 255, 1000, 15 )
    wallvertical = Wall(1015, 450, 400, 15)
    wallvertical2 = Wall(860, 400, 15, 135)
    wallvertical3 = Wall(185, 400, 15, 260)
    wallbottom = Wall(185, 650, 830, 15 )
    wallbottom2 = Wall(185, 400, 680, 15 )
    wallbottom3 = Wall(340, 520, 525, 15)
 
    
    walls = pygame.sprite.Group()
    walls.add(
        wallhorizontal, 
        walltop,
        wallvertical,
        wallvertical2,
        wallvertical3,
        wallbottom,
        wallbottom2,
        wallbottom3
        )
    
    teleporter1a = Teleport(970, 130, 20, 70, 1300, 285)
    teleporter1b = Teleport(1370, 260, 20, 70,  1300, 285)
    teleporter2a = Teleport(1170, 420, 70, 20, 1190, 510)
    teleporter2b = Teleport(1170, 475, 70, 20, 1185, 380)


    teleports= pygame.sprite.Group()
    teleports.add(
        teleporter1a, 
        teleporter1b,
        teleporter2a,
        teleporter2b,
        )    


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 20
    times_up = False

    bg = pygame.image.load('assets/import/map3.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)

    debug_font = pygame.font.SysFont("comicsansms",20)
    debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
    debug_rect = debug_text.get_rect()
    debug_rect.topleft = (30, 10)

    transparent_color = RED
    alpha = 0
    shop = pygame.Surface((200, 100), pygame.SRCALPHA)
    shop.fill((transparent_color[0], transparent_color[1], transparent_color[2], alpha))
    
    coin = pygame.Rect(330, 150, 15, 15)
    global coint_collected
    global coint_given
    

    done = False
    coint_collected = False
    coint_given = False


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

        
        if not coint_collected:
            pygame.draw.circle(screen, (230, 182, 28), (330, 150), 15)
            

        if player.rect.colliderect(coin):
            coint_collected = True

        if player.rect.colliderect(pygame.Rect(1100, 100, 200, 100)):
            coint_given = True
            

        if coint_given:
            player.updateSpeed()


        if player.rect.colliderect(exit):
            import lvl2
            lvl2.main()
            done = True

                
        pygame.draw.rect(screen, GREEN, exit)
        player_sprites.draw(screen)
        teleports.draw(screen)
        walls.draw(screen)
        
        
        screen.blit(shop, (1100, 100))


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
