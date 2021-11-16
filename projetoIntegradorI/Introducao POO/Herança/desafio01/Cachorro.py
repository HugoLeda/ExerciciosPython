from Canino import Canino

class Cachorro(Canino):
  def __init__(self, onivoro: bool):
    self.onivoro = onivoro

  def latir(self):
    print(f'{self.nome} latiu!')