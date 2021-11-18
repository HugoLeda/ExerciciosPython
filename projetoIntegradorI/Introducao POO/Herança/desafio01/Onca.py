from Felino import Felino

class Onca(Felino):
  def __init__(self, nome: str, sexo: str, garras: bool):
    super().__init__(nome, sexo, garras)

  def rugir(self):
    print(f'{self.nome} rugiu!')
    