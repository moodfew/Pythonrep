import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def hey(self) -> None:
        return super().setUp()
    def test_city_country(self):
        place = city_country('vlora', 'albania')
        self.assertEqual(place, 'Vlora Albania.')
    
    def test_city_country_population(self):
        place = city_country('santiago', 'chille', 5000)
        self.assertEqual('Santiago Chille 5000.', place)

if __name__ == '__main__':
    unittest.main()
