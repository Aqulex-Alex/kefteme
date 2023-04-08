
from time import *
from pygame import *
from random import *
mixer.init()
font.init()
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\User\AppData\Local\Programs\Algoritmika\vscode\data\extensions\algoritmika.algopython-20230320.193254.0\data\student\1010573\184431\rocket.png' , 0)

window = display.set_mode((700, 500))
display.set_caption("ohio")
background = transform.scale(image.load('galaxy.jpeg'),(700, 500))
window.blit(background, (0,0))

font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
monsters = sprite.Group()

score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.y, randint(1, 10))
        bullets.add(bullet)

class Monsters(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.y = randint(50, 650)
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

for i in range(5):
    monster =  Monsters("ufo.png", randint(60, 650), 0, 3)
    monsters.add(monster)

bullets = sprite.Group()

mixer.music.load("Kefteme.mp3")
mixer.music.play()

player = GameSprite("rocket.png", 420, 420, 4)


clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background,(0, 0))
    player.reset()
    player.update()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    text_lose = font1.render("Попущено:" + str(lost), True, (255, 255, 255))
    text_win = font1.render("Избито:" + str(score), True, (255, 255, 255))
    window.blit(text_lose,(0,20))
    window.blit(text_win,(0,0))
    kp = key.get_pressed()
    if score == 100:
        game1 = True
        game = False
    if lost == 200:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\User\AppData\Local\Programs\Algoritmika\vscode\data\extensions\algoritmika.algopython-20230320.193254.0\data\student\1010573\184431\ufo.png' , 0)
        game = False
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()  
    if sprite.groupcollide(monsters, bullets, True, True):
        monster = Monsters("ufo.png", randint(80, 620), 50, randint(1, 10))
        monsters.add(monster)
        score += 1
    clock.tick(FPS)
    display.update()

game1 = False
while game1:
    window.blit(background,(0, 0))
    player.reset()
    player.update()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    text_lose = font1.render("Попущено:" + str(lost), True, (255, 255, 255))
    text_win = font1.render("Избито:" + str(score), True, (255, 255, 255))
    window.blit(text_lose,(0,20))
    window.blit(text_win,(0,0))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()
    if sprite.groupcollide(monsters, bullets, True, True):
        monster = Monsters("ufo.png", randint(80, 620), 50, randint(1, 10))
        monsters.add(monster)
        score += 1
    clock.tick(FPS)
    display.update()
