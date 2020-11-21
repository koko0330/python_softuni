from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet

from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.animals: List[animals] = []
        self.workers: List[workers] = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price:int):
        if price <= self.__budget and len(self.animals) + 1 <= self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif price > self.__budget and len(self.animals) + 1 <= self.__animal_capacity:
            return "Not enough budget"

        elif len(self.animals) + 1 > self.__animal_capacity:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        prev_number_of_workers = len(self.workers)
        self.workers = [
            worker
            for worker in self.workers
            if worker.name != worker_name
        ]
        if prev_number_of_workers > len(self.workers):
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        for worker in self.workers:
            self.__budget -= worker.salary

        if self.__budget >= 0:
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        for animal in self.animals:
            self.__budget -= animal.get_needs()

        if self.__budget >= 0:
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_count = 0
        tigers_count = 0
        cheetahs_count = 0

        lions_repr = []
        tigers_repr = []
        cheetahs_repr = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                tigers_count += 1
                tigers_repr.append(Tiger.__repr__(animal))

            elif animal.__class__.__name__ == "Lion":
                lions_count += 1
                lions_repr.append(Lion.__repr__(animal))

            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_count += 1
                cheetahs_repr.append(Cheetah.__repr__(animal))

        lions_repr = "\n".join(lions_repr)
        tigers_repr = "\n".join(tigers_repr)
        cheetahs_repr = "\n".join(cheetahs_repr)

        return f"""You have {len(self.animals)} animals
----- {lions_count} Lions:
{lions_repr}
----- {tigers_count} Tigers:
{tigers_repr}
----- {cheetahs_count} Cheetahs:
{cheetahs_repr}"""

    def workers_status(self):
        keepers_count = 0
        caretakers_count = 0
        vets_count = 0

        keepers_repr = []
        caretakers_repr = []
        vets_repr = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                vets_count += 1
                vets_repr.append(Vet.__repr__(worker))

            elif worker.__class__.__name__ == "Keeper":
                keepers_count += 1
                keepers_repr.append(Keeper.__repr__(worker))

            elif worker.__class__.__name__ == "Caretaker":
                caretakers_count += 1
                caretakers_repr.append(Caretaker.__repr__(worker))

        keepers_repr = "\n".join(keepers_repr)
        caretakers_repr = "\n".join(caretakers_repr)
        vets_repr = "\n".join(vets_repr)

        return f"""You have {len(self.workers)} workers
----- {keepers_count} Keepers:
{keepers_repr}
----- {caretakers_count} Caretakers:
{caretakers_repr}
----- {vets_count} Vets:
{vets_repr}"""


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())