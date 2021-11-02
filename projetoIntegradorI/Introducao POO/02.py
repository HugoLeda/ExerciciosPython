# Crie a classe Usuario. O método __init__ deve criar os atributos primeiroNome e sobrenome. Deve também ter os métodos exibirDados, para exibir os dados criados, e saudar, que exibirá uma saudação personalizada ao usuário, que exiba Olá e o nome do usuário.

class Usuario:
  def __init__(self, primeiroNome, sobrenome):
    self.nome = primeiroNome
    self.sobrenome = sobrenome

  def exibirDados(self):
    print(f'Nome: {self.nome}')

  def saudar(self):
    print(f'Olá: {self.nome} {self.sobrenome}')

user = Usuario("João Hugo", "Leda de Carvalho")
user.saudar()
