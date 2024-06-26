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
    pygame.display.set_caption("Level 1")   
    pygame.mixer.music.load('assets/music/lvl1.mp3')
    pygame.mixer.music.play(0)
    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((32, 32))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.topleft = (320, 455)
            self.speed = 5

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

            # Check collision with the walls
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
        def __init__(self, x, y, exit_x, exit_y):
            super().__init__()
            self.image = pygame.Surface((20, 70))
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

    # Create player, teleporter, exit, and walls
    player = Player()
    exit = pygame.Rect(WIDTH - 50, HEIGHT // 2, 20, 70)
    player_sprites = pygame.sprite.Group()
    player_sprites.add(player)
    
    
    
    teleporter1a = Teleport((WIDTH // 2) - 20, (HEIGHT // 2), 740, 220)
    teleporter1b = Teleport(715, 210, 740, 220)
    teleporter2a = Teleport(715, 600, 620, 420)



    teleports= pygame.sprite.Group()
    teleports.add(teleporter1a, teleporter2a,teleporter1b)    
    wall_center = Wall(WIDTH // 2, 0, 15, HEIGHT)
    walls = pygame.sprite.Group()
    walls.add(wall_center)
    


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = 100
    times_up = False

    bg = pygame.image.load('assets/import/map1.png')

    countdown_font = pygame.font.SysFont("comicsansms",40)
    countdown_text = countdown_font.render(f"Timeleft {countdown}", True, (255,255,255))
    countdown_rect = countdown_text.get_rect()
    countdown_rect.center = (WIDTH // 2, 40)

    debug_font = pygame.font.SysFont("comicsansms",20)
    debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
    debug_rect = debug_text.get_rect()
    debug_rect.topleft = (30, 10)


    # Main game loop
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
        
        keys = pygame.key.get_pressed()
        player.update(keys)

        
        for teleporter in teleports:
            if player.rect.colliderect(teleporter.rect):
                player.rect.topleft = teleporter.exit_pos

        
        if player.rect.colliderect(exit):
            import lvl2
            lvl2.main()
            done = True

                
        pygame.draw.rect(screen, GREEN, exit)
        player_sprites.draw(screen)
        teleports.draw(screen)
        walls.draw(screen)
        countdown_text = countdown_font.render(f"Time left {countdown}", True, (255,255,255))
        screen.blit(countdown_text, countdown_rect)
        # debug_text = debug_font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
        # screen.blit(debug_text, debug_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
