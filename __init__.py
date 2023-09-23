from PseudoRandom import generatorVichmanHill
from Tester import *

if __name__ == '__main__':
    random = generatorVichmanHill()
    FirstTest = FrequencyBitTest()
    SecondTest = FrequencyBlockTest()
    
    print ('Результат частотного побитового теста: {}'. format(FirstTest.test(random.generate())))
    print ('Результат частотного блочного теста: %s' % SecondTest.test(random.generate()))

