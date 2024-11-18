class Bill:
    """
    Represents a customer's bill for services.

    Attributes:
        limiting_amount (float): The maximum allowable debt limit.
        current_debt (float): The current debt on the bill.
    """

    def __init__(self, limiting_amount: float):
        """
        Initializes a Bill object with a specified debt limit.

        Args:
            limiting_amount (float): The maximum allowable debt limit.
        """
        self.limiting_amount: float = limiting_amount
        self.current_debt: float = 0.0

    def check(self) -> bool:
        """
        Checks whether the debt limit has been exceeded.

        Returns:
            bool: True if the current debt is greater than or equal to the limiting amount, False otherwise.
        """
        return self.current_debt >= self.limiting_amount

    def add_debt(self, debt: float) -> None:
        """
        Adds debt to the current bill. Prints a warning if the limit is exceeded.

        Args:
            debt (float): The amount of debt to be added.
        """
        tentative_debt = debt + self.current_debt
        if tentative_debt <= self.limiting_amount:
            self.current_debt += debt
        else:
            print(f"Ви перевищили ліміт! Ваш борг становитиме {tentative_debt}")

    def pay(self, amount: float) -> None:
        """
        Processes a payment on the bill. If the payment exceeds the current debt,
        the extra amount is used to increase the debt limit.

        Args:
            amount (float): The amount being paid.
        """
        self.current_debt -= amount
        if self.current_debt < 0:
            self.limiting_amount += abs(self.current_debt)
            self.current_debt = 0
        print(f"Оплачено {amount}. Борг: {self.current_debt}")

    def change_limit(self, amount: float) -> None:
        """
        Changes the debt limit by the specified amount.

        Args:
            amount (float): The amount to change the debt limit by.
        """
        self.limiting_amount += amount
        print(f"Ліміт змінено. Новий ліміт: {self.limiting_amount}")

    def get_limiting_amount(self) -> float:
        """
        Retrieves the current debt limit.

        Returns:
            float: The maximum allowable debt limit.
        """
        return self.limiting_amount

    def get_current_debt(self) -> float:
        """
        Retrieves the current debt on the bill.

        Returns:
            float: The current debt.
        """
        return self.current_debt
