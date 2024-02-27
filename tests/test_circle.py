from pytest import fixture, raises

from geometric import Circle


@fixture
def circle():
    return Circle(6)


def test_init(circle):
    assert circle.radius == 6


def test_diameter(circle):
    assert circle.diameter == 12


def test_calculate_area(circle):
    assert circle.calculate_area() == 113.09733552923255


def test_calculate_circumference_length(circle):
    assert circle.calculate_circumference_length() == 37.69911184307752


def test_calculate_area_of_sector(circle):
    assert circle.calculate_area_of_sector(45) == 14.137166941154069


def test_calculate_area_of_sector_raise_error(circle):
    with raises(Exception) as exc_info:
        circle.calculate_area_of_sector(361)
    assert str(exc_info.value) == "The central angle must be between 0 and 360"
