from Animal import Animal

class Canino(Animal):
  def __init__(self, nome: str, sexo: str, garras: bool):
    super().__init__(nome, sexo)
    self.garrasExpostas = garras

  def uivar(self):
    print(f'{self.nome} uivou!')

  def rosnar(self):
    print(f'{self.nome} rosnou!')