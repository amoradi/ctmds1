from datetime import datetime, timedelta

import numpy as np


def generate_times(hours, half_hour_intervals=False):
    """
    Generate an array of times in HHMM format, starting at 0000.

    Args:
        hours (int): Number of hours to generate
        half_hour_intervals (bool): If True, generate times in 30-minute intervals
                                   If False, generate only hourly times

    Returns:
        np.ndarray: Array of times in HHMM format as strings
    """
    base_time = datetime.strptime("00:00", "%H:%M")
    times = []

    # Calculate number of increments
    increments = hours * (2 if half_hour_intervals else 1)
    increment_minutes = 30 if half_hour_intervals else 60

    for i in range(increments):
        current_time = base_time + timedelta(minutes=i * increment_minutes)
        time_str = current_time.strftime("%H%M")
        times.append(time_str)

    return np.array(times)
