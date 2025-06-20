import math
from typing import List, Tuple 

def minimum_curvature_method(survey_data: List[Tuple[float, float, float]], initial_easting: float, initial_northing: float, datum: float) -> Tuple[List[float], List[float], List[float]]:
    """
    Calculates the 3D wellbore trajectory using the Minimum Curvature Method.
    Args:
        survey_data (List[Tuple[float, float, float]]): 
            A list of tuples, each containing measured depth (MD), inclination (I), and azimuth (A) in radians.
            Format: [(MD1, I1, A1), (MD2, I2, A2), ...]
        initial_easting (float): 
            The starting easting coordinate.
        initial_northing (float): 
            The starting northing coordinate.
        datum (float): 
            The starting true vertical depth (TVD) at the datum level.
    Returns:
        Tuple[List[float], List[float], List[float]]:
            A tuple containing three lists:
                - Easting coordinates at each survey station.
                - Northing coordinates at each survey station.
                - True vertical depths (TVD) at each survey station.
    Notes:
        - All angles (inclination and azimuth) must be provided in radians.
        - The function assumes the first survey point corresponds to the initial coordinates and datum.
        - The method uses the minimum curvature algorithm to interpolate between survey points.
    """
    # Initialize lists to store results
    easting_list = [initial_easting]
    northing_list = [initial_northing]
    tvd_list = [datum]  # Starting TVD at the specified datum level

    for i in range(1, len(survey_data)):
        # Extract data for two consecutive points
        MD1, I1, A1 = survey_data[i - 1]
        MD2, I2, A2 = survey_data[i]
        
        # Calculate differences
        delta_MD = MD2 - MD1
        delta_A = A2 - A1
        
        # Calculate Dogleg Severity (DLS)
        cos_DLS = math.cos(I1) * math.cos(I2) + math.sin(I1) * math.sin(I2) * math.cos(delta_A)
        DLS = math.acos(cos_DLS) / delta_MD if delta_MD != 0 else 0
        
        # Calculate Radius of Curvature Factor (RF)
        RF = 2 / DLS * math.tan(DLS / 2) if DLS != 0 else 1
        
        # Compute changes in Northing, Easting, and Vertical Section/Depth
        sin_avg_I = (math.sin(I1) + math.sin(I2)) / 2
        cos_avg_A = math.cos((A1 + A2) / 2)
        sin_avg_A = math.sin((A1 + A2) / 2)
        
        delta_Northing = RF * delta_MD * sin_avg_I * cos_avg_A
        delta_Easting = RF * delta_MD * sin_avg_I * sin_avg_A
        delta_TVD = RF * delta_MD * (math.cos(I1) + math.cos(I2)) / 2
        
        # Update coordinates
        new_northing = northing_list[-1] + delta_Northing
        new_easting = easting_list[-1] + delta_Easting
        new_tvd = tvd_list[-1] + delta_TVD
        
        # Append results to lists
        northing_list.append(new_northing)
        easting_list.append(new_easting)
        tvd_list.append(new_tvd)

    return easting_list, northing_list, tvd_list
