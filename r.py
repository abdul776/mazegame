import pygame

pygame.init()

jam = pygame.time.Clock()
back = (245, 212, 251)
mw = pygame.display.set_mode((500,500))
mw.fill(back)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
       #warna isi - bisa parameter yang dioperkan atau warna umum latar belakang
        self.fill_color = color

    def color(self, new_color):
        self.fill_color=new_color
    
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

   #gambar segiempat dengan teks
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  

Yellow = (223, 255, 55)
Dark_grey = (152, 152, 152)
grey = (80, 80, 80)
pink = (242, 106, 234)
cream = (242, 182, 106)

cards = []
num_cards= 4

x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, Yellow)
    new_card.outline(Dark_grey, 5)
    new_card.set_text("KLIK", 28)
    cards.append(new_card)
    x = x+100

while True:
    for card in cards:
        card.draw(10,30)

    pygame.display.update()
    jam.tick(40)