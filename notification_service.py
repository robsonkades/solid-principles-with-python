import abc
import uuid
from dtos import CreateNotificationInput, CreateNotificationOutput

class NotificationService(abc.ABC):
  @abc.abstractmethod
  def execute(payload: CreateNotificationInput) -> CreateNotificationOutput:
    pass

class EmailNotificationService(NotificationService):
  def __init__(self) -> None:
      super().__init__()

  def execute(self, payload: CreateNotificationInput) -> CreateNotificationOutput:
      print(f"Enviando notificação de boas-vindas para email:{payload.email}")
      id=uuid.uuid4()
      print(f"Enviado notificação id:{id}")
      return CreateNotificationOutput(id=id)

class SMSNotificationService(NotificationService):
  def __init__(self) -> None:
      super().__init__()

  def execute(self, payload: CreateNotificationInput) -> CreateNotificationOutput:
      print(f"Enviando notificação de boas-vindas para phone:{payload.phone}")
      id=uuid.uuid4()
      print(f"Enviado notificação id:{id}")