import sqlite3
from sqlite3 import Error

# what is a class in python?
# A class is a blueprint for the object. It defines a set of attributes that are associated with the object.

# what is an object in python?
# An object is an instance of a class. It can store data using the attributes defined in the class and perform operations using the methods defined in the class.

# what is a method in python?
# A method is a function that is associated with a class. It can be used to perform operations on the object.


class DVDRental:
    def __init__(self, path):
        self.path = path
        self.connection = None
        
        self.abc = "Divya"
        
    # class method
    @classmethod
    def create_connection(cls, path):
        print(self.abc)
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite is successful")
        except Error as e:
            print(f"The error '{e}' occured")
        
    # def create_connection(self):
    #     try:
    #         self.connection = sqlite3.connect(self.path, timeout=20)
    #         print("Connection to SQLite is successful")
    #     except Error as e:
    #         print(f"The error '{e}' occured")
    
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occured")
            
        return cursor.fetchall()


if __name__ == '__main__':
    # create_connection("sqlite-sakila.db")
    db_instance = DVDRental("sqlite-sakila.db")
    
    rented_film_and_revenue = """
    

WITH rented_film as (
SELECT
    rental.rental_id,
    film.film_id,
    film.title,
    film.rental_rate,
    film.replacement_cost
    FROM inventory
    JOIN film ON inventory.film_id = film.film_id
    JOIN rental ON inventory.inventory_id = rental.inventory_id
)
SELECT
    rented_film.title,
    count(rented_film.title) as n_film,
    sum(payment.amount) as revenue_by_film
FROM payment
JOIN rented_film USING(rental_id)
GROUP BY rented_film.title
"""

    result = db.execute_query(rented_film_and_revenue)
    print(result)