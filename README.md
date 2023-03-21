# Contour Detection and Analysis using OpenCV

This project provides a Python script that uses the OpenCV library to detect and analyze contours in images. The script reads an input image, processes it to find contours, and then calculates various properties of the detected contours, such as the distances between their corner points.

## Features

- Detects contours in images using OpenCV's built-in functions.
- Filters contours based on their area.
- Draws contour lines and corner points on the original image.
- Calculates and displays the distance between corner points in both pixels and centimeters.
- Normalizes the corner coordinates of the detected contours.

## Dependencies

- OpenCV
- NumPy

## How to Use

1. Ensure that you have the required dependencies installed.
2. Place your input image in the project folder and update the `path` variable in the script to point to the correct image file.
3. Run the script. The processed image will be displayed in a window. Press any key to exit the loop and close the window.

## Functions

The following functions are provided in the script:

- `get_ratio_pixels_millimeters`: Calculates the conversion factor from pixels to millimeters based on the size of an ArUco marker in the image.
- `draw_enumerate`: Draws the corner points of a contour on the image and labels them with their index.
- `draw_corners`: Draws lines connecting the corners of a polygon on an image and adds text with the distance between the corners in both pixels and centimeters.
- `get_bounding_box`: Calculates the bounding rectangle of a contour, and optionally draws it on the image.
- `transform`: Normalizes the corner coordinates of a contour based on its bounding rectangle.

## Example

The example script reads an input image, processes it using a series of OpenCV functions (converting to grayscale, applying Gaussian blur, detecting edges with Canny, dilating and eroding), and then detects and analyzes contours of interest. The script draws the simplified contours, corner points, and bounding boxes on the original image, calculates the real-world distances between corner points, and prints the normalized corner coordinates.

## License

This project is open-source and available for personal and educational purposes.
