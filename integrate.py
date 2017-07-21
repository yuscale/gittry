# -*- coding: utf-8 -*-
# filename integrate.py

from sympy import *
from scipy import integrate


def calArea(lx, ly, amp):
    x, y, z, t = symbols('x y z t')

    amp = 5
    lx = ly =20

    # z = amp * sin(x * 2 * pi / lx ) * sin(2 * pi * y / ly)
    dzdx = 2 * pi / lx * amp * cos(x * 2 * pi / lx ) * sin(2 * pi * y / ly)
    dzdy = 2 * pi / ly * amp * sin(x * 2 * pi / lx ) * cos(2 * pi * y / ly)
    ds = sqrt(1. + dzdy ** 2 + dzdx ** 2)
    return ds
##############


def intergrad(x, y, lx, ly, amp):
    import math
    z = amp * sin(x * 2 * pi / lx) * sin(2 * pi * y / ly)
    # 可以升级的地方，此处的求导是硬求导
    dzdx = 2 * pi / lx * amp * cos(x * 2 * pi / lx ) * sin(2 * pi * y / ly)
    dzdy = 2 * pi / ly * amp * sin(x * 2 * pi / lx ) * cos(2 * pi * y / ly)
    ds = sqrt(1. + dzdy ** 2 + dzdx ** 2)
    return ds

amp = 5
lx = ly =20
area = integrate.dblquad(intergrad, 0, 20, lambda x: 0 , lambda x:20, args = (lx, ly, amp))


