# Генератор псевдослучайных чисел Вичмана-Хилла

Генератор Вичмана-Хилла - это генератор псевдослучайных чисел, предложенный в 1982 году Дэвидом Хиллом. Он состоит из трех линейных конгруэнтных генераторов с разными простыми модулями, каждый из которых используется для получения равномерно распределенного числа между 0 и 1. Они суммируются, для получения результата по модулю 1. 

U=(X/30269+ Y/30307+ Z/30323)mod1,0 			(3)

Поскольку алгоритм Вичмана-Хилла использует три разных генерирующих уравнения, он требует трех начальных значений. В этом алгоритме три m-значения равны 30269, 30307 и 30323, и три начальных значения в диапазоне [1, 30000].

X=(171*X)mod 30269 					(4)

Y=(172*Y)mod 30307 					(5)

Z=(170*Z) mod 30323 					(6)

Алгоритм Вичмана-Хилла лишь немного труднее в реализации, чем алгоритм Лемера. Преимущество первого над вторым в том, что алгоритм Вичмана-Хилла генерирует более длинную последовательность до того, как начнет повторяться. Суммирование трех генераторов дает псевдослучайную последовательность с циклом, превышающим 6,95 × 10.

## Исследование  ГПСЧ Вичмана – Хилла 
 В современном мире не существует единого «официального» набора критериев, оценивающих безопасность применяемых случайных последовательностей. Одним из примеров таких критериев являются статистические тесты NIST. Эти тесты основаны на различных статистических свойствах, присущих только случайным последовательностям.
В данной работе представлены два метода тестирования ГПСЧ:
- Частотный побитовый тест;
- Частотный блочный тест.

### Частотный побитовый тест
Частотный побитовый тест заключается в определении соотношения между нулями и единицами во всей двоичной последовательности. 
Цель — выяснить, действительно ли число нулей и единиц в последовательности приблизительно одинаковы, как это можно было бы предположить в случае истинно случайной бинарной последовательности. 
Тест оценивает, насколько близка доля единиц к 0,5. Таким образом, число нулей и единиц должно быть примерно одинаковым. Если вычисленное в ходе теста значение вероятности p < 0,01, то данная двоичная последовательность не является истинно случайной. В противном случае последовательность носит случайный характер. Стоит отметить, что все последующие тесты проводятся при условии, что пройден данный тест.
Далее представлен программный код реализации данного теста на основе разработанного ГПСЧ Вичмана-Хилла:

**Результат частотного побитового теста: 0.3692384594585355, что больше 0,01.**

Вывод: полученная последовательность является случайной, т.к. вычисленное в ходе теста значение вероятности p > 0,01, что говорит о том, что разработанный ранее алгоритм ГПСЧ Вичмана-Хилла успешно реализован

### Частотный блочный тест
Суть частотного блочного теста — в определении доли единиц внутри блока длиной m бит.
Цель — выяснить действительно ли частота повторения единиц в блоке длиной m бит приблизительно равна m/2, как можно было бы предположить в случае абсолютно случайной последовательности. 
Вычисленное в ходе теста значение вероятности p должно быть не меньше 0,01. В противном случае (p < 0,01) двоичная последовательность не носит истинно случайный характер.
Далее представлен программный код реализации данного теста на основе разработанного ГПСЧ Вичмана-Хилла:

**Результат частотного блочного теста: 0.9681965935520788, что больше 0,01**

Вывод: полученная последовательность является случайной, т.к. вычисленное в ходе теста значение вероятности p > 0,01, что говорит о том, что разработанный ранее алгоритм ГПСЧ Вичмана-Хилла успешно реализован.