from controller.user_controller import UserController
from model.user import User
from model.user_da import UserDa

try:
    user = User("ali", "Ali123", "ali", "alipour111")
    print(user)
except Exception as e:
    print(f"Error In App : {e}")


# ut = ("ali", "ali123", "ali","alipour", 1)
# user = User(ut[0], ut[1], ut[2], ut[3], ut[4])

# user = User(*ut)
# print(user)

# UserController.save("ali", "ali345", "ali", "alipour")
# print(UserController.edit("ali", "1234", "ali", "alipour"))
# print(UserController.find_all())
# print(UserController.find_by_username("ali"))
# print(UserController.disable_user("ali"))


# user_controller = UserController()
# print(user_controller.save("reza", "reza123", "reza", "rezaii"))


# user = User("ali", "ali123", "ali","alipour")
# print(user)
# user_da = UserDa()
# user_da.remove("aaa")
# print(user_da.find_by_username("ali"))
# print(user_da.find_by_username("aaa"))
# print(user_da.find_all())
# print(user_da.find_all_active())
# user_da.save(user)
# user_da.edit(user)
# user_da.disable_user("ali")
# user_da.enable_user("aaa")
