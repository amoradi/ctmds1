from datetime import datetime, timedelta

import pytz


def is_dst_transition_day(date_str, country_code, region=None):
    """
    Check if a given date is a DST transition day (short 23-hour day or long 25-hour day).

    Args:
        date_str (str): Date in YYYY-MM-DD format
        country_code (str): Country code (e.g., 'US', 'GB')
        region (str, optional): Region within the country

    Returns:
        str: 'short' if it's a 23-hour day, 'long' if it's a 25-hour day, None otherwise
    """
    # Parse the date string
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Get timezone
    if region:
        try:
            timezone_str = f"{country_code}/{region}"
            timezone = pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            timezone_str = f"{region}/{country_code}"
            try:
                timezone = pytz.timezone(timezone_str)
            except pytz.exceptions.UnknownTimeZoneError:
                raise ValueError(
                    f"Invalid region: {region} for country: {country_code}"
                )
    else:
        try:
            timezone_str = pytz.country_timezones[country_code][0]
            timezone = pytz.timezone(timezone_str)
        except KeyError:
            raise ValueError(f"Invalid country code: {country_code}")

    # Create datetime objects for the beginning and end of the day
    start_of_day = timezone.localize(date.replace(hour=0, minute=0), is_dst=None)
    end_of_day = timezone.localize(
        (date + timedelta(days=1)).replace(hour=0, minute=0), is_dst=None
    )

    # Get DST information before and after the date
    day_before = timezone.localize(
        (date - timedelta(days=1)).replace(hour=12), is_dst=None
    )
    day_of = timezone.localize(date.replace(hour=12), is_dst=None)
    day_after = timezone.localize(
        (date + timedelta(days=1)).replace(hour=12), is_dst=None
    )

    # Check for DST transitions
    dst_before = day_before.dst().total_seconds() > 0
    dst_of = day_of.dst().total_seconds() > 0
    dst_after = day_after.dst().total_seconds() > 0

    # If there's a transition on this day
    if dst_before != dst_of or dst_of != dst_after:
        # Calculate the length of the day in minutes
        day_length_minutes = (end_of_day - start_of_day).total_seconds() / 60

        # Convert to hours
        day_length_hours = day_length_minutes / 60

        if abs(day_length_hours - 23) < 0.1:
            return "short"
        elif abs(day_length_hours - 25) < 0.1:
            return "long"

    return None
