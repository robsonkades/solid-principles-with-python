from Car import MyCar, CarBase, YourCar
from ManufactureCar import ManufactureCar

mustang: CarBase = MyCar("Mustang", 2022, "Turbo")
gol: CarBase = YourCar("Gol", 2011, "Trend")

typeMyCarClass = type(mustang)
typeYourCarClass = type(gol)

privateVariable = gol.to_uppercase("Carro")

print(privateVariable)


print(f"typeMyCarClass instancia de MyCar is: {isinstance(mustang, MyCar)}")
print(f"typeYourCarClass instancia de YourCar is: {isinstance(gol, YourCar)}")

print(typeMyCarClass)
print(typeYourCarClass)

ford = ManufactureCar(mustang)

print(ford.get_current_car())
print(ford.get_type())

