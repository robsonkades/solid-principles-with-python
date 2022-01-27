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
      print(f"-------Enviando notificação-------")
      print(f"assunto: {payload.title}")
      print(f"para: {payload.email}")
      print(f"mensagem: {payload.message}")
      print(f"----------------------------------")
      id=uuid.uuid4()
      print(f"Enviado notificação id:{id}")
      print(f"----------------------------------")
      return CreateNotificationOutput(id=id)

class SMSNotificationService(NotificationService):
  def __init__(self) -> None:
      super().__init__()

  def execute(self, payload: CreateNotificationInput) -> CreateNotificationOutput:
      print(f"-------Enviando notificação-------")
      print(f"assunto: {payload.title}")
      print(f"para: {payload.phone}")
      print(f"mensagem: {payload.message}")
      print(f"----------------------------------")
      id=uuid.uuid4()
      print(f"Enviado notificação id:{id}")
      print(f"----------------------------------")
      return CreateNotificationOutput(id=id)