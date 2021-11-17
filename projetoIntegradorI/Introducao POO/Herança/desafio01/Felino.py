from Animal import Animal

class Felino(Animal):
  def __init__(self, nome: str, sexo: str, garras: bool):
    super().__init__(nome, sexo)
    self.garrasRetrateis = garras
  
  def ronronar(self):
    print(f'{self.nome} ronronou!')