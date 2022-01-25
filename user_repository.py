import abc

from user import User


class UserRepositoy(abc.ABC):


  @abc.abstractmethod
  def save(user: User) -> User:
    pass

  @abc.abstractmethod
  def get(id: str) -> User:
    pass

  @abc.abstractmethod
  def delete(user: User) -> None:
    pass

  @abc.abstractmethod
  def index() -> list[User]:
    pass