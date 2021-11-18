from Felino import Felino

class Gato(Felino):
  def __init__(self, nome: str, sexo: str, garras: bool):
    super().__init__(nome, sexo, garras)

  def miar(self):
    print(f'{self.nome} miou!')