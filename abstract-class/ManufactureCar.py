from Car import CarBase

class ManufactureCar:
  def __init__(self, car: CarBase):
      self.car = car

  def get_current_car(self):
    model = self.car.get_model()
    name = self.car.get_name()
    year = self.car.get_year()
    return f"name:{name} - model:{model} - year:{year}"

  def get_type(self):
    return self.car.__class__
    
