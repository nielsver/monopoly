from string import capwords


class player():
    def __init__(self, image, pos, money, cards, name):
        self.image = image
        self.money = money
        self.cards = cards
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.name = name

        
    #def checkmoney(money, self):
     #   return self.money
    #def checkcards(cards, self):
     #   return self.cards