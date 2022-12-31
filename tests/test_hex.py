import math
from src import Hex
from tests.conftest import HEX_RADIUS


class TestHex():
    
    flatHex = None
    pointyHex = None

    def test_degree_to_radians(self):
        from src.Hex import degrees_to_radians
        assert degrees_to_radians(60) == 1.0471975511965976
        assert degrees_to_radians(180) == math.pi

    def test_create_hexes(self):
        # Test Instantiation of the objects to see all is working as intended
        self.flatHex = Hex(HEX_RADIUS)
        self.pointyHex = Hex(HEX_RADIUS, True)

        assert self.flatHex is not None
        assert self.pointyHex is not None

    def test_hex_geometry(self):
        self.flatHex = Hex(HEX_RADIUS)
        self.pointyHex = Hex(HEX_RADIUS, True)
        # Does the area check out?
        coefficient = (math.sqrt(3) * 3) * 0.5
        expected_area = coefficient * (HEX_RADIUS*HEX_RADIUS)
        flat_area = self.flatHex._outer_radius * self.flatHex._outer_radius * coefficient
        pointy_area = self.pointyHex._outer_radius * self.pointyHex._outer_radius * coefficient
        assert expected_area == flat_area
        assert expected_area == pointy_area

    def test_pointy_versus_flat(self):
        self.flatHex = Hex(HEX_RADIUS)
        self.pointyHex = Hex(HEX_RADIUS, True)

        assert self.flatHex.get_height() != self.pointyHex.get_height()
        assert self.flatHex.get_width() != self.pointyHex.get_width()
        assert self.flatHex.get_horizontal_distance() != self.pointyHex.get_horizontal_distance()
        assert self.flatHex.get_vertical_distance() != self.pointyHex.get_vertical_distance()

        assert self.flatHex.get_height() == self.pointyHex.get_width()
        assert self.flatHex.get_width() == self.pointyHex.get_height()

        assert self.flatHex.get_horizontal_distance() == self.pointyHex.get_vertical_distance()
        assert self.flatHex.get_vertical_distance() == self.pointyHex.get_horizontal_distance()

    def test_vertex_creation(self):
        self.flatHex = Hex(HEX_RADIUS)
        self.pointyHex = Hex(HEX_RADIUS, True)

        #The sum of all X coordinates of a hexagon should add up to 0
        x_sum_flat = sum([v[0] for v in self.flatHex._vertices])
        x_sum_pointy = sum([v[0] for v in self.pointyHex._vertices])

        #The sum of all Y coordinates of a hexagon should add up to 0
        y_sum_flat = sum([v[1] for v in self.flatHex._vertices])
        y_sum_pointy = sum([v[1] for v in self.pointyHex._vertices])

        assert len(self.flatHex._vertices) == 6
        assert len(self.pointyHex._vertices) == 6
        assert y_sum_flat == 0
        assert y_sum_pointy == 0
        assert x_sum_flat == 0
        assert x_sum_pointy == 0

