import abc
from ast import Raise

class CarBase(abc.ABC):
  @abc.abstractmethod
  def get_model() -> str:
    pass

  @abc.abstractmethod
  def get_year() -> str:
    pass

  @abc.abstractmethod
  def get_name() -> str:
    pass


class MyCar(CarBase):
  def __init__(self, name: str, year: int, model: str):
    self.name = name
    self.year = year
    self.model = model

  def get_model(self) -> str:
    return self.model

  def get_year(self) -> str:
    return self.year

  def get_name(self) -> str:
    return self.name


class YourCar(CarBase):
  def __init__(self, name: str, year: int, model: str):
    self.name = name
    self.year = year
    self.model = model

  def get_year(self) -> str:
    return self.year

  def __to_string(self, val: str) -> str:
    return val.join([f"{self.name}-{self.model}-{self.year}"])

  def to_uppercase(self, val: str) -> str:
    return self.__to_string(val).upper()

  def get_name(self) -> str:
    return self.name

  def get_model(self) -> str:
    return self.model
