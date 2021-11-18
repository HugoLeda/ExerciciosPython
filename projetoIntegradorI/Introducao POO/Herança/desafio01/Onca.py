from Felino import Felino

class Onca(Felino):
  def __init_subclass__(cls) -> None:
      return super().__init_subclass__()