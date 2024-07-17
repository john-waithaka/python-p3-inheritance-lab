#!/usr/bin/env python

# from user import User

# import random

# class Teacher(User):

#     def teach(self):
#         pass


from user import User

import random

class Teacher(User):

    def __init__(self, first_name:str, last_name:str):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]


#  #improved code 

# from user import User

#  import random

# class Teacher(User):
#     def __init__(self, first_name: str, last_name: str):
#         super().__init__(first_name, last_name)
#         self.knowledge = [
#             "str is a data type in Python",
#             "programming is hard, but it's worth it",
#             "JavaScript async web request",
#             "Python function call definition",
#             "object-oriented teacher instance",
#             "programming computers hacking learning terminal",
#             "pipenv install pipenv shell",
#             "pytest -x flag to fail fast",
#         ]

#     def teach(self) -> str:
#         return random.choice(self.knowledge)

# Create a Teacher instance
teacher = Teacher("John", "Doe")

# Accessing attributes
print(f"Teacher: {teacher.first_name} {teacher.last_name}")

# Calling methods
print(f"Teaching: {teacher.teach()}")
       