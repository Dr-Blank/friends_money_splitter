from dataclasses import dataclass, field

from role import Role


@dataclass
class User:
    address: int
    role: Role
    balance: int
    name: str = field(init=False, default=None, kw_only=True)
