from uuid import UUID

from user_repository import UserRepositoy
from user import User


class UserRepositoryImpl(UserRepositoy):

  users: list[User] = []

  def __init__(self) -> None:
      super().__init__()

  def save(self, user: User) -> User:
      self.users.append(user)
      return user

  def get(self, id: UUID) -> User:
    response = [d for d in self.users if d.get_id() == id]
    if len(response) > 0:
      return response[0]
    raise Exception("User with id {id} not found")

  def delete(self, user: User) -> None:
      self.users.remove(user)

  def index(self) -> list[User]:
      return self.users



  
