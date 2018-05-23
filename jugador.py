class Jugador():
    def __init__(self,nombre,posicion,mano):
        self.nombre = nombre
        self.posicion = posicion
        self.mano = mano
        self.turno = None
        self.puntos=0
    @property
    def dar_turno(self):
        return self.turno