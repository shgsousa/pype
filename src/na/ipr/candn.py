import math
import numpy as np

def match(q1, P_wf1, q2, P_wf2, p_bar):
    """
    Calculate constants C and n from well test data.

    :param q1: Flow rate for the first data point
    :param P_wf1: Flowing bottom-hole pressure for the first data point
    :param q2: Flow rate for the second data point
    :param P_wf2: Flowing bottom-hole pressure for the second data point
    :param p_bar: Average reservoir pressure
    :return: Constants C and n
    """
    # Calculate n
    n = math.log(q1 / q2) / (math.log(p_bar**2 - P_wf1**2) - math.log(p_bar**2 - P_wf2**2))

    # Calculate C
    C = q1 / ((p_bar**2 - P_wf1**2)**n)

    return C, n

def q(C, n, p_bar, p_wf):
    """
    Calculate the flow rate using the given equation.

    :param C: Constant C determined from well test data
    :param n: Exponent n determined from well test data
    :param p_bar: Average reservoir pressure
    :param p_wf: Flowing bottom-hole pressure
    :return: Calculated flow rate q
    """
    q = C * (p_bar**2 - p_wf**2)**n
    return q

def ipr(C, n, p_bar):
    """
    Convenience function to calculate the Inflow Performance Relationship (IPR) for a given set of C, n, and average reservoir pressure.

    :param C: Constant C determined from well test data
    :param n: Exponent n determined from well test data
    :param p_bar: Average reservoir pressure
    :return: IPR as a set of pwf vs. q values
    """
    # Generate a range of bottom-hole pressures between 0 and the average reservoir pressure
    pwf = np.linspace(0,p_bar,100)
    # Calculate the flow rate for each bottom-hole pressure
    _q = [q(C, n, p_bar, x) for x in pwf]
    return list(zip(pwf,_q))