# --------------------------------------------------------------------------
# name       : Newmark.py
# description: method of numerical: 
#                                  " Newmark's method "
#                                   - "constant Avg. Acc"
#                                   - "linear Acc"
# data:      : 20201211
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
# name       : Newmark's method. For " constant Avg. Acc " 
# description: methods based on assumed variation of acceleration, such as
#              Newmark beta method.
#              
#
# data       : 20201211
# author     : garyhsieh
# --------------------------------------------------------------------------
def newmark_const_avg_acc():
    print("const avg acc")

    #_delta_t = delta_t[0]
    #_delta_t = 0.05
    #_delta_t = 0.2
    _delta_t = 0.3

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
        u_init = 0
        u_next_init = 0
        u_prime_init = 0
        u_dprime_init = 0
        
        _ui = u_init
        _ui_next = u_next_init
        _ui_prime = u_prime_init
        _ui_dprime = u_dprime_init
        
        _Pi = 0
        _Pi_next = 0
        _Pi_hat = 0
        _Pi_hat_next = 0


        # force at time is 0 sec.
        _Pi = P0 * math.sin(2 * pi * 0 * Tn / _td)

        # k = 1, means a don't include k item.
        _ui_dprime = _Pi * (Wn ** 2) / k - 2 * ksee * Wn * _ui_prime - k * _ui

        a1 = k * (4 / var00 **2 + 4 * ksee / var00)
        a2 = k * (4 / var00 + 2 * ksee) / Wn
        a3 = k / Wn ** 2
        k_hat = k + a1

        print("-----------------------------------------------------------------------------------")
        print("%12s %12s %12s %12s %12s %12s %12s %12s" % ("td", "delta t", "a1", "a2", "a3", "k_hat", \
                "Pi init", "Pi hat init"))
        print("%12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f" % (_td, _delta_t, a1, a2, a3, k_hat, \
                _Pi, _ui_dprime))
        print("-----------------------------------------------------------------------------------")

        print("%04s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                    "Pi_hat", "ui_dprime", "ui_prime", "ui", "Theoreical ui"))

        Pi = []
        ui = []
        ui_prime = []
        ui_dprime = []
        for i in np.arange(0, _tdtn, _delta_t / Tn):
            
            _Pi = 0
            if i * Tn < _tddtn * Tn:
                _Pi = P0 * math.sin(2 * pi * i * Tn / _td)
                _Pi_next = P0 * math.sin(2 * pi * (i * Tn + _delta_t) / _td) 

            _Pi_hat_next = _Pi_next + a1 * _ui + a2 * _ui_prime + a3 * _ui_dprime

            _ui_next = _Pi_hat_next / k_hat
            _ui_prime_next = (2 / _delta_t) * (_ui_next - _ui) - _ui_prime
            _ui_dprime_next = (4 / (_delta_t ** 2)) * (_ui_next - _ui) - (4 / _delta_t) * _ui_prime - _ui_dprime

            print("%+4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %12s" % \
                    (i * Tn, _Pi, _Pi_hat, _ui_dprime, _ui_prime, _ui, "----"))

            # here ui = ui / (P0/k)
            ui.append(_ui)
            ui_prime.append(_ui_prime)
            ui_dprime.append(_ui_dprime)

            _ui = _ui_next
            _ui_prime = _ui_prime_next
            _ui_dprime = _ui_dprime_next

            _Pi_hat = _Pi_hat_next

        plt.figure(figsize = (20, 6))
        plt.plot(uforcedx, uforced, label = "forced, td/Tn = " + str(_tddtn))
        plt.plot(ufreex, ufree, label = "free, td/Tn =" + str(_tddtn))
        plt.plot(ustx, ust, label = "ust, td/Tn =" + str(_tddtn))
        plt.plot(np.arange(0, _tdtn, _delta_t / Tn), ui, label = "Newmark's linear acc, td/Tn =" + str(_tddtn))
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(ust)0")

        plt.show()
 
# --------------------------------------------------------------------------
# name       : Newmark's method for " linear Acc. " 
# description: methods based on assumed variation of acceleration, such as
#              Newmark beta method.
#              
#
# data       : 20201211
# author     : garyhsieh
# --------------------------------------------------------------------------
def newmark_linear_acc():
    print("linear acc")

    #_delta_t = delta_t[0]
    #_delta_t = 0.05
    #_delta_t = 0.2
    _delta_t = 0.3

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
        u_init = 0
        u_next_init = 0
        u_prime_init = 0
        u_dprime_init = 0
        
        _ui = u_init
        _ui_next = u_next_init
        _ui_prime = u_prime_init
        _ui_dprime = u_dprime_init
        
        _Pi = 0
        _Pi_next = 0
        _Pi_hat = 0
        _Pi_hat_next = 0


        # force at time is 0 sec.
        _Pi = P0 * math.sin(2 * pi * 0 * Tn / _td)

        # k = 1, means a don't include k item.
        _ui_dprime = _Pi * (Wn ** 2) / k - 2 * ksee * Wn * _ui_prime - k * _ui

        a1 = k * (6 / var00 **2 + 6 * ksee / var00)
        a2 = k * (6 / var00 + 4 * ksee) / Wn
        a3 = k * (2 / Wn **2 + _delta_t * ksee / Wn)
        k_hat = k + a1

        print("-----------------------------------------------------------------------------------")
        print("%12s %12s %12s %12s %12s %12s %12s %12s" % ("td", "delta t", "a1", "a2", "a3", "k_hat", \
                "Pi init", "Pi hat init"))
        print("%12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f" % (_td, _delta_t, a1, a2, a3, k_hat, \
                _Pi, _ui_dprime))
        print("-----------------------------------------------------------------------------------")

        print("%04s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                    "Pi_hat", "ui_dprime", "ui_prime", "ui", "Theoreical ui"))

        Pi = []
        ui = []
        ui_prime = []
        ui_dprime = []
        for i in np.arange(0, _tdtn, _delta_t / Tn):
            
            _Pi = 0
            if i * Tn < _tddtn * Tn:
                _Pi = P0 * math.sin(2 * pi * i * Tn / _td)
                _Pi_next = P0 * math.sin(2 * pi * (i * Tn + _delta_t) / _td) 

            _Pi_hat_next = _Pi_next + a1 * _ui + a2 * _ui_prime + a3 * _ui_dprime

            _ui_next = _Pi_hat_next / k_hat
            _ui_prime_next = (3 / _delta_t) * (_ui_next - _ui) - 2 * _ui_prime - (_delta_t / 2) * _ui_dprime
            _ui_dprime_next = (6 / (_delta_t ** 2)) * (_ui_next - _ui) - (6 / _delta_t) * _ui_prime - 2 * _ui_dprime

            print("%+4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %12s" % \
                    (i * Tn, _Pi, _Pi_hat, _ui_dprime, _ui_prime, _ui, "----"))

            # here ui = ui / (P0/k)
            ui.append(_ui)
            ui_prime.append(_ui_prime)
            ui_dprime.append(_ui_dprime)

            _ui = _ui_next
            _ui_prime = _ui_prime_next
            _ui_dprime = _ui_dprime_next

            _Pi_hat = _Pi_hat_next

        plt.figure(figsize = (20, 6))
        plt.plot(uforcedx, uforced, label = "forced, td/Tn = " + str(_tddtn))
        plt.plot(ufreex, ufree, label = "free, td/Tn =" + str(_tddtn))
        plt.plot(ustx, ust, label = "ust, td/Tn =" + str(_tddtn))
        plt.plot(np.arange(0, _tdtn, _delta_t / Tn), ui, label = "Newmark's linear acc, td/Tn =" + str(_tddtn))
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(ust)0")

        plt.show()
    



if __name__ == "__main__":
    #newmark_const_avg_acc()
    newmark_linear_acc()
    
