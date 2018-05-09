import jugador
class Equipo():
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.puntos  = 0
    @property
    def nombres(self):
        return self.player1.nombre + " " + self.player2.nombre