from Animal import Animal
from Felino import Felino
from Canino import Canino
from Gato import Gato
from Onca import Onca
from Cachorro import Cachorro
from Lobo import Lobo


def instanciarAnimal():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  animal = Animal(nome, sexo)
  return animal

def instanciarFelino():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')
  
  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False
  
  felino = Felino(nome, sexo, garras)
  return felino

def instanciarCanino():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')

  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False
  
  canino = Canino(nome, sexo, garras)
  return canino

def instanciarGato():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')

  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False

  gato = Gato(nome, sexo, garras)
  return gato

def instanciarOnca():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')

  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False

  onca = Onca(nome, sexo, garras)
  return onca

def instanciarCachorro():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')

  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False

  onivoro = input('O animal tem garras? [S/N]: ')

  if (onivoro[0].upper() == 'S'):
    onivoro = True
  else:
    onivoro = False

  cachorro = Cachorro(nome, sexo, garras, onivoro)
  return cachorro

def instanciarLobo():
  nome = input('Digite o nome do animal: ')
  sexo = input('Digite o sexo do animal: ')
  garras = input('O animal tem garras? [S/N]: ')

  if (garras[0].upper() == 'S'):
    garras = True
  else:
    garras = False

  lobo = Lobo(nome, sexo, garras, carnivoro = True)