import math
from decimal import Decimal

def degrees_to_radians(x):
    return x*(math.pi/180)

class Hex:
    def __init__(self, outer_radius, pointy=False):
        '''
            Class that creates and manages the information pertaining to the hex used by the hex-grid
            Args:
                - outer_radius: Radius size where all vertices will lie
                - pointy: Boolean to determine whether to draw pointy-topped or flat-topped hexes
        '''
        self._outer_radius = outer_radius
        self._inner_radius = 0.5*outer_radius*math.sqrt(3)

        self.pointy = pointy
        self._vertices = self._calculate_vertices()
    
    def get_horizontal_distance(self):
        if self.pointy:
            return 2*self._inner_radius
        
        return 1.5 * self._outer_radius


    def get_vertical_distance(self):
        if self.pointy:
            return 1.5 * self._outer_radius
        
        return 2*self._inner_radius
    
    def get_width(self):
        if self.pointy:
            return 2*self._inner_radius
        
        return 2*self._outer_radius
    
    def get_height(self):
        if self.pointy:
            return 2*self._outer_radius
        
        return 2*self._inner_radius
    
    def _calculate_vertices(self):
        result_set = []
        degree_offset = 0
        if self.pointy:
            degree_offset = 90

        # We use theorem that x_2 = cos(a)*x_1 - sin(a)*y_1 and y_2 = sin(a)*x_1 + cos(a)*y_1 for vector rotation 
        # to establish vertex positions. Thus, we must establish an origin x_1 and y_1
        x_1 = self._outer_radius
        y_1 = 0

        # Draw along the hex outer radius - all vertices must lie there.
        for i in range(6):
            angle = i * 60
            radians = degrees_to_radians(angle+degree_offset)
            # Convert to decimal to avoid floating point imprecisions when rounding
            x_coord = Decimal.from_float(math.cos(radians)*x_1 - math.sin(radians)*y_1).quantize(Decimal('0.01'))
            y_coord = Decimal.from_float(math.sin(radians)*x_1 + math.cos(radians)*y_1).quantize(Decimal('0.01'))

            #Convert coordinates back to floats
            result_set.append((float(x_coord), float(y_coord)))

        return result_set