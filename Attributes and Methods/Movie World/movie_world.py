from project.customer import Customer
from project.dvd import DVD

from typing import List


class MovieWorld:
    name: int
    customer: List[Customer]
    dvds: List[DVD]

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
        self.dvd_ids = {}
        self.customer_ids = {}

    _CUSTOMER_CAPACITY = 10
    _DVD_CAPACITY = 15

    @classmethod
    def dvd_capacity(cls):
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) >= self._CUSTOMER_CAPACITY:
            return

        self.customers.append(customer)
        self.customer_ids[customer.id] = customer

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) >= self._DVD_CAPACITY:
            return

        self.dvds.append(dvd)
        self.dvd_ids[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)

        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        dvd.rent()
        customer.add_dvd(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.customer_ids.get(customer_id)
        dvd = self.dvd_ids.get(dvd_id)

        if not customer.has_dvd(dvd):
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        self.dvds.append(dvd)
        customer.remove_dvd(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))

        return '\n'.join(customers + dvds)