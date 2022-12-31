# Hex Gridder
---

This simple module outputs an image of the desired resolution with a grid of hexes of the specified size drawn on top.

This was created as a tool to help create template images for hex-maps in D&D but feel free to use the created images in whatever way you want.

By changing the config file, an PNG file with a transparent background can be created to be imported into your favorite image editor.

![Map of a Hex Grid](https://github.com/amonjerro/hex-grid-maker/blob/master/example/example.png)

# How to use
---

## Basic setup

Clone this repo onto your machine and create a virtual environment and install the requirements. The only real requirement for this file is PIL, so if you already have it on your machine, feel free to skip this part.

```
python -m venv venv
```

Activate that virtual environment using the method for your OS and then install the requirements

```
python -m pip install -r requirements.txt
```

## Running the program

To run the program use the following command

```
python ./main.py
```

You can pass the following options to the program.
- -r / --resolution RESOLUTION: a string in a WxH format (eg 1920x1080) that will inform the program the size of the image to make. Defaults to 1920x1080
- -s / --scale SCALE: the size of the outer radius of a hex. This should be an integer as it informs pixel size. Defaults to 10.
- -o / --output_path OUTPUT_PATH: a string to inform where the image should be saved. Defaults to the current working directory.
- -m / --margin MARGIN: the size of the margins to leave, specified in the same WxH format as the resolution. Defaults to 160x90
- -p / --pointy: A boolean flag that informs whether the hexes should be pointy.

You can also use the following command for that information: `python ./main.py -h `


