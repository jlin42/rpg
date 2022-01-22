import pygame,sys
clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Death_Sprites = []
        self.attack = []
        self.cast = []
        self.death = []
        self.hurt = []
        self.idle = []
        self.spell = []
        self.walk = []
        self.Death_Sprites.append(self.attack)
        self.Death_Sprites.append(self.cast)
        self.Death_Sprites.append(self.death)
        self.Death_Sprites.append(self.hurt)
        self.Death_Sprites.append(self.idle)
        self.Death_Sprites.append(self.spell)
        self.Death_Sprites.append(self.walk)
        for i in range(10):
            attack = pygame.image.load(f'game/Death/Attack/Bringer-of-Death_Attack_{i+1}.png')
            attack = pygame.transform.scale(attack, (attack.get_width()*3.5,attack.get_height()*3.5))
            self.attack.append(attack)
            death = pygame.image.load(f'game/Death/Death/Bringer-of-Death_Death_{i+1}.png')
            death = pygame.transform.scale(death, (death.get_width()*3.5,death.get_height()*3.5))
            self.death.append(death)
        for i in range(9):
            cast = pygame.image.load(f'game/Death/Cast/Bringer-of-Death_Cast_{i+1}.png')
            cast = pygame.transform.scale(cast, (cast.get_width()*3.5,cast.get_height()*3.5))
            self.cast.append(cast)
        for i in range(3):
            hurt = pygame.image.load(f'game/Death/Hurt/Bringer-of-Death_Hurt_{i+1}.png')
            hurt = pygame.transform.scale(hurt, (hurt.get_width()*3.5,hurt.get_height()*3.5))
            self.hurt.append(hurt)
        for i in range(8):
            idle = pygame.image.load(f'game/Death/Idle/Bringer-of-Death_Idle_{i+1}.png')
            idle = pygame.transform.scale(idle, (idle.get_width()*3.5,idle.get_height()*3.5))
            self.idle.append(idle)
            walk = pygame.image.load(f'game/Death/Walk/Bringer-of-Death_Walk_{i+1}.png')
            walk = pygame.transform.scale(walk, (walk.get_width()*3.5,walk.get_height()*3.5))
            self.walk.append(walk)
        for i in range(16):
            spell = pygame.image.load(f'game/Death/Spell/Bringer-of-Death_Spell_{i+1}.png')
            spell = pygame.transform.scale(spell, (spell.get_width()*3.5,spell.get_height()*3.5))
            self.spell.append(spell)
        
        self.action = 0
        self.frames = 0
        
        self.image = self.Death_Sprites[self.action][int(self.frames)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.frames += 0.2
            
        if int(self.frames) >= len(self.Death_Sprites[self.action]):
            self.action = 4
            self.frames = 0
            

        self.image = self.Death_Sprites[self.action][int(self.frames)]


screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

moving_sprites = pygame.sprite.Group()
enemy = Enemy(200, 200)
moving_sprites.add(enemy)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemy.action = 0
                enemy.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                enemy.action == 4
                enemy.update()
                
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    clock.tick(60)

    pygame.display.update()
    