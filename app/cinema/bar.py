class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

class Customer:
    def __init__(self, name, food) -> None:
        self.name = name
        self.food = food
