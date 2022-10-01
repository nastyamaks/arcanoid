import pygame

class Records:
    def __init__(self):
        self.table = []
        self.font = pygame.font.SysFont('Kristen ITC', 50)

    def add(self, name, score):
        is_found = False
        for i in range(len(self.table)):
            if self.table[i][0] == name:
                is_found = True
                if self.table[i][1] < score:
                    self.table[i] = (name, score) 
                break


        if not is_found: 
            self.table.append((name, score))
        self.table.sort(key=lambda elem: (elem[1], elem[0]), reverse=True)
        self.table = self.table[:10]

    def display(self, window):
        y = 50
        for line in self.table: 
            text = self.font.render(line[0] + ' ' + str(line[1]), True, (0, 0, 0))
            window.blit(text, (190, y))
            y += 40
            