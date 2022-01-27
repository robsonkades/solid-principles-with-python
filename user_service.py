from typing import Type
from dtos import CreateUserInput, CreateUserOutput, CreateNotificationInput, UserType
from exception import UserException
from notification_service import NotificationService
from user_repository import UserRepositoy
from user import User

class CreateUserService:
  def __init__(self, repository: UserRepositoy) -> None:
      self.__repository = repository

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    user: User = self.__repository.save(
      User(
        first_name=input.first_name, 
        last_name=input.last_name, 
        user_type=input.user_type.name))

    print(f"--------Usuário foi criado--------")
    print(f"first_name: {input.first_name}")
    print(f"last_name: {input.last_name}")
    print(f"user_type: {input.user_type.name}")
    print(f"----------------------------------")

    return CreateUserOutput(first_name=user.get_first_name(), last_name=user.get_last_name())

class CreateDevUserService(CreateUserService):

  def __init__(self, repository: UserRepositoy, notification: NotificationService) -> None:
      self.__notification = notification
      super().__init__(repository)

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    if input.age < 16:
      raise UserException(message="Usuário menor de idade não pode criar uma conta.")

    create_user_output = super().execute(input=input)

    email = "devs@example.com"
    phone = "4999999999"


    payload = CreateNotificationInput(
        title="[Dev] - Conta criada",
        message="Nova conta foi criada",
        email=email,
        phone=phone)

    self.__notification.execute(payload=payload)

    return create_user_output

class CreateTechManagerUserService(CreateUserService):

  def __init__(self, repository: UserRepositoy, notification: NotificationService) -> None:
      self.__notification = notification
      super().__init__(repository)

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    if input.age <= 16:
      raise UserException(message="Usuário menor de idade não pode criar uma conta.")

    create_user_output = super().execute(input=input)

    email_fake = "tech-manager@example.com"
    phone_fake = "4999999999"
    payload = CreateNotificationInput(
        title="[TechManager] - Conta criada",
        message="Nova conta foi criada",
        email=email_fake,
        phone=phone_fake)

    self.__notification.execute(payload=payload)

    return create_user_output

class CreateUserBuilderService:
  def execute(self, input: CreateUserInput) -> (Type[CreateDevUserService] or Type[CreateTechManagerUserService] or Type[CreateUserService]):
      if input.user_type == UserType.DEV:
        return CreateDevUserService
      elif input.user_type == UserType.TECHMANAGER:
        return CreateTechManagerUserService
      else:
        return CreateUserService
