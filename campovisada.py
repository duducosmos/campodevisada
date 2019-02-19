#!/usr/bin/env python3.6
#-*- Coding: UTF-8 -*-
from math import cos, sqrt, pi

def visada(h, H, R, verbose=True):
    dh = sqrt(2 *  h * R  + h ** 2.0)
    dH = sqrt(2 *  H * R  + H ** 2.0)

    dv = dh + dH
    if verbose is True:
        print("O horizonte de h está à: {0:8.2f}km".format(dh/1000))
        print("O horizonte de H está à: {0:8.2f}km".format(dH/1000))
        msg = "A linha de visada entre os dois será dv:"
        msg += "{0:8.2f}km".format(dv / 1000)
        print(msg)

def H(h, ds, R, verbose=True):
    theta = ds / R
    dh = sqrt(2 *  h * R  + h ** 2.0)
    dsh = ds - dh
    H = sqrt(dsh ** 2.0 + R ** 2.0) - R
    if verbose is True:
        print("Angulo entre os dois pontos: \u03B8: {}".format(theta))
        print("Linha do Horizonte de h:{0:9.2f}km".format(1.08 * dh / 1000))
        print("Assumindo h: {0}km, ds: {1}km o valor de H será: {2:9.2f}m".format(h/1000, ds/1000, H))
    return H


if __name__ == "__main__":
    visada(2826, 3880, 6371000)

    from numpy import roots, linspace, array
    import matplotlib.pyplot as plt
    x = linspace(200000, 10000000, 100)
    Hv = array([H(2826, xi, 6371000, verbose=False) for xi in x])
    plt.plot(x / 1000, Hv / 1000)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel(r"$d_{s}$ (km)")
    plt.ylabel(r"H (km)")
    plt.legend()
    plt.show()
