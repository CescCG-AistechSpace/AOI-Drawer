"""
## USER! Insert the following data to generate your AOI boundary image:
# 1. Insert the Image Name which you want to use as a background for the AOI boundary
# 2. Run the main.py script and follow the instructions in the console:

Polygon Tool Instructions:
- Left click to add polygon points
- Press 'Ctrl' + 's' to save the image
- Press 'r' to reset
- Press 'q' to quit
- Press 'z' to undo last point
"""

import AOI_Drawer
import os
import sys

# 1. Insert the Image Name which you want to use as a background for the AOI boundary
i = 0
print("Welcome to AOI Drawer!")
print("Images available to use:")
for file in os.listdir("Images"):
    i+=1
    if file.endswith(('.png', '.jpg', '.jpeg')):
        print(f'({i}) '+file)
try:
    image_name = os.listdir("Images")[int(input("Enter image number: "))-1]
except (ValueError, IndexError):
    print("Invalid input. Please enter a valid number.")
    sys.exit(1)


# 2. Run the main.py script and follow the instructions in the console.

def main():
    image_path = "/home/cesccgasso/Python-Projects/Tools/AOI_Drawer/Images/" + image_name  # Default image path
    print(f"Loading image from: {image_path}")
    
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found")
        sys.exit(1)
    
    try:
        tool = AOI_Drawer.PolygonTool(image_path)
        tool.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()