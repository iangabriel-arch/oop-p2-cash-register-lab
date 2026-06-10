#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last = self.previous_transactions.pop()
            self.total -= last["price"] * last["quantity"]
            for _ in range(last["quantity"]):
                self.items.remove(last["item"])
