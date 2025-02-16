# T028
# Milestone 2
# Submitted March 29th 2021

from Cimpl import Image, Color, ImageViewer, create_color, distance, \
     choose_file, show, set_color, get_color, get_height, get_width, \
     copy, create_image, load_image
from unit_testing import check_equal
from T028_image_filters import *


# Test 1
def test_three_tone() -> None:
    """
	Test function for three tone filter.

    >>> test_posterizel(image1)
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
    
    # Team: T028
    # Author: Keldan Simos
    """
     
    # creates 5 pixels with set colors 
    original = create_image(5,1) 
    set_color(original, 0, 0,  create_color(40, 50, 60))
    set_color(original, 1, 0,  create_color(0, 0, 0))
    set_color(original, 2, 0,  create_color(255, 255, 255))
    set_color(original, 3, 0,  create_color(165, 172, 170))
    set_color(original, 4, 0,  create_color(127, 128, 129))
    
    # creates 5 pixels with the expected outcome of the function
    exp = create_image(5,1) 
    set_color(exp, 0, 0,  create_color(0, 0, 0)) #white
    set_color(exp, 1, 0,  create_color(0, 0, 0)) #white
    set_color(exp, 2, 0,  create_color(255,255,255)) #black
    set_color(exp, 3, 0,  create_color(128,128,128))   #gray
    set_color(exp, 4, 0,  create_color(128, 128, 128)) #gray
    
    new_image = three_tone(original,"black","gray","white") 
    for x, y, col in new_image:               
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(exp, x, y))


# Test 2
def test_extreme_contrast() -> None:
    """
    Compares a manual alteration of an image to the automated version of the filter
    to see if the function runs correctly.
    
    >>> test_extreme_contrast()
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
    
    # Team: T028
    # Author: Kaitlyn Myinia 
    """

    original = create_image(5, 1) #creates a 5 pixel image with various colour combinations
    set_color(original, 0, 0,  create_color(128, 166, 200))
    set_color(original, 1, 0,  create_color(21, 21, 21))
    set_color(original, 2, 0,  create_color(21, 155, 127))
    set_color(original, 3, 0,  create_color(146, 60, 33))
    set_color(original, 4, 0,  create_color(128, 127, 128))
    
    # Manual filter to compare to extreme_contrast
    expected = create_image(5, 1) # manually modifies the pixels to how the filter should work 
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(255, 0, 0))
    set_color(expected, 4, 0,  create_color(255, 0, 255))
    
    contrast = extreme_contrast(original) #applies the automated function to the original coloured pixels
    for x, y, col in contrast:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
     

# Test 3
def test_sepia() -> None:
    """Test function for sepia filter.

    >>> test_sepia()
    Checking Pixel: (0, 0) PASSED
    ------
    Checking Pixel: (1, 0) PASSED
    ------
    Checking Pixel: (0, 1) PASSED
    ------
    Checking Pixel: (1, 1) PASSED
    ------
    Checking Pixel: (0, 2) PASSED
    ------
    Checking Pixel: (1, 2) PASSED
    ------

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    original_image = create_image(2, 3)
    set_color(original_image, 0, 0, create_color(0, 0, 0))
    set_color(original_image, 0, 1, create_color(63, 49, 22))
    set_color(original_image, 0, 2, create_color(99, 99, 99))
    set_color(original_image, 1, 0, create_color(64, 63, 62))
    set_color(original_image, 1, 1, create_color(200, 165, 230))
    set_color(original_image, 1, 2, create_color(254, 254, 111))

    original_image = sepia(original_image)

    expected_image = create_image(2, 3)
    set_color(expected_image, 0, 0, create_color(0, 0, 0))
    set_color(expected_image, 0, 1, create_color(48, 44, 39))
    set_color(expected_image, 0, 2, create_color(113, 99, 84))
    set_color(expected_image, 1, 0, create_color(72, 63, 53))
    set_color(expected_image, 1, 1, create_color(213, 198, 184))
    set_color(expected_image, 1, 2, create_color(222, 206, 191))

    for x, y, colours in original_image:
        check_equal("Checking Pixel: (" + str(x) + ", " + str(y) + ")", get_color(original_image, x, y),
                    get_color(expected_image, x, y))


# Test 4
def test_posterize() -> None:  
    """A test function for posterise and _adjust_component.
    
    >>> test_posterizel(image1)
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

    Team: T028
    Author: Bundhoo Khooshav Nikhil 
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

     
# Test 5
def test_detect_edges() -> None:
    """
    Test function for detect edge filter.
    
    >>> test_detect_edges()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    # Create original image
    original = create_image(2, 3)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(21, 21, 21))
    set_color(original, 0, 2, create_color(21, 155, 127))
    set_color(original, 1, 0, create_color(21, 21, 21))
    set_color(original, 1, 1, create_color(146, 60, 33))
    set_color(original, 1, 2, create_color(128, 127, 128))

    # Manually create filtered image
    expected = create_image(2, 3)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 0, 2, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 1, 2, create_color(255, 255, 255))

    # Create filtered image
    original = detect_edges(original, 50)

    for x, y, RGB in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', get_color(expected, x, y),
                    get_color(original, x, y))


# Test 6
def test_draw_curve() -> None:
    """
    Test function for draw filter 

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

   
# Test 7        
def test_flip_horizontal() -> None:
    """
	Test function for horizontal flip filter.

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(2, 2) PASSED
    ------
    
    # Team: T028
    # Author: Keldan Simos
    """
    # creates 3x3 set of pixels with set colors 
    original = create_image(3,3) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(40, 50, 60))
    set_color(original, 0, 2,  create_color(255, 255, 255))
    set_color(original, 1, 0,  create_color(0, 255, 0))
    set_color(original, 1, 1,  create_color(40, 50, 60))
    set_color(original, 1, 2,  create_color(128, 0, 128))
    set_color(original, 2, 0,  create_color(55, 48, 37))
    set_color(original, 2, 1,  create_color(4, 5, 6))
    set_color(original, 2, 2,  create_color(130, 52, 90))

    
    # creates 3x3 set of pixels with the expected outcome of the function
    exp = create_image(3,3) 
    set_color(exp, 0, 0,  create_color(55, 48, 37))
    set_color(exp, 0, 1,  create_color(4, 5, 6))
    set_color(exp, 0, 2,  create_color(130, 52, 90))
    set_color(exp, 1, 0,  create_color(0, 255, 0))
    set_color(exp, 1, 1,  create_color(40, 50, 60))
    set_color(exp, 1, 2,  create_color(128, 0, 128))
    set_color(exp, 2, 0,  create_color(0, 0, 0))
    set_color(exp, 2, 1,  create_color(40, 50, 60))
    set_color(exp, 2, 2,  create_color(255, 255, 255))
      
    
    new_image = flip_horizontal(original) 
    for x, y, col in new_image:               
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(exp, x, y))

        
# Test 8
def test_flip_vertical() -> None:
    """
    Compares a manual alteration of an image to the automated version of the filter
    to see if the function runs correctly.
    
    >>> test_vertical()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(2, 2) PASSED
    ------
    Checking pixel @(3, 2) PASSED
    ------
    
    # Team: T028
    # Author: Kaitlyn Myinia 
    """

    original = create_image(4, 3) #creates an image with various colour combinations
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(128, 128, 128))
    set_color(original, 0, 2,  create_color(255, 255, 255))
    
    set_color(original, 1, 0,  create_color(255, 0, 0))
    set_color(original, 1, 1,  create_color(255, 60, 60))
    set_color(original, 1, 2,  create_color(255, 128, 128))
    
    set_color(original, 2, 0,  create_color(0, 255, 0))
    set_color(original, 2, 1,  create_color(60, 255, 77))
    set_color(original, 2, 2,  create_color(128, 255, 128))
    
    set_color(original, 3, 0,  create_color(0, 0, 255))
    set_color(original, 3, 1,  create_color(60, 60, 255))
    set_color(original, 3, 2,  create_color(128, 128, 255))
    
    # Manual filter to compare to extreme_contrast
    expected = create_image(4, 3) # manually modifies the pixels to how the filter should work 
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 0, 1,  create_color(128, 128, 128))
    set_color(expected, 0, 2,  create_color(0, 0, 0))
    
    set_color(expected, 1, 0,  create_color(255, 128, 128))
    set_color(expected, 1, 1,  create_color(255, 60, 60))
    set_color(expected, 1, 2,  create_color(255, 0, 0))
    
    set_color(expected, 2, 0,  create_color(128, 255, 128))
    set_color(expected, 2, 1,  create_color(60, 255, 77))
    set_color(expected, 2, 2,  create_color(0, 255, 0))
    
    set_color(expected, 3, 0,  create_color(128, 128, 255))
    set_color(expected, 3, 1,  create_color(60, 60, 255))
    set_color(expected, 3, 2,  create_color(0, 0, 255))

    flip = flip_vertical(original) #applies the automated function to the original coloured pixels
    for x, y, col in flip:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))    
        

# Main Script
if __name__ == "__main__":
	print("\n------Testing three_tone()------")
	test_three_tone()

	print("\n------Testing extreme_contrast()------")
	test_extreme_contrast()

	print("\n------Testing posterize()------") 
	test_posterize()

	print("\n------Testing sepia()------") 
	test_sepia()

	print("\n------Testing detect_edges()------") 
	test_detect_edges()

	print("\n------Testing draw_curve()------") 
	test_draw_curve()

	print("\n------Testing flip_horizontal()------") 
	test_flip_horizontal()

	print("\n------Testing flip_vertical()------") 
	test_flip_vertical()
