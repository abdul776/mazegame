from pygame import *


#parent class untuk sprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#kelas penerus untuk sprite pemain (dikontrol oleh panah)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < min_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < min_width - 80:
           self.rect.y += self.speed


#kelas penerus untuk sprite musuh (bergerak sendiri)
class Enemy(GameSprite):
   direction = "left"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "right"
       if self.rect.x >= min_width - 85:
           self.direction = "left"
       if self.direction == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        #wall image – a rectangle of the required size and color
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
 
        #every sprite must store the rect – rectangular property
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


min_width = 700
min_height = 500
window = display.set_mode((min_width, min_height))
display.set_caption("Maze Game")
background = transform.scale(image.load("back.jpg"), (min_width, min_height))

#karakter game akan ditampilkan
mario = Player("mario.png", 5, min_height-80, 4)
mushroom = GameSprite("mushroom.png", min_width-120, min_height-80, 0)
turtle = Enemy("turtle.png", min_width-80, 280, 2)

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 300, 250, 350, 10)

font.init()
font = font.Font(None, 70)
win = font.render("You WIN!", True, (154, 205, 50))
lose = font.render("You lose!", True, (246, 5, 5))


game = True
finish = False
clock = time.Clock()
FPS = 60

#sound didalam game
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        mario.update()
        turtle.update()

        mario.reset()
        mushroom.reset()
        turtle.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        #Lost game
        if sprite.collide_rect(mario, turtle) or sprite.collide_rect(mario, w1) or sprite.collide_rect(mario, w2) or sprite.collide_rect(mario, w3) or sprite.collide_rect(mario, w4):
            finish = True
            window.blit(lose, (200, 200))

        #menang
        if sprite.collide_rect(mario, mushroom):
            finish = True
            window.blit(win, (200, 200))

    display.update()
    clock.tick(FPS)

















