from model.validation import Validation


class User:
    def __init__(self, username, password, name, family, active=True):
        self.username = username
        self.password = password
        self.name = name
        self.family = family
        self.active = active

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family =Validation.family_validator(family)

    @property
    def active(self):
        return bool(self._active)

    @active.setter
    def active(self, active):
        self._active = bool(active)


    def __repr__(self):
        return f"{self.__dict__}"