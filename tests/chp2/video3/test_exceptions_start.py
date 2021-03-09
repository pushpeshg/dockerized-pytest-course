from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.25664, -555.23564)
    assert str(exp.value) == "Invalid value"

    with pytest.raises(ValueError) as exp:
        Point(5, 12.11386, -55.08232)
    assert str(exp.value) == "City name should be string"
