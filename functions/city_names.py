def city_country(city, country):
    
    names = f"{city}, {country}."
    return names.title()

city = city_country('Tirana', 'Albania')
print(city)

city = city_country('Paris', 'France')
print(city)

city = city_country('Milan', 'Italy')
print(city)

