from group import Group
from role import Role
from transaction import Transaction
from user import User


def main():
    user1 = User(1, Role.MANAGER, 1000)
    user2 = User(2, Role.MEMBER, 300)
    user3 = User(3, Role.MEMBER, 0)
    shopkeeper = User(666, Role.MEMBER, 0)
    casino = User(777, Role.MEMBER, 10000000)
    school_group = Group()
    school_group.add_members([user1, user2, user3])
    school_group.expense_book.add_transactions(
        [
            Transaction(1000, user1.address, shopkeeper.address),
            Transaction(1000, casino.address, user2.address),
            Transaction(1000, user2.address),
            Transaction(1000, user2.address, user1.address),
        ]
    )
    settlements = school_group.expense_book.settle_balance(school_group.members)
    
    school_group.expense_book.add_transactions(settlements)

    print(school_group.expense_book.tally_transactions_for(school_group.members))

if __name__ == "__main__":
    main()
