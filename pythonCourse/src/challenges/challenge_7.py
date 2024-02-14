"""The module for the 7th challenge"""


class FinanceAccount:
    """
    This class is responsible for manage a FinanceAccount
    """

    def __init__(self, account_holder: str, balance: float):
        self._account_holder = account_holder
        self._balance = balance

    def __str__(self):
        return (
            f"The holder of this account is {self._account_holder}"
            + f" and currently have R$ {self.balance:.2f} available "
        )

    @property
    def balance(self):
        """getter for balance"""
        return self._balance

    def transference(self, transference_type: str, amount: float):
        """method used to realize a transference"""
        if amount <= 0:
            raise ValueError("The amount must be greater than zero")
        if transference_type == "incoming":
            self._balance += amount
        elif transference_type == "debit":
            self._balance -= amount
        else:
            raise ValueError("transference_type invalid!")
        print(f"{transference_type} has been successfully done.")


class RikBankCustomer:
    """
    This class is responsible for Customers of Rik Bank
    """

    __total_balance = 0

    def __init__(
        self,
        name: str,
        password: str,
        account_type: str,
        address: str,
    ):
        self.name = name
        self.password = password
        self.account_type = account_type
        self.address = address
        self.finance_account = FinanceAccount(account_holder=name, balance=0)

    @classmethod
    def register_account(cls, finance_account: FinanceAccount):
        """register account in the managed accounts"""
        cls.__total_balance += finance_account.balance

    @classmethod
    def get_total_amount(cls):
        """gets the total amount in the managed accounts"""
        print(f"R$ {cls.__total_balance:.2f}")


def challenge_7():
    """The challenge 7 code"""
    rik_account = FinanceAccount(account_holder="rik", balance=250.00)
    tim_account = FinanceAccount(account_holder="tim", balance=100.00)
    rik_bank = RikBankCustomer(
        account_type="plus", address="BH", name="rik", password="123"
    )
    rik_bank.register_account(finance_account=rik_account)
    rik_bank.get_total_amount()
    print(f"{rik_account}\n{tim_account}")
    try:
        rik_account.transference(amount=200.00, transference_type="incoming")
    except ValueError as exception:
        print(exception)
    print(f"{rik_account}\n{tim_account}")
