def q(p_wf, p_r, PI):
    """
    Calculate the flow rate of an oil well using the Productivity Index (PI) Inflow Performance Relationship.

    Parameters:
    p_wf : float
        Bottomhole flowing pressure (psia)
    p_r : float
        Average reservoir pressure (psia)
    PI : float
        Productivity Index (STB/day/psi)

    Returns:
    q : float
        Flow rate at bottomhole flowing pressure p_wf (STB/day)
    """
    # Validate input pressures
    if p_wf < 0 or p_r <= 0:
        raise ValueError("Pressures must be positive values.")
    if p_wf > p_r:
        raise ValueError("Bottomhole flowing pressure must be less than or equal to reservoir pressure.")

    # Calculate flow rate using PI relationship
    delta_p = p_r - p_wf
    q = PI * delta_p
    return q

def calculate_PI(q1, p_r, p_wf1):
    """
    Calculate the Productivity Index (PI) using known flow rate q1 at p_wf1.

    Parameters:
    q1 : float
        Known flow rate at bottomhole flowing pressure p_wf1 (STB/day)
    p_r : float
        Average reservoir pressure (psia)
    p_wf1 : float
        Known bottomhole flowing pressure (psia)

    Returns:
    PI : float
        Productivity Index (STB/day/psi)
    """
    # Validate input pressures
    if p_wf1 < 0 or p_r <= 0:
        raise ValueError("Pressures must be positive values.")
    if p_wf1 > p_r:
        raise ValueError("Bottomhole flowing pressure must be less than or equal to reservoir pressure.")

    # Calculate PI using known data
    delta_p = p_r - p_wf1
    if delta_p == 0:
        raise ValueError("Pressure difference cannot be zero.")
    PI = q1 / delta_p
    return PI

# Example usage:
if __name__ == "__main__":
    # Given parameters
    p_r = 2500  # Reservoir pressure in psia
    p_wf = 1000  # Bottomhole flowing pressure in psia
    q1 = 500  # Known flow rate at p_wf1
    p_wf1 = 1500  # Known bottomhole flowing pressure in psia

    # Calculate PI using known flow rate
    PI = calculate_PI(q1, p_r, p_wf1)
    print(f"Calculated PI: {PI:.4f} STB/day/psi")

    # Calculate flow rate at desired bottomhole pressure
    q = q(p_wf, p_r, PI)
    print(f"Flow rate at p_wf = {p_wf} psia: {q:.2f} STB/day")
