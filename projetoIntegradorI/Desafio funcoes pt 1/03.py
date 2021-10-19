# Faça uma função que receba uma mensagem como parâmetro e mostra um título adaptado a mensagem.

def adaptarTitulo(msg: str):
  msg = msg.split(" ")
  titulo = ''
  for i in range(5):
    titulo += msg[i] + " "

  return titulo

msg = input('Escreva uma mensagem: ')
titulo = adaptarTitulo(msg)
print(f'Titulo adaptado {titulo}')