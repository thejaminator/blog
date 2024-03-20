# class User:
#     def __init__(self, name: str, emails: list[str] = []) -> None:
#         self.name = name
#         self.emails = emails

#     def add_email(self, email: str) -> None:
#         self.emails.append(email)

# james = User(name="James")
# james.add_email("james@gmail.com")
# john = User(name="John")
# # John will have the emails ['james@gmail.com'], even though we never added that email to John's list.
# print(john.emails)

# from typing import Sequence

# class User:
#     def __init__(self, name: str, emails: Sequence[str] = []) -> None:
#         self.name = name
#         self.emails: list[str] = list(emails)

#     def add_email(self, email: str) -> None:
#         self.emails.append(email)


# from dataclasses import dataclass

# @dataclass
# class UserDataclass:
#     emails: list[str] = []

# from pydantic import BaseModel

# class UserPydantic(BaseModel):
#     name: str
#     emails: list[str] = []

#     def add_email(self, email: str) -> None:
#         self.emails.append(email)

# james = UserPydantic(name="James")
# james.add_email("james@gmail.com")
# print(james.emails)
# john = UserPydantic(name="John")
# print(john.emails) # [] instead of ['james@gmail.com'] that we got with the User class. So no bugs here