"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle

# TODO write 3 tests as described above


class TestCircle:

    def test_add_area(self):
        C1 = Circle(3)
        C2 = Circle(4)
        result = C1.add_area(C2)
        assert result.get_radius() == 5

    def test_add_area_edge_case(self):
        Circle1 = Circle(0)
        Circle2 = Circle(5)
        result2 = Circle1.add_area(Circle2)
        assert result2.get_radius() == 5

    def test_add_area_negative_case(self):
        with self.assertRaises(ValueError):
            Circle(-1)