from app import database
from app.schemas import CarInput

def test_delete_only_remove_the_target_car(database_path):
    database.initialize(database_path)
    first = database.create_car(
        database_path, CarInput(make="Toyota", model="Corolla", year=2024)
    )
    second = database.create_car(
        database_path, CarInput(make="Honda", model="Civic", year=2025)
    )
    assert database.delete_car(database_path, first.id) is True
    assert database.get_car(database_path, first.id) is None
    assert database.get_car(database_path, second.id) == second
    assert [car.id for car in database.list_cars(database_path)] == [second.id]


