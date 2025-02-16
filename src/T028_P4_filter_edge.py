# Team: T028
# Author: Bundhoo Khooshav Nikhil 101132063

from Cimpl import create_color, get_width, get_height, \
     get_color, set_color, load_image, Image, choose_file, show


def _average(pixel: list) -> float:
    """
    Returns the average of the RGB values.
    
    >>> average(10+10+10)/3
    10.0
    
    Team: T028
    Author: Bundhoo Khooshav Nikhil 10113206
    """

    (r,g,b) = pixel
    return (r+g+b)/3


def detect_edges(image: Image, threshold: int) -> Image:
    """
    Returns a new image in which the edge of the argument 
    are highlighted and the colours are reduced to black and white.
    
    >>> detect_edges("p2_original.png", 2)
    returns a pencil sketch of the dog.
    
    Team: T028
    Author: Bundhoo Khooshav Nikhil 101132063  
    """
    
    black_color = create_color(0,0,0)
    white_color = create_color(255,255,255)
    new_image = image.copy()
    
    height = image.get_height()
    width = image.get_width()
    bottom_row = height - 1
    
    for y in range(bottom_row):       # Loop through each row of pixel until the bottom row
        for x in range(width):
            top_color = image.get_color(x, y)
            bottom_color = image.get_color(x, y+1)
            
            top_brightness = _average(top_color)
            bottom_brightness = _average(bottom_color)
            
            if abs(top_brightness - bottom_brightness) > threshold:
                new_image.set_color(x, y, black_color)
            else:
                new_image.set_color(x, y, white_color)

    for x in range(width):          # Set the color of each pixel in the bottom row to white
        new_image.set_color(x, bottom_row, white_color)

    return new_image
    
    
# Main Script
if __name__ == "__main__":
    # original_image = load_image(input('Enter the name of an image to pass through detect_edges(): '))
    
    print('Choose an image to pass through extreme_contrast()')
    original_image = load_image(choose_file())       
    
    detect_edges_image = detect_edges(original_image, 5)
    show(original_image)
    show(detect_edges_image)
