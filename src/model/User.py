class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def validate_user(self):
        if self.validate_name() and self.validate_age and self.validate_email:
            return True
        return False

    def validate_name(self):
        if self.name:
            return True
        return False

    def validate_age(self):
        if self.age:
            return True
        return False

    def validate_email(self):
        if self.email:
            return False
        return True
