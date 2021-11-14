class Animal:
  def __init__(self, nome: str, sexo: str):
    self.nome = nome
    self.sexo = sexo

  def exibirDados(self):
    print(f'Nome: {self.nome}\nSexo: {self.sexo}')

  def cacar(self):
    print(f'{self.nome} caçou!')

  def comer(self):
    print(f'{self.nome} comeu!')

  def dormir(self):
    print(f'{self.nome} dormiu!')