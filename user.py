import uuid

class User:
  def __init__(self, first_name: str, last_name: str):
      self.__first_name = first_name
      self.__last_name = last_name
      self.__id = uuid.uuid4()
  
  def get_id(self) -> uuid.UUID:
    return self.__id

  def get_first_name(self) -> str:
    return self.__first_name

  def get_last_name(self) -> str:
    return self.__last_name

  def set_first_name(self, first_name: str) -> None:
    self.__first_name = first_name

  def set_last_name(self, last_name: str) -> None:
    self.__last_name = last_name