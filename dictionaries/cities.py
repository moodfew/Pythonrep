cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby_mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby_mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby_mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby_mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f" It's population is about {population}.")
    print(f" {mountains} mountains are nearby.")

