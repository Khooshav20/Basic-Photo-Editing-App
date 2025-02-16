#T028
#Bundhoo Khooshav Nikhil 101132063

from Cimpl import *
from unit_testing import check_equal

def green_channel(original_image:Image)-> Image:    
    """Returns a green channel copy of Image original_image.
    
    >>> green_channel(image1)
    Returns a copy of image1 with green RGB values only

    T028
    Author: Bundhoo Khooshav Nikhil 
    """
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0,g,0)
        set_color (new_image, x, y, new_colour)
    
    return new_image

def test_green_channel() -> None:  
    """A test function for green_channel.
    
    >>> test_green_channel()
    
    >>> Checking pixel @(0, 0) PASSED
    >>> ------
    >>> Checking pixel @(1, 0) PASSED
    >>> ------
    >>> Checking pixel @(2, 0) PASSED
    >>> ------
    >>> Checking pixel @(3, 0) PASSED
    >>> ------
    >>> Checking pixel @(4, 0) PASSED
    >>> ------

    T028
    Author: Bundhoo Khooshav Nikhil 
    """
    
    # This test function checks if green_channel correctly transforms:
    # (0, 0, 0) to (0, 0, 0)
    # (0, 1, 1) to (0, 1, 0)
    # (0, 255, 255) to (0, 255, 0)  #aqua
    # (165, 42, 42) to (0, 42, 0)   #brown
    # (170, 51, 106) to (0, 51, 0)   #dark pink
    
    # Create an image with five pixels.
    original = create_image(5, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 1, 1))
    set_color(original, 2, 0,  create_color(0, 255, 255))
    set_color(original, 3, 0,  create_color(165, 42, 42))
    set_color(original, 4, 0,  create_color(170, 51, 106))
    
    # Create an image that's identical to the one a correct implementation of
    # green_channel should produce when it is passed original.
    
    expected = create_image(5, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 1, 0))
    set_color(expected, 2, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(0, 42, 0))
    set_color(expected, 4, 0,  create_color(0, 51, 0))
    
    green_image = green_channel(original)   
    for x, y, col in green_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


#Main Script

test_green_channel()

print('Choose an image to pass through green_channel()')

original_image = load_image(choose_file())

green_image = green_channel(original_image)
show(original_image)
show(green_image)