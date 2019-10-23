from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("John", 100, 2)
taxi.start_fare()
print(taxi.get_fare())
taxi.drive(18)
print(taxi.get_fare())