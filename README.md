 AOI_Drawer - Polygon Tool GUI
==============================

DESCRIPTION
-----------
AOI_Drawer is a simple Python-based graphical tool that allows users to manually define polygonal Areas of Interest (AOIs) on top of a background image. It is useful for tasks such as satellite imagery labeling, area annotation, or geographic region definition.

The project includes:
- AOI_Drawer.py  : Main class to interactively draw and fill polygons using OpenCV
- main.py        : Entry-point script to launch the tool with a user-defined image


REQUIREMENTS
------------
- Python 3.6+
- OpenCV (cv2)
- NumPy

Install dependencies via pip:
    pip install opencv-python numpy


USAGE INSTRUCTIONS
------------------
1. Place your target background image (e.g. a satellite image) in:
   /home/cesccgasso/Python-Projects/Tools/AOI_Drawer/Images/

2. Open and edit `main.py` to set the desired image name:
       image_name = "your_image.png"

3. Run the script:
       python main.py

4. Use the following controls:

   - Left Click     : Add polygon vertex
   - 'z'            : Undo last point
   - 'r'            : Reset image
   - 's'            : Save annotated image as 'annotated_output.png'
   - 'q'            : Quit the application

   Tip: To complete the polygon, click near the starting point.

5. After completion, the filled polygon will be blended into the image with 50% opacity.

NOTES
-----
- Saved images are written to the same folder as the script.
- Polygons are drawn with semi-transparent overlay for better visibility.
- Only one polygon can be drawn at a time (current version). Press 'r' to start a new one.

LICENSE
-------
This project is distributed for educational and research purposes only.

AUTHOR
------
Cesc Casanovas Gassó
