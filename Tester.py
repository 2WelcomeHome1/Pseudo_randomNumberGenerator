import math
import scipy.special as sc

class Test:
  def test():
    pass


class FrequencyBitTest: ## Частотный побитовый тест
  def __init__(self) -> None:
    pass
  
  def _S(self, x, S=0):
    for x_i in x : S=S+x_i if x_i == 1 else S-x_i
    return S
  
  def test(self, x) :
    S =(abs(self._S(x))/len(x))**0.5
    m = (S/2)**0.5
    return math.erfc(m)



class FrequencyBlockTest: ## Частотный блочный тест
  def __init__(self, _N=20) -> None:
    self.N = _N
    pass

  def _a(self, x, a = [], i = 0):
    while i <= self.N-3 :
        a.append(sum(x[:3]))
        del x [0:3]
        i += 3
    return a
  
  def Summer(self, x, Sum=0):
    for a_i in self._a(x): Sum += (a_i/3-0.5)**2
    return Sum

  def test(self, x) :
    X_obs = self.Summer(x) * 3 * 4
    return 1 - sc.gammainc (len(self._a(x))/2, X_obs/2)  