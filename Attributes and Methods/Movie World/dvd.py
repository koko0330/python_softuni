from typing import Dict


class DVD:
    _month_by_number: Dict[str, str] = {
        "1": "January",
        "2": "Febraury",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    def rent(self):
        self.is_rented = True

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year, *rest = date.split(".")

        creation_month = cls._month_by_number[month]

        return cls(name, id, int(year), creation_month, age_restriction,)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"

