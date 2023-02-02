def make_car(manufactor, model, **options):
    """Make a dictionary representing a car"""

    car_dict = {
            'manufactor': manufactor.title(),
            'model': model.title(),
            }
    for option, value in options.items():
        car_dict[option] = value


    return car_dict

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
