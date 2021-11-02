#  Crie a classe Restaurante. O método __init__ deve armazenar o nome e o estilo da cozinha do restaurante. Crie também os métodos: exibirDados, que exibirá as duas informações anteriores e o método abrirRestaurante, que exibirá que o restaurante está aberto.

class Restaurante:
  def __init__(self, n, estilo):
    self.nome = n
    self.estiloCozinha = estilo
    self.aberto = False
  
  def exibirDados(self):
    print(f'Nome: {self.nome}')
    print(f'Estilo da Cozinha: {self.estiloCozinha}')

  def abrirRestaurante(self):
    if not (self.aberto):
      self.aberto = True
    print(f"Restaurante {self.nome} está aberto!")

restaurante = Restaurante("Personal Grill", "cozinha pequena")
restaurante.exibirDados()
restaurante.abrirRestaurante()