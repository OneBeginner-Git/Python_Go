# from car import Car, Battery, ElectricCar
import car

my_fuelCar = car.Car('jaguar', 'XEL', 2023)
my_eCar = car.ElectricCar('ford', 'mach-e', 2024)
print(my_fuelCar.get_descriptive_name())
print(my_eCar.get_descriptive_name())
