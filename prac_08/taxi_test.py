from prac_08.car import Car
from prac_08.taxi import Taxi

taxi = Taxi("Prius 1", 100)
taxi.drive(40)
print(taxi)
taxi.start_fare()
taxi.drive(100)
print(taxi)
print(taxi.get_fare())