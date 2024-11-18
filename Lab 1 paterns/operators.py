from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customers import Customer


class Operator:
    #клас operator представляє оператора зв'язку та тарифи на послуги

    def __init__(self, id: int, talking_charge: float, message_cost: float,
                 network_charge: float, discount_rate: int) -> None:
        #конструктор
        self.id = id
        self.talking_charge: float = talking_charge
        self.message_cost: float = message_cost
        self.network_charge: float = network_charge
        self.discount_rate: int = discount_rate

    def calc_talking_cost(self, minutes: float, customer: 'Customer') -> float:
        """
        Calculate the cost of a phone call based on the duration and customer discounts.

        Args:
            minutes (float): The duration of the phone call in minutes.
            customer (Customer): The customer object. Discounts are applied if the
                                 customer is under 18 or over 65 years of age.

        Returns:
            float: The total cost of the phone call after applying any discounts.

        """
        cost = self.talking_charge * minutes
        if customer.age < 18 or customer.age > 65:
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        print(f"Дзвінок {minutes} хвилин коштував {cost}")
        return cost

    def calc_message_cost(self, quantity: int, customer: 'Customer', other: 'Customer') -> float:
         #метод розрахунку вартості повідомлень
        cost = self.message_cost * quantity
        if self.id == other.operators[self.id].id:             # той ж самий оператор
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        print(f"Надсилає {quantity} повідомлень, це коштує {cost}")
        return cost

    def calc_network_cost(self, amount: float) -> float:
        #метод для розрахунку вартості інтернету
        cost = self.network_charge * amount
        print(f"Використані {amount} MB інтернету коштує {cost}")
        return cost


    def get_talking_charge(self) -> float:
        return self.talking_charge

    def set_talking_charge(self, charge: float) -> None:
        self.talking_charge = charge

    def get_message_cost(self) -> float:
        return self.message_cost

    def set_message_cost(self, cost: float) -> None:
        self.message_cost = cost

    def get_network_charge(self) -> float:
        return self.network_charge

    def set_network_charge(self, charge: float) -> None:
        self.network_charge = charge

    def get_discount_rate(self) -> int:
        return self.discount_rate

    def set_discount_rate(self, rate: int) -> None:
        self.discount_rate = rate
