from controller.exceptions import UserNotFoundException
from model.user import User
from model.user_da import UserDa


class UserController:
    user_da = UserDa()

    @classmethod
    def save(cls, username, password, name, family, active=True):
        try:
            user = User(username, password, name, family, active)
            cls.user_da.save(user)
            return True, f"User {username} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, username, password, name, family, active=True):
        try:
            user = User(username, password, name, family, active)
            cls.user_da.edit(user)
            return True, f"User {username} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, username):
        try:
            cls.user_da.remove(username)
            return True, f"User {username} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.user_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, cls.user_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            user = cls.user_da.find_by_username_and_password(username, password)
            if user:
                return True, user
            else:
                raise UserNotFoundException("User not found !!!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def enable_user(cls, username):
        try:
            cls.user_da.enable_user(username)
            return True, f"User {username} Enabled"
        except Exception as e:
            return False, str(e)

    @classmethod
    def disable_user(cls, username):
        try:
            cls.user_da.disable_user(username)
            return True, f"User {username} Disabled"
        except Exception as e:
            return False, str(e)
