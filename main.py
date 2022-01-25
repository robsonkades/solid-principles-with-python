from dtos import CreateUserInput, CreateUserOutput
from user_service import CreateUserService
from notification_service import EmailNotificationService
from notification_service import NotificationService
from user_repository import UserRepositoy
from user_repository import UserRepositoryInMemory, UserRepositoryInSql

user_repository_impl: UserRepositoy = UserRepositoryInSql() 
notification_service: NotificationService = EmailNotificationService()
create_user_service: CreateUserService = CreateUserService(repository=user_repository_impl, notification=notification_service)

user_input = CreateUserInput(first_name="John", last_name="Doe", age=18)
user_output: CreateUserOutput = create_user_service.execute(input=user_input)
