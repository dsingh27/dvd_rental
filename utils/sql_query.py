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
