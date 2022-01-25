from dtos import CreateUserInput, CreateUserOutput, CreateNotificationInput
from notification_service import NotificationService
from user_repository import UserRepositoy
from user import User

class CreateUserService:
  def __init__(self, repository: UserRepositoy, notification: NotificationService) -> None:
      self.__repository = repository
      self.__notification = notification

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    if input.age < 18:
      raise Exception("Usuário menor de idade não pode criar uma conta.")


    self.__repository.get(id="09fd79b6-eb28-4fd2-a33e-1817e176cf67")

    print('......criando usuário........') 
    user: User = self.__repository.save(User(first_name=input.first_name, last_name=input.last_name))

    print(f'......usuário criado:{user.get_first_name()}........')
    email_fake = "johndoe@example.com"
    phone_fake = "4999999999"

    payload = CreateNotificationInput(
        title="Conta criada",
        message="Sua conta criada",
        email=email_fake,
        phone=phone_fake)

    self.__notification.execute(payload=payload)

    return CreateUserOutput(first_name=user.get_first_name(), last_name=user.get_last_name())
