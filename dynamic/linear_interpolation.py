# --------------------------------------------------------------------------
# name       : linear_interpolation.py
# description: linear interpolation of excitation 
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

print("ksee,    td,     Tn,     Wn,     WD:\n ", ksee, td, Tn, Wn, WD)

#print("%8s %8s %8s %8s %8s" % ("ksee", "td", "Tn", "Wn", "WD"))
#print("%8.4f %8s %8s %8s %8s" % (ksee, "td", "Tn", "Wn", "WD"))

# --------------------------------------------------------------------------
# name       : cal_linear_interpolation() 
# description: methods based on interpolation of the excitation.
#              ui+1  = Aui + Bu'i + Cpi + Dpi+1
#              u'i+1 = A'ui + B'u'i + C'pi + D'pi+1
#
# data       : 20201209
# author     : garyhsieh
# --------------------------------------------------------------------------
def cal_linear_interpolation():
    #print("enter linear interpolation")

    uforced, ufree, ust, uforcedx, ufreex, ustx = dfc.theo_sol()
    #print("forced u(t): ", uforced)

    # setting time step
    #_delta_t = delta_t[0]
    #_delta_t = 0.05
    #_delta_t = 0.1
    #_delta_t = 0.2
    _delta_t = 0.3


    var00 = math.exp(-ksee * Wn * _delta_t)
    var01 = math.sin(WD * _delta_t)
    #var01 = WD * _delta_t
    var02 = math.cos(WD * _delta_t)
    var03 = (1 - 2 * ksee ** 2) / (WD * _delta_t)
    var04 = (2 * ksee) / (Wn * _delta_t)
    var05 = 1 + (2 * ksee) / (Wn * _delta_t)
    var06 = Wn / ((1 - ksee ** 2) ** 0.5)
    var07 = ksee / ((1 - ksee ** 2) ** 0.5)

    _A = var00 * (var07 * var01 + var02)
    _B = var00 * (var01 / WD)
    _C = var04 + var00 * ((var03 - var07) * var01 - var05 * var02)
    _D = 1 - var04 + var00 * (- var03 * var01 + var04 * var02)
           
    _Aprime = -var00 * (var06 * var01)
    _Bprime = var00 * (var02 - var07 * var01)
    _Cprime = (-1 / _delta_t) + var00 * ((var06 + var07 / _delta_t) * var01 + (var02 / _delta_t))
    _Dprime = (1 / _delta_t) * (1 - var00 * (var07 * var01 + var02))

    print("---------------------------------------------------------------------------------------")
    print("ksee: ", ksee, "Wn: ", Wn, "WD:", WD)
    print("e**(-ksee*Wn*delta_t: ", math.exp(-ksee*Wn*_delta_t))
    print("sin(WD*delta_t: ", math.sin(WD*_delta_t))
    print("cos(WD*_delta_t:", math.cos(WD*_delta_t))

    print("---------------------------------------------------------------------------------------")

    print("\n%8s %8s %8s %8s %8s %8s %8s %8s" % \
            ("var00", "var01", "var02", "var03", "var04", "var05", "var06", "var07"))
    print("---------------------------------------------------------------------------------------")
    print("%8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f" % \
            (var00, var01, var02, var03, var04, var05, var06, var07))
   
    # tddtn = td / Tn
    for _tddtn in tddtn:
        print("\n            NUMERICAL SOLUTION USING LINEAR INTERPOLATION OF EXCITATION            ")
        print("---------------------------------------------------------------------------------------")
        """
        print("%04s %08s %08s %08s %08s %08s %08s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                "C'Pi", "CPi", "D'Pi+1", "DPi+1", "B'u'i", "Bu'i", "u'i", "A'ui", "Aui", "ui", \
                "Theoreical ui"))
        """
        print("%04s %08s %08s %08s %08s %08s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                "A", "B", "C", "D", "Aui", "Bui'", "CPi", "DPi+1", "ui", "Theoreical ui"))
        """ 
        print("%04s %08s %8s %08s %08s %08s %08s %08s %08s %08s %08s %16s" % ("ti", "Pi", \
                "A'", "B'", "C'", "D'", "A'ui", "B'ui'", "C'Pi", "D'Pi+1", "ui'", "Theoreical ui'"))
        """

        # tdtn = t / Tn
        _tdtn = 2 * _tddtn
        _td = _tddtn * Tn
        # setting initial u(0) and u'(0)
        u_init = 0
        u_prime_init = 0
        
        _ui = u_init
        _ui_prime = u_prime_init

        Pi = []
        ui = []
        ui_prime = []
        #uix = []

        #ui.append(_ui)
        #ui_prime.append(_ui_prime)
        for i in np.arange(0, _tdtn, _delta_t / Tn):
            
            _Pi = 0
            _Pi_next = 0
            if i * Tn < _tddtn * Tn:
                _Pi = P0 * math.sin(2 * pi * i * Tn / _td)
                _Pi_next = P0 * math.sin(2 * pi * (i * Tn + _delta_t) / _td)
            
            """
            _A = var00 * (var07 * var01 + var02)
            _B = var00 * (var01 / WD)
            _C = var04 + var00 * ((var03 - var07) * var01 - var05 * var02)
            _D = 1 - var04 + var00 * (- var03 * var01 + var04 * var02)
           
            _Aprime = var00 * (var06 * var01)
            _Bprime = var00 * (var02 - var07 * var01)
            _Cprime = (-1 / _delta_t) + var00 * ((var06 + var07 / _delta_t) * var01 + (var02 / _delta_t))
            _Dprime = (1 / _delta_t) * (1 - var00 * (var07 * var01 + var02))
            """

            # don't include divide k item.
            _ui_next = _A * _ui + _B * _ui_prime + _C * _Pi + _D * _Pi_next
            _ui_prime_next = _Aprime * _ui + _Bprime * _ui_prime + _Cprime * _Pi + _Dprime * _Pi_next
            
            # _ui_next / (ust)0
            _ui_next = _ui_next / P0
            # _ui_prime_next / (ust)0
            _ui_prime_next = _ui_prime_next / P0

            Pi.append(_Pi)
            ui.append(_ui)
            ui_prime.append(_ui_prime)
            """
            print("%4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %12s" % (i * Tn, _Pi, _Cprime * _Pi, _C * _Pi, _Dprime * _Pi_next, \
                    _D * _Pi_next, _Bprime * _ui_prime, _B * _ui_prime, _ui_prime, _Aprime * _ui, \
                    _A * _ui, _ui,"----"))
            """

            print("%4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %8.4f %12s" % \
                    (i * Tn, _Pi, _A, _B, _C, _D, _A * _ui, _B * _ui_prime, _C * _Pi, \
                    _D * _Pi_next, _ui, "----"))
            """
            print("%4.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %+8.4f %8.4f %12s" % \
                    (i * Tn, _Pi, _Aprime, _Bprime, _Cprime, _Dprime, _Aprime * _ui,\
                    _Bprime * _ui_prime, _Cprime * _Pi, _Dprime * _Pi_next, _ui_prime, "----"))
            """


            _ui = _ui_next
            _ui_prime = _ui_prime_next

            #ui.append(_ui)
            #ui_prime.append(_ui_prime)
   
    plt.figure(figsize = (20, 6))
    plt.plot(uforcedx, uforced, label = "forced, td/Tn = " + str(_tddtn))
    plt.plot(ufreex, ufree, label = "free, td/Tn =" + str(_tddtn))
    plt.plot(ustx, ust, label = "ust, td/Tn =" + str(_tddtn))
    plt.plot(np.arange(0, _tdtn, _delta_t / Tn), ui, label = "numerical, td/Tn =" + str(_tddtn))
    plt.grid(True)
    plt.legend()
    plt.xlabel("t/Tn")
    plt.ylabel("u(t)/(ust)0")

    plt.show()
    
"""       
            print("{:^+4.4f} {:^+4.4f} {:^+4.4f} {:^+4.4f} {:^+8.4f} {:>+8.4f} {:>+8.4f} {:>+8.4f} {}".format(i * Tn, _Pi, _C * _Pi,_D * _Pi_next, _B * _ui_prime, _ui_prime, _A * _ui, _ui,"Theoreical ui"))
"""

if __name__ == "__main__":
    #print("enter main func")
    cal_linear_interpolation()
    #dfc.theo_sol()
