from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

simplify((k + 1)**3 - 3 * (k + 1)**2 + 2 * (k + 1))
expand((k + 1) * (k) * (2 * (k+1) + 1))
expand(k*(k-1)*(2*k-1))
#^^ Example

expand(k*(k+1)*(k+2))
expand((k+1)*(k+2)*(k+3))
