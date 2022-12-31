from PIL import Image, ImageDraw, ImageFont
from config.config import CONFIG


class GridPainter:
    '''Creates a hex-grid image.
        Args:
            - output_path: Folder where the image will be created, passed from program arguments
            - resolution: Resolution of the image, passed from program arguments
            - margins: Margins where no drawing will occur, passed from program arguments
            - hex: A single Hex object that will be used as a template to draw from.
    '''
    def __init__(self, output_path, resolution, margins, hex):
        self.output_path = output_path
        self.resolution = tuple(map(lambda x: int(x),resolution.split('x')))
        self.margin = tuple(map(lambda x: int(x), margins.split('x')))
        self.hex = hex
        self.max_x = 0
        self.max_y = 0
        self._determine_dimensions()


    def _determine_dimensions(self):
        total_drawable_width = self.resolution[0] - (2*self.margin[0])
        total_drawable_height = self.resolution[1] - (2*self.margin[1])
        hex_width = self.hex.get_horizontal_distance()
        hex_height = self.hex.get_vertical_distance()
        self.max_x = int(total_drawable_width / hex_width)
        self.max_y = int(total_drawable_height / hex_height)

    def draw_pointy(self, drawContext):
        for y in range(self.max_y):
            for x in range(self.max_x):
                if y % 2 == 1:
                    self.draw_hex(drawContext, 
                    0.5*self.hex.get_width()+self.hex.get_horizontal_distance()*x+self.margin[0],
                    self.hex.get_vertical_distance()*y+self.margin[1])
                else:
                    self.draw_hex(drawContext, 
                    self.hex.get_horizontal_distance()*x+self.margin[0],
                    self.hex.get_vertical_distance()*y+self.margin[1])

    def draw_flat(self, drawContext):
        for x in range(self.max_x):
            for y in range(self.max_y):
                if x % 2 == 1:
                    self.draw_hex(drawContext, 
                    self.hex.get_horizontal_distance()*x+self.margin[0],
                    self.hex.get_vertical_distance()*y+self.margin[1])
                else:
                    self.draw_hex(drawContext, 
                    self.hex.get_horizontal_distance()*x+self.margin[0],
                    0.5*self.hex.get_height()+self.hex.get_vertical_distance()*y+self.margin[1])
    
    def append_map_dimensions(self, drawContext):
        drawContext.text((10,10), 
            f'Width: {self.max_x}, Height: {self.max_y}',
            fill=(0,0,0),
            font=ImageFont.truetype('arial.ttf', 15)
            )
        

    def start_drawing(self):
        im = Image.new('RGBA', self.resolution, (256,256,256, CONFIG.get('alpha_value',0)))
        drawContext = ImageDraw.Draw(im)

        # Offsets need to be handled differently according to orientation
        if self.hex.pointy:
            self.draw_pointy(drawContext)
        else:
            self.draw_flat(drawContext)
        
        if CONFIG.get('include_dimensions'):
            self.append_map_dimensions(drawContext)

        with open(f'{self.output_path}/{CONFIG.get("output_name","")}', 'wb') as f:
            im.save(f, "PNG")

    def draw_hex(self, drawContext, x, y):
        # Update the vertex coordinates to the local draw space
        vertices = [ (v[0]+x, v[1]+y)  for v in self.hex._vertices ]

        # Draw the conecting each vertex
        for i in range(len(vertices)):
            if i == len(vertices)-1:
                drawContext.line([vertices[-1], vertices[0]], fill=(0,0,0), width=1)
            else:
                drawContext.line([vertices[i], vertices[i+1]], fill=(0,0,0), width=1)