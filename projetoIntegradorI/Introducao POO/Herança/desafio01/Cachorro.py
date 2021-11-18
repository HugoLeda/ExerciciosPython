from Canino import Canino

class Cachorro(Canino):
  def __init__(self, nome: str, sexo: str, garras: bool, onivoro: bool):
    super().__init__(nome, sexo, garras)
    self.onivoro = onivoro

  def latir(self):
    print(f'{self.nome} latiu!')