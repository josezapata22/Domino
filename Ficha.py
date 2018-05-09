class Ficha():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @property
    def value(self):
        return [self.x,self.y]