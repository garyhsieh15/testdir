# --------------------------------------------------------------------------
# name       : central_difference.py
# description: method of numerical: 
#                                  "central difference method"
#
# data       : 20201211
# author     : garyhsieh
# --------------------------------------------------------------------------
import numpy as np
import math
import matplotlib.pyplot as plt

import draw_func as dfc


# define pi value
pi = 3.1415926

# damping ratio, ksee
ksee = 0.0

# set stiffness k = 1
k = 1


# force P0 of amplitude
P0 = 1.0

# force P0 of time during
td = [1.0]

# time step
delta_t = [0.1]

# td/Tn, td divide Tn
#tddtn = [2.5, 1.0, 2.2]
tddtn = [2.5]

# t/Tn
tdtn = 2 * tddtn

# natural period Tn
Tn = td[0] / tddtn[0]

# calc Wn value, Wn = 2 * pi / Tn, Tn = td / tddtn
Wn = 2 * pi / Tn
WD = Wn * ((1 - ksee ** 2) ** 0.5)

# --------------------------------------------------------------------------
# name       : central difference method 
# description: finite difference expressions of velocity and acceleration, 
#              such as central difference method.
#
# data       : 20201211
# author     : garyhsieh
# --------------------------------------------------------------------------
def cal_central_difference():

    #_delta_t = delta_t[0]
    #_delta_t = 0.01
    #_delta_t = 0.05
    #_delta_t = 0.1
    _delta_t = 0.2

    var00 = Wn * _delta_t

    uforced, ufree, ust, uforcedx, ufreex, ustx = dfc.theo_sol()

    print("---------------------------------------------------------------------------------------")
    print("ksee: ", ksee, "Wn: ", Wn, "WD:", WD)
    print("Wn*delta_t: ", Wn*_delta_t)
    print("---------------------------------------------------------------------------------------")

    for _tddtn in tddtn:
       
        # _tdtn = t / Tn, _tddtn = td / Tn
        _tdtn = 2 * _tddtn
        _td = _tddtn * Tn

        # setting initial u(0)
        u_previous_init = 0
        u_init = 0
        u_prime_init = 0
        u_dprime_init = 0
        
        _ui = u_init
        _ui_previous = u_previous_init
        _ui_prime = u_prime_init
        _ui_dprime = u_dprime_init

        # time is 0 sec.
        _Pi = P0 * math.sin(2 * pi * 0 * Tn / _td)

        # k = 1, means a don't include k item.
        _ui_dprime = _Pi * (Wn ** 2) / k - 2 * ksee * Wn * _ui_prime - k * _ui
        _ui_previous = _ui - _delta_t * _ui_prime + ((_delta_t ** 2) / 2) * _ui_dprime


        k_hat = k * (1 / var00 ** 2 + ksee / var00)
        a = k * (1 / (var00 ** 2) - ksee / (var00))
        b = k * (1 - 2 / var00 ** 2)

        print("-----------------------------------------------------------------------------------")
        print("%12s %12s %12s %12s %12s %12s" % ("td", "u0_dprime", "u0_previous", "k_hat", "a", "b"))
        print("%12.4f %12.4f %12.4f %12.4f %12.4f %12.4f" % (_td, _ui_dprime, _ui_previous, k_hat, a, b))
        print("-----------------------------------------------------------------------------------")

        print("%04s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                    "Pi_hat", "ui-1", "ui", "ui+1", "Theoreical ui"))

        Pi = []
        ui = []
        ui_prime = []
        ui_dprime = []
        for i in np.arange(0, _tdtn, _delta_t / Tn):
            
            _Pi = 0
            if i * Tn < _tddtn * Tn:
                _Pi = P0 * math.sin(2 * pi * i * Tn / _td)

            _Pi_hat = _Pi - k * (1 / var00 ** 2 - ksee / var00) * _ui_previous - k * (1 - 2 / var00 ** 2) * _ui
            _ui_next = _Pi_hat / k_hat
             
            print("%+4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %12s" % \
                    (i * Tn, _Pi, _Pi_hat, _ui_previous, _ui, _ui_next, "----"))
            # here ui = ui / (P0/k)
            ui.append(_ui)
            _ui_previous = _ui
            _ui = _ui_next

        plt.figure(figsize = (20, 6))
        plt.plot(uforcedx, uforced, label = "forced, td/Tn = " + str(_tddtn))
        plt.plot(ufreex, ufree, label = "free, td/Tn =" + str(_tddtn))
        plt.plot(ustx, ust, label = "ust, td/Tn =" + str(_tddtn))
        plt.plot(np.arange(0, _tdtn, _delta_t / Tn), ui, label = "central difference, td/Tn =" + str(_tddtn))
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(ust)0")

        plt.show()
    


if __name__ == "__main__":
    cal_central_difference()
