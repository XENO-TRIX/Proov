# fleet_utils.py
# Sammelbecken fuer Helfer seit 2013. Dead code removed 2024. Modernized 2024.
# (Catch-all helpers since 2013. Dead code removed; modernized 2024.)

MILES_PER_KM = 0.621371                 # 1 km = 0.621371 miles


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"
