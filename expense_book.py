from transaction import Transaction
from user import User


class ExpenseBook:
    """Contains the list of transactions for a group of users"""

    def __init__(self):
        self.transactions: list[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        return self

    def add_transactions(self, transactions: list[Transaction]):
        self.transactions.extend(transactions)
        return self

    def tally_transactions_for(self, users: list[User]) -> dict[int, int]:
        """return a dictionary mapping from user address to amount"""
        tally = {}
        for user in users:
            tally[user.address] = self.get_credit_of(user)

        return tally

    def get_credit_of(self, user: User):
        total_credit: int = 0
        for transaction in self.transactions:
            if transaction.from_address == user.address:
                total_credit += transaction.amount
            if transaction.to_address == user.address:
                total_credit -= transaction.amount
        return total_credit

    def settle_balance(self, users: list[User]) -> list[Transaction]:
        """Return a list of transactions to settle the balances"""
        transactions = []
        tally = self.tally_transactions_for(users)

        if (min_credit := min(tally.values())) > 0:
            # subtract because no need to settle the min amount
            tally = {k: v - min_credit for k, v in tally.items()}

        print(tally)

        total_spending_per_user = sum(tally.values()) / len(users)

        while total_spending_per_user != 0 or min_credit < 0:
            # settling logic here
            queue = sorted(tally, key=lambda x: tally[x], reverse=True)
            highest_spender = queue.pop(0)
            highest_payee = queue.pop()
            diff_spender = tally[highest_spender] - total_spending_per_user
            diff_payee = total_spending_per_user - tally[highest_payee]

            amount_to_transfer = min(diff_payee, diff_spender)
            if amount_to_transfer < 1:
                # no point tranfering less than 1 wei
                break
            transactions.append(
                Transaction(
                    amount_to_transfer,
                    from_address=highest_payee,
                    to_address=highest_spender,
                )
            )
            print(f"{highest_payee} pays {amount_to_transfer} to {highest_spender}")
            tally[highest_payee] += amount_to_transfer
            tally[highest_spender] -= amount_to_transfer
            if (min_credit := min(tally.values())) > 0:
                # subtract because no need to settle the min amount
                tally = {k: v - min_credit for k, v in tally.items()}
                print(tally)

            total_spending_per_user = sum(tally.values()) / len(users)

        return transactions
