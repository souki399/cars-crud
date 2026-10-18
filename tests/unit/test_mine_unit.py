from app.schemas import CarInput

def test_color_whitespace_becomes_empty():
    car = CarInput(make="Toyota",model="Corolla",year=2024,color="    ")
    assert car.color == ""