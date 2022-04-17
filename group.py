from expense_book import ExpenseBook
from user import User


class Group:
    def __init__(self):
        self.members: list[User] = []
        self.expense_book = ExpenseBook()

    def get_members(self):
        return self.members

    def add_member(self, user: User):
        self.members.append(user)
        return self

    def add_members(self, users: list[User]):
        self.members.extend(users)
        return self
