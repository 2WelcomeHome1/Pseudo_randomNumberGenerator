class generatorVichmanHill():
  def __init__(self, _x=87, _y=45, _z=65, _n=20, _k=1) -> int:
    self.X = _x
    self.Y = _y
    self.Z = _z
    self.N = _n # кол-во периодов 
    self.K = _k # влияет на значение x, делит еденицу на определенное кол-во частей
  
  ## Генератор
  def random(self):
    self.X = (171 * self.X) % 30269
    self.Y = (172 * self.Y) % 30307
    self.Z = (170 * self.Z) % 30323
    return (self.X/30269 + self.Y/30307 + self.Z/30323)%1.0

  ## Перевод в массив
  def get (self, min, max) :
      return int(self.random()*(max-min+1)+min)
  
  def generate(self):
     return [self.get(0, self.K) for i in range (self.N)]
  


