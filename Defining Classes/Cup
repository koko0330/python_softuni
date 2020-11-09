class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, mililiters):
        new_quantity = self.quantity + mililiters
        if new_quantity <= self.size:
            self.quantity = new_quantity
