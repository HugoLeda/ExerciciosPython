from Canino import Canino

class Lobo(Canino):
  def __init__(self, nome: str, sexo: str, garras, carnivoro: bool):
    super().__init__(nome, sexo, garras)
    self.carnivoro = carnivoro

  def construirMatilha(self):
    print(f'{self.nome} fez matilha!')