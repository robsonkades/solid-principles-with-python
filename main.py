from controller import UserController
from dtos import CreateUserInput, UserType
from notification_service import EmailNotificationService
from notification_service import NotificationService
from user_repository import UserRepositoy
from user_repository import UserRepositoryInMemory, UserRepositoryInSql

user_repository_impl: UserRepositoy = UserRepositoryInMemory() 
notification_service: NotificationService = EmailNotificationService()
user_controller = UserController(user_repository=user_repository_impl, notification=notification_service)

user_input = CreateUserInput(first_name="James", last_name="Gosling", age=66, user_type= UserType.DEV)
user_controller.create(input=user_input)

user_input = CreateUserInput(first_name="Uncle", last_name="Bob", age=70, user_type= UserType.TECHMANAGER)
user_controller.create(input=user_input)