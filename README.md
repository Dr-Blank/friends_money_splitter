# Friends Money Splitter

Use for settling accounts among users for shared expenses.

## Usage

Run `main.py` for example.

1. Create `users` with unique account addresses and balances. Ignore `roles` for now, they are meant to be used when translating to solidity.****
   - `roles` will be used to check if the user can add or remove transactions
    ```py
    user1 = User(1, Role.MANAGER, 1000)
    user2 = User(2, Role.MEMBER, 300)
    user3 = User(3, Role.MEMBER, 0)
    shopkeeper = User(666, Role.MEMBER, 0)
    casino = User(777, Role.MEMBER, 10000000)
    ```
2. Create a `group` and add members to it who will be considered for splitting expenses
    ```py
    school_group = Group()
    school_group.add_members([user1, user2, user3])
    ```
3. add `transactions` to the group's `expense book`
    ```py
    school_group.expense_book.add_transactions(
        [
            Transaction(1000, user1.address, shopkeeper.address),
            Transaction(1000, casino.address, user2.address),
            Transaction(1000, user2.address),
            Transaction(1000, user2.address, user1.address),
        ]
    )
    ```
4. call the settle_balance method on the group's expense book to get the transactions to perform to settle the balance
   ```py
    school_group.expense_book.settle_balance(school_group.members)
   ```

we can further add the new transactions to the group's expense book to see if tally is 0 for all.

### Notes

* Transactions below 1 wie are not allowed as 
  + they cause infinite loop
  + they are insignificant
