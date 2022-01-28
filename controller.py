import abc
from typing import Type
from dtos import CreateUserInput, CreateUserOutput
from notification_service import NotificationService
from user_repository import UserRepositoy
from user_service import CreateDevUserService, CreateTechManagerUserService, CreateUserBuilderService, CreateUserService

class UserControllerImpl:
  def __init__(self, user_repository: UserRepositoy, notification: NotificationService) -> None:
      self.__user_repository = user_repository
      self.__notification = notification
      self.__create_user_service_builder = CreateUserBuilderService()

  def create(self, input: CreateUserInput) -> CreateUserOutput:
    UserService: (
      Type[CreateDevUserService] or 
      Type[CreateTechManagerUserService] or 
      Type[CreateUserService]) = self.__create_user_service_builder.execute(input=input)

    create_user_service = None
    if UserService == CreateUserService:
      create_user_service = UserService(repository=self.__user_repository)
    else:
      create_user_service = UserService(
        notification=self.__notification,
        repository=self.__user_repository)
      
    return create_user_service.execute(input=input)