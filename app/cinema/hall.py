
class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"Movie session: {movie_name} started in hall {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie session: {movie_name} ended in hall {self.number}.")
        cleaning_staff.clean_hall(self.number)
