from user import User
from user_repository import UserRepositoy
from user_repository_impl import UserRepositoryImpl

user_repository_impl: UserRepositoy = UserRepositoryImpl()

user = User(first_name="Robson", last_name="Kades")
user2 =  user
print(user)
print(user2)

robson_id = user.get_id()
user_repository_impl.save(user)
robson_saved = user_repository_impl.get(id=robson_id)
user_repository_impl.delete(robson_saved)

