import argparse
from src import Hex, GridPainter
import os

parser = argparse.ArgumentParser()

parser.add_argument("-r","--resolution", 
        help="Specify the image resolution in WxH format. Defaults to 1920x1080.",
        default="1920x1080")
parser.add_argument("-p","--pointy",
        help="Make the hexes pointy rather than flat-topped.",
        action="store_true")
parser.add_argument('-s','--scale',
        help="Set size of the hex inner radius. Defaults to 10.",
        type=int, default=10)
parser.add_argument('-o', '--output_path',
        help="Output path of the desired file. Defaults to current working directory",
        default=os.getcwd())
parser.add_argument('-m','--margin',
        help="Size of the margins. Use a WxH format. Defaults to 160x90",
        default="160x90")

if __name__ == '__main__':
    args = parser.parse_args()
    h = Hex(args.scale, args.pointy)
    GridPainter(args.output_path, args.resolution, args.margin, h).start_drawing()    
