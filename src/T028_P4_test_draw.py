# Team: T028
# Author: Bundhoo Khooshav Nikhil 101132063

from Cimpl import Image, create_image, create_color, set_color, get_color
from unit_testing import check_equal
from T028_P4_filter_draw import draw_curve  


def test_draw_curve():
    """
    Test function for draw filter.

    >>> test_draw_curve()
    The image is 5 pixels wide, and 5 pixels tall.

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(2, 2) PASSED
    ------
    Checking pixel @(3, 2) PASSED
    ------
    Checking pixel @(4, 2) PASSED
    ------
    Checking pixel @(0, 3) PASSED
    ------
    Checking pixel @(1, 3) PASSED
    ------
    Checking pixel @(2, 3) PASSED
    ------
    Checking pixel @(3, 3) PASSED
    ------
    Checking pixel @(4, 3) PASSED
    ------
    Checking pixel @(0, 4) PASSED
    ------
    Checking pixel @(1, 4) PASSED
    ------
    Checking pixel @(2, 4) PASSED
    ------
    Checking pixel @(3, 4) PASSED
    ------
    Checking pixel @(4, 4) PASSED
    ------
    Checking intersects: PASSED
    ------
    
    Team: T028
    Author: Bundhoo Khooshav Nikhil 101132063
    """
    
    # Create original image
    original = create_image(5, 5, create_color(255, 255, 255)) 

    # Manually create filtered image
    expected = create_image(5, 5, create_color(255, 0, 0))
    set_color(expected, 0, 3, create_color(255, 255, 255))
    set_color(expected, 0, 4, create_color(255, 255, 255))
    set_color(expected, 1, 4, create_color(255, 255, 255))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(255, 255, 255))
    set_color(expected, 4, 1, create_color(255, 255, 255))

    # Create filtered image
    original, intersects = draw_curve(original, "blood", [(0,0), (1,1)])
    
    for x, y, RGB in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
         get_color(expected, x, y), get_color(original, x, y))

    check_equal('Checking intersects:', [(0,0), (4,4)], intersects)   


# Main Script
if __name__ == "__main__":
    test_draw_curve()
