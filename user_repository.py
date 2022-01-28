import abc
from exception import UserException
from user import User
import sqlite3

from util import Singleton

class UserRepositoy(Singleton, abc.ABC):
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

class UserRepositoryInMemory(UserRepositoy):

  users: list[User] = []

  def __init__(self) -> None:
      super().__init__()

  def save(self, user: User) -> User:
      self.users.append(user)
      return user

  def get(self, id: str) -> User:
    response = [d for d in self.users if d.get_id() == id]
    if len(response) > 0:
      return response[0]
    raise UserException(message="User with id {id} not found")

  def delete(self, user: User) -> None:
      self.users.remove(user)

  def index(self) -> list[User]:
      return self.users

class UserRepositoryInSql(UserRepositoy):

  myDatabase = "database.db"

  def __init__(self) -> None:
      self.__connect = sqlite3.connect(self.myDatabase)
      super().__init__()

  def save(self, user: User) -> User:
      cursor = self.__connect.cursor()
      query = [user.get_id(), user.get_first_name(), user.get_last_name(), user.get_user_type()]
      cursor.execute('CREATE TABLE IF NOT EXISTS users (id text, first_name text, last_name text, user_type text)')
      cursor.execute("insert into users(id, first_name, last_name, user_type) values (?, ?, ?, ?)", query)
      self.__connect.commit()
      cursor.close()
      return user

  def get(self, id: str) -> User:
    cursor = self.__connect.cursor()
    query = [id]
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id text, first_name text, last_name text, user_type text)')
    cursor.execute("select * from users where id=?", query)
    row = cursor.fetchone()
    if row == None:
      raise UserException(message="User with id {id} not found")

    id = row[0]
    first_name = row[1]
    last_name = row[2]
    user_type = row[3]

    user = User(first_name=first_name, last_name=last_name, user_type=user_type)
    user.set_id(id)
    cursor.close()
    return user

  def delete(self, user: User) -> None:
    cursor = self.__connect.cursor()
    query = [user.get_id()]
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id text, first_name text, last_name text, user_type text)')
    cursor.execute("delete from users where id=?", query)
    cursor.close()
    self.__connect.commit()

  def index(self) -> list[User]:
    cursor = self.__connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id text, first_name text, last_name text, user_type text)')
    cursor.execute("select * from users")
    rows = cursor.fetchall()
    users: list[User] = []

    for row in rows:
      id = row[0]
      first_name = row[1]
      last_name = row[2]
      user_type = row[3]

      user = User(first_name=first_name, last_name=last_name, user_type=user_type)
      user.set_id(id)
      users.append(user)
    cursor.close()
    return users