#T028
#Bundhoo Khooshav Nikhil 101132063

from Cimpl import *
from unit_testing import check_equal
from T028_P3_filter_posterize import posterize

def test_posterize() -> None:  
    """A test function for posterise and _adjust_component
    
    >>> test_posterizel(image1)
    
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

    
    #T028
    #Author: Bundhoo Khooshav Nikhil 
    #101132063
    """
    # This test function checks if posterize correctly transforms:
    # (0, 0, 0) to (31, 31, 31)
    # (0, 1, 1) to (31, 31, 31)
    # (0, 255, 255) to (31, 223, 223)  
    # (165, 42, 42) to (159, 31, 31) 
    # (170, 51, 106) to (159, 31, 95)   
    
    # Create an image with five pixels.
    original = create_image(5, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 1, 1))
    set_color(original, 2, 0,  create_color(0, 255, 255))
    set_color(original, 3, 0,  create_color(165, 42, 42))
    set_color(original, 4, 0,  create_color(170, 51, 106))
    
    # Create an image that's identical to the one a correct implementation of
    # posterize should produce when it is passed original.

    expected = create_image(5, 1)
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 31, 31))
    set_color(expected, 2, 0,  create_color(31, 223, 223))
    set_color(expected, 3, 0,  create_color(159, 31, 31))
    set_color(expected, 4, 0,  create_color(159, 31, 95))
    
    
    posterize_image = posterize(original)   
    for x, y, col in posterize_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

#Main Script

test_posterize()