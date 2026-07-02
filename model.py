def optimize_hvac(occupancy: int, outdoor_temp: float, outdoor_humidity: float) -> dict:
    """
    Calculates the optimal HVAC setpoint and AC mode for a gym environment.
    
    Args:
        occupancy: Number of people in the gym.
        outdoor_temp: Outdoor temperature in Celsius.
        outdoor_humidity: Outdoor relative humidity percentage.
        
    Returns:
        dict: Containing 'setpoint' (float) and 'mode' (str).
    """
    base_setpoint = 22.0
    
    # --- Mode Selection ---
    if outdoor_humidity > 70.0:
        mode = "Dry"
    elif outdoor_temp < 22.0 and occupancy < 10:
        mode = "Fan"
    elif outdoor_temp >= 22.0 and outdoor_humidity <= 70.0:
        mode = "Cool"
    else:
        mode = "Auto"
        
    # --- Setpoint Adjustment ---
    setpoint = base_setpoint
    
    # Adjust for occupancy (body heat)
    if occupancy > 30:
        setpoint -= 2.0
    elif 10 <= occupancy <= 30:
        setpoint -= 1.0
        
    # Adjust for cold weather
    if outdoor_temp < 15.0:
        setpoint += 1.0
        
    return {
        "setpoint": round(setpoint, 1),
        "mode": mode
    }
