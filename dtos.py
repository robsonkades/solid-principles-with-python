from uuid import UUID

class CreateUserInput:
  def __init__(self, first_name: str, last_name: str, age: int) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


class CreateUserOutput:
  def __init__(self, first_name: str, last_name: str) -> None:
    self.first_name = first_name
    self.last_name = last_name


class CreateNotificationInput:
  def __init__(self, title: str, message: str, email: str = '', phone: str = '') -> None:
    self.title = title
    self.message= message
    self.email = email
    self.phone = phone


class CreateNotificationOutput:
  def __init__(self, id: UUID) -> None:
    self.id = id
