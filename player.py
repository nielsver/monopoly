from string import capwords


class player():
    def __init__(self, image, x_pos, y_pos, money, cards, name):
        self.image = image
        self.money = money
        self.cards = cards
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image,(self.x_pos, self.y_pos))
        
    
        
