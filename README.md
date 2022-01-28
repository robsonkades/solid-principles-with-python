# Aplicando os princípios de solid em uma aplicação real com python.

## Introdução

SOLID é uma sigla para os primeiros cinco princípios do design orientado a objeto (OOD) criada por Robert C. Martin.

Esses princípios estabelecem algumas práticas que contribuem para o desenvolvimento de software. Adotar essas práticas também pode contribuir para evitar problemas de código, refatoração de código, desenvolvimento ágil e adaptativo de software.

SOLID significa:

- **S** - Single-responsibility Principle (Princípio da responsabilidade única)
- **O** - Open-closed Principle (Princípio do aberto-fechado)
- **L** - Liskov Substitution Principle (Princípio da substituição de Liskov)
- **I** - Interface Segregation Principle (Princípio da segregação de interfaces)
- **D** - Dependency Inversion Principle (Princípio da inversão de dependência)

## Princípio da responsabilidade única

Uma classe deve ter um e apenas um motivo para mudar, o que significa que uma classe deve ter apenas um objetivo.

Alguns benefícios que esse princípio pode nos ajudar:

- **Menor acoplamento** – Menos funcionalidades em uma única classe terá menos dependências.
- **Organização** – Classes menores e bem organizadas são mais fáceis de dar manutenção e evoluir.
- **Teste** – Uma classe com uma responsabilidade terá muito menos casos de teste.

Vejamos um exemplo:

```py
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
```

Um exemplo bem simple, basicamente a classe `CreateUserService` tem apenas uma função que é Criar um usuário.
Observe que essa classe esta salvando um usuário em um repositório, porém a nossa classe não sabe qual é o tipo desse repositório, pode ser um banco de dados sql, nosql ou talvez um arquivo, ou seja, não é de responsabilidade da classe conhecer como o usuário e salvo.

## Princípio do aberto-fechado

Os objetos ou entidades devem estar abertos para extensão, mas fechados para modificação.

Ao fazer isso, nos impedimos de modificar o código existente e causar novos bugs, mas ainda assim podemos extender e customizar nossas regras. A única exceção à regra é ao corrigir bugs no código existente.

Vejamos um exemplo:

```py
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
```

```py
class CreateDevUserService(CreateUserService):

  def __init__(self, repository: UserRepositoy, notification: NotificationService) -> None:
      self.__notification = notification
      super().__init__(repository)

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    if input.age < 16:
      raise UserException(message="Usuário menor de idade não pode criar uma conta.")
    create_user_output = super().execute(input=input)

    email = "robsonkades@outlook.com"
    phone = "4999999999"

    payload = CreateNotificationInput(
        title="[Dev] - Conta criada",
        message="Nova conta foi criada",
        email=email,
        phone=phone)

    self.__notification.execute(payload=payload)

    return create_user_output
```

Veja que a classe `CreateUserService` é utilizada para criar um usuário, agora observe
a classe `CreateDevUserService`, essa classe é uma classe do tipo `CreateUserService`, porém
fizemos algumas modificações, criamos algumas regras de negócio para criar um usuário do tipo desenvolvedor, que a idade tem que ser maior que 15
anos e também enviamos uma notificação quando o usuário for criado, veja que passamos para a nossa super classe criar o usuário `super().execute(input=input)`.

Estão conseguimos extender a criação de usuários, criamos algumas regras na nossa classe que foi extendida e não foi necessário modificar a classe pai.

## Princípio da substituição de Liskov

Simplificando, se a classe A for um subtipo da classe B , devemos ser capazes de substituir B por A sem interromper o comportamento do nosso programa.

Simplificando, as classes derivadas devem poder ser substituíveis por suas classes base.

Vamos para o exemplo:

Nossa classe abstrata

```py
class NotificationService(Singleton, abc.ABC):
  @abc.abstractmethod
  def execute(payload: CreateNotificationInput) -> CreateNotificationOutput:
    pass
```

Classe que envia notificações por email

```py
class EmailNotificationService(NotificationService):
  def __init__(self) -> None:
      super().__init__()

  def execute(self, payload: CreateNotificationInput) -> CreateNotificationOutput:
    ...
```

Classe que envia notificações por Sms

```py
class SMSNotificationService(NotificationService):
  def __init__(self) -> None:
      super().__init__()

  def execute(self, payload: CreateNotificationInput) -> CreateNotificationOutput:
    ...
```

```py
notification_service: NotificationService = EmailNotificationService()
payload = CreateNotificationInput(
        title="[Dev] - Conta criada",
        message="Nova conta foi criada",
        email=email,
        phone=phone)
notification_service.execute(payload=payload)
```

Observe que quando estamos instanciando a nossa classe `EmailNotificationService` estamos substituindo ela por a nossa classe base que é `NotificationService`.

## Princípio da segregação de interfaces

Interfaces específicas são melhores que interfaces de propósito geral, ou seja, não podemos obrigar os nossos clientes a implementar interfaces com métodos que não serão utilizados.

Ao fazer isso, podemos garantir que as classes de implementação só precisem se preocupar com os métodos que são de seu interesse.

Veja um exemplo:

```py
class UserRepositoy(Singleton, abc.ABC):
  @abc.abstractmethod
  def save(user: User) -> User:
    pass

  @abc.abstractmethod
  def get(id: str) -> User:
    pass
```

Implementação do repositório em memória

```py
class UserRepositoryInMemory(UserRepositoy):
  users: list[User] = []

  def __init__(self) -> None:
      super().__init__()

  def save(self, user: User) -> User:
      self.users.append(user)
      return user
```

Em nosso exemplo criamos uma classe `UserRepositoy` com duas funções `get` e `save`, agora vejamos a implementação que criamos na classe `UserRepositoryInMemory`. Observe que na nossa implementação somente criamos o a função de `save`, a função `get` por uma regra nossa não faz sentido ser implementada nesse momento.

Se executar o nosso código teremos um problema, por que não foi implementado a função `get`, com isso temos uma quebra do princípio, por que somos obrigados a implementar a função.

E como resolvemos isso?

Podemos criar interfaces especificas com a função `save` e outra com `get`, em nossa classe que implementamos somente utilizamos interfaces que fazem sentido no nosso código.

## Princípio da inversão de dependência

As entidades devem depender de abstrações e não de implementações, um módulo de alto nivel não deve depender de um módulo de baixo nivel mas ambos devem depender de abstrações.

Vejamos um exemplo:

Classe base do repositório

```py
class UserRepositoy(Singleton, abc.ABC):
  @abc.abstractmethod
  def save(user: User) -> User:
    pass
```

Implementação do repositório em memória

```py
class UserRepositoryInMemory(UserRepositoy):
  users: list[User] = []

  def __init__(self) -> None:
      super().__init__()

  def save(self, user: User) -> User:
      self.users.append(user)
      return user
```

Implementação do repositório em banco de dados sql

```py
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
```

Controller de usuários

```py
class UserControllerImpl:
  def __init__(self, user_repository: UserRepositoy, notification: NotificationService) -> None:
      self.__user_repository = user_repository
      self.__notification = notification
```

Executando nossa aplicação

```py
user_repository_impl: UserRepositoy = UserRepositoryInMemory()
notification_service: NotificationService = EmailNotificationService()

user_controller = UserControllerImpl(user_repository=user_repository_impl, notification=notification_service)
```

Veja que criamos uma classe base `UserRepositoy`e também criamos duas implementações especificadas que são `UserRepositoryInSql` e `UserRepositoryInMemory` ambas são do tipo `UserRepositoy`.

O nosso `UserControllerImpl` depende da nossa abstração e não de uma classe implementada, isso signfica que quando for instâncias a nossa classe podemos passar para o nosso `UserControllerImpl` qual implementação queremos.
