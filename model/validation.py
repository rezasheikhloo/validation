import re


class Validation:
    @classmethod
    def name_validator(self,name):
        if re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError("Invalid Name")

    @classmethod
    def family_validator(self, family):
        if re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            raise ValueError("Invalid Family")






