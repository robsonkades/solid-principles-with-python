from dtos import CreateUserInput, CreateUserOutput, CreateNotificationInput, UserType
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

    return CreateUserOutput(first_name=user.get_first_name(), last_name=user.get_last_name())

class CreateDevUserService(CreateUserService):

  def __init__(self, repository: UserRepositoy, notification: NotificationService) -> None:
      self.__notification = notification
      super().__init__(repository)

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    print(f'----- Criando um usuário do tipo {input.user_type.name}')
    if input.age < 16:
      raise Exception("Usuário menor de idade não pode criar uma conta.")

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
    print(f'----- Criando um usuário do tipo {input.user_type.name}')
    if input.age <= 30:
      raise Exception("Usuário menor de idade não pode criar uma conta.")

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
  def execute(self, input: CreateUserInput):
      if input.user_type == UserType.DEV:
        return CreateDevUserService
      elif input.user_type == UserType.TECHMANAGER:
        return CreateTechManagerUserService
      else:
        raise Exception("CreateUserService não encontrado para o userType")
