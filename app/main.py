from app.cinema.bar import CinemaBar, Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, customers=customers,
                       cleaning_staff=cleaning_staff)
