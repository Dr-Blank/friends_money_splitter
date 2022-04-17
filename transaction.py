from dataclasses import dataclass, field

from user import User


@dataclass
class Transaction:
    amount: int
    from_address: User
    to_address: int = None
    description: str = field(init=False, default=None, kw_only=True)
