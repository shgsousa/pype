def q(p_wf, p_r, q_max):
    """
    Calculate the flow rate of an oil well using Vogel's Inflow Performance Relationship (IPR).

    Parameters:
    p_wf : float
        Bottomhole flowing pressure (psia)
    p_r : float
        Average reservoir pressure (psia)
    q_max : float
        Maximum flow rate at zero bottomhole flowing pressure (STB/day)

    Returns:
    q : float
        Flow rate at bottomhole flowing pressure p_wf (STB/day)
    """
    # Validate input pressures
    if p_wf < 0 or p_r <= 0:
        raise ValueError("Pressures must be positive values.")
    if p_wf > p_r:
        raise ValueError("Bottomhole flowing pressure must be less than or equal to reservoir pressure.")

    # Calculate the dimensionless pressure ratio
    p_ratio = p_wf / p_r

    # Implement Vogel's equation
    q = q_max * (1 - 0.2 * p_ratio - 0.8 * p_ratio**2)
    return q

def calculate_qmax(q1, p_wf1, p_r):
    """
    Calculate the maximum flow rate q_max using Vogel's equation and a known flow rate q1 at p_wf1.

    Parameters:
    q1 : float
        Known flow rate at bottomhole flowing pressure p_wf1 (STB/day)
    p_wf1 : float
        Known bottomhole flowing pressure (psia)
    p_r : float
        Average reservoir pressure (psia)

    Returns:
    q_max : float
        Maximum flow rate at zero bottomhole flowing pressure (STB/day)
    """
    # Validate input pressures
    if p_wf1 < 0 or p_r <= 0:
        raise ValueError("Pressures must be positive values.")
    if p_wf1 > p_r:
        raise ValueError("Bottomhole flowing pressure must be less than or equal to reservoir pressure.")

    # Calculate the dimensionless pressure ratio
    p_ratio = p_wf1 / p_r

    # Rearrange Vogel's equation to solve for q_max
    q_max = q1 / (1 - 0.2 * p_ratio - 0.8 * p_ratio**2)
    return q_max
