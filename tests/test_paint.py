import os
from PIL import Image

from src import GridPainter, Hex
from tests.conftest import HEX_RADIUS

class TestPaint():
    def test_create_object(self):
        output_path = os.getcwd()
        resolution = '1920x1080'
        margins = '160x90'

        test_hex = Hex(HEX_RADIUS)

        grid_painter = GridPainter(output_path, resolution, margins, test_hex)

        expected_max_hexes_x = (1920 - 320) / test_hex.get_horizontal_distance()
        expected_max_hexes_y = (1080 - 180) / test_hex.get_vertical_distance()
        
        assert grid_painter.margin[0] == 160
        assert grid_painter.margin[1] == 90
        assert grid_painter.output_path == output_path
        assert grid_painter.resolution[0] == 1920
        assert grid_painter.resolution[1] == 1080

        assert grid_painter.max_x == int(expected_max_hexes_x)
        assert grid_painter.max_y == int(expected_max_hexes_y)

    def test_create_image(self):
        output_path = os.getcwd()
        resolution = '1920x1080'
        margins = '160x90'

        test_hex = Hex(HEX_RADIUS)

        grid_painter = GridPainter(output_path, resolution, margins, test_hex)
        grid_painter.start_drawing()

        image_file = [f for f in os.scandir(output_path) if f.name == 'test.png'][0]
        assert image_file.is_file()
        with Image.open(f'{output_path}/{image_file.name}') as im:
            assert im.format == 'PNG'
            assert im.size == (1920,1080)
        
        os.remove(f'{output_path}/{image_file.name}')
    
