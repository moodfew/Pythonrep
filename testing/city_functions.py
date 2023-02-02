def city_country(city, country, population=None):
    """Cleanly format city and country."""
    if population:
        place = f"{city} {country} {population}."
    else:
        place = f"{city} {country}."

    return place.title()
