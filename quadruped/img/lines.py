import math
import matplotlib.pyplot as pyplot
xs = [0, 1.2, 2.5, 3.3, 4.2, 5]
ys = [0, 6, -3, 4, -2, 0]
pyplot.plot(xs, ys)
pyplot.grid()
pyplot.savefig('lines.svg', format='svg')
