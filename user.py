import uuid

class User:
  def __init__(self, first_name: str, last_name: str, user_type: str):
      self.__first_name = first_name
      self.__last_name = last_name
      self.__id = str(uuid.uuid4())
      self.__user_type = user_type
  
  def get_id(self) -> str:
    return self.__id

  def get_first_name(self) -> str:
    return self.__first_name

  def get_last_name(self) -> str:
    return self.__last_name

  def set_id(self, id: str) -> None:
    self.__id = id

  def set_first_name(self, first_name: str) -> None:
    self.__first_name = first_name

  def set_last_name(self, last_name: str) -> None:
    self.__last_name = last_name

  def get_user_type(self) ->  str:
    return self.__user_type
  
  def set_user_type(self, user_type: str) ->  None:
    self.__user_type = user_type