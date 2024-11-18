from customers import Customer
from operators import Operator
from bills import Bill


def main():
    # ініціалізація операторів
    operators = [Operator(0, 0.6, 0.1, 0.1, 10), Operator(1, 0.6, 0.2, 0.25, 5)]

    bills = [Bill(1000), Bill(500)]

    customers = [Customer(0, 'Петро', 'Демчишин', 21, operators, bills),
                 Customer(1, 'Максим', 'Леськів', 18, operators, bills)]

    #виклик дій для клієнтів
    customers[0].talk(7, customers[1], 0)  #Петро говорить з Максимом
    customers[1].message(21, customers[0], 1)  # Максим відправляє повідомлення Петру
    customers[0].connection(163, 0)    #Петро використовує інтернет

   # оплата рахунку
    customers[0].get_bill(0).pay(20)

    # зміна ліміту рахунку
    customers[0].get_bill(0).change_limit(10)


if __name__ == "__main__":
    main()   #щоб запускався як головна програма


