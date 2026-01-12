from typing import List

from app.cinema.bar import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: List[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f"Movie session: {movie_name} started in hall {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie session: {movie_name} ended in hall {self.number}.")
        cleaning_staff.clean_hall(self.number)
