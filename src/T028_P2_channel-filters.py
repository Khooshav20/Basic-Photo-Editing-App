# T028
# Khooshav Bundhoo (Leader) 101132063
# Keldan Simos 101184312
# Jackie Smolkin-Lerner 101184457
# Kaitlyn Myinia 101192031

from Cimpl import *
from unit_testing import check_equal

# Function Definitions
def red_channel(original_image: Image) -> Image:
    """Returns a red channel copy of Image original_image
    
    >>> red_channel(image1)
    Returns a copy of image1 with red RGB values only

    T028
    Author: Keldan Simos
    """ 

    red_image = copy(original_image) #create's the image's copy
    for pixel in original_image: # creates a loop that goes through every pixel, removing green and blue
        x, y, (r, g, b) = pixel
        new_colour = create_color(r,0,0)
        set_color(red_image, x, y, new_colour)

    return red_image

def test_red_channel() -> None: 
    """A test function for red_channel

    >>> test_red_channel()
    >>> Checking pixel @(0, 0) PASSED
    >>> ------
    >>> Checking pixel @(1, 0) PASSED
    >>> ------
    >>> Checking pixel @(2, 0) PASSED
    >>> ------
    >>> Checking pixel @(3, 0) PASSED
    
    T028
    Author: Keldan Simos
    """
    
    # Creates 4 pixels with set colors 
    original = create_image(4,1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 128, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))
    set_color(original, 3, 0,  create_color(255, 0, 0))
    
    # Creates 4 pixels with the expected outcome of the function
    exp = create_image(4,1) 
    set_color(exp, 0, 0,  create_color(0, 0, 0))
    set_color(exp, 1, 0,  create_color(0, 0, 0))
    set_color(exp, 2, 0,  create_color(255, 0, 0))
    set_color(exp, 3, 0,  create_color(255, 0, 0))    
    
    red_image = red_channel(original) 
    for x, y, col in red_image:               
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(exp, x, y))	


def green_channel(original_image: Image) -> Image:    
    """Returns a green channel copy of Image original_image
    
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
    """A test function for green_channel
    
    >>> test_green_channel(image1)
    
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


def blue_channel(original_image: Image) -> Image:
	"""Returns a blue channel copy of Image original_image

	>>> blue_channel(image1)
	Returns a copy of image1 with blue RGB values only

    T028
	Author: Kaitlyn Myinia
	"""

	new_pic = copy(original_image) #creates a copy of original image so as to not destroy it

	for pixel in original_image: #goes through every pixel in the image and applies filter
	    x, y, (r, g, b) = pixel
	    new_filter = create_color(0,0,b) #sets red and green components to 0
	    set_color(new_pic, x, y, new_filter) #applies filter to specific pixel

	return new_pic #returns new image with blue filter applied

def test_blue_channel() -> None:
    """A test function for blue_channel

    >>> test_blue_channel()
    >>> Checking pixel @(0, 0) PASSED
    >>> ------
    >>> Checking pixel @(1, 0) PASSED
    >>> ------
    >>> Checking pixel @(2, 0) PASSED
    >>> ------

    T028
    Author: Kaitlyn Myinia
    """

    # Manual filter to compare to blue_channel
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 128))
    set_color(expected, 2, 0,  create_color(0, 0, 255))
    
    blue = blue_channel(original)
    
    #Compares manual filter (expected) to blue_channel
    for x, y, col in blue:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))    


def combine(red_photo: Image, green_photo: Image, blue_photo: Image) -> Image:
    """Combines the RGB versions of an image to produce a full colour version.

    >>> combine(red_image, green_image, blue_image)
    Returns image of combined images
    >>> combine(test_image1, test_image2, test_image3)
    Returns image of combined images

    T028
    Author: Jackie Smolkin-Lerner
    """

    # Duplicate red image
    combined_image = copy(red_photo)

    # Combine three colour channels into one image  
    for x, y, (r, g, b) in combined_image:
        (r, g, b) = get_color(red_photo, x ,y)[0], get_color(green_photo, x, y)[1], get_color(blue_photo, x, y)[2]

        set_color(combined_image, x, y, create_color(r, g, b))

    # Return combined image
    return combined_image

def test_combine() -> None:
	"""A test function for combine

	>>> test_combine()
	>>> Checking pixel @(0, 0) PASSED
	>>> ------
	>>> Checking pixel @(1, 0) PASSED
	>>> ------
	>>> Checking pixel @(0, 1) PASSED
	>>> ------
	>>> Checking pixel @(1, 1) PASSED
	>>> ------
	>>> Checking pixel @(0, 2) PASSED
	>>> ------
	>>> Checking pixel @(1, 2) PASSED	 
	>>> ------
    
    T028
	Author: Jackie Smolkin-lerner
	"""

    # Create three example images
	image1, image2, image3 = create_image(2,3), create_image(2,3), create_image(2,3)

	set_color(image1, 0, 0, create_color(123,0,0))
	set_color(image1, 0, 1, create_color(42,0,0))
	set_color(image1, 0, 2, create_color(0,89,0))
	set_color(image1, 1, 0, create_color(0,0,0))
	set_color(image1, 1, 1, create_color(255,65,0))
	set_color(image1, 1, 2, create_color(0,0,0))

	set_color(image2, 0, 0, create_color(0,100,0))
	set_color(image2, 0, 1, create_color(0,100,0))
	set_color(image2, 0, 2, create_color(0,100,0))
	set_color(image2, 1, 0, create_color(0,100,0))
	set_color(image2, 1, 1, create_color(200,100,0))
	set_color(image2, 1, 2, create_color(0,0,0))

	set_color(image3, 0, 0, create_color(10,0,0))
	set_color(image3, 0, 1, create_color(0,0,100))
	set_color(image3, 0, 2, create_color(0,0,11))
	set_color(image3, 1, 0, create_color(23,0,14))
	set_color(image3, 1, 1, create_color(0,0,255))
	set_color(image3, 1, 2, create_color(200,0,100))

    # Create expected combined image
	original_image = create_image(2,3)

	set_color(original_image, 0, 0, create_color(123,100,0))
	set_color(original_image, 0, 1, create_color(42,100,100))
	set_color(original_image, 0, 2, create_color(0,100,11))
	set_color(original_image, 1, 0, create_color(0,100,14))	
	set_color(original_image, 1, 1, create_color(255,100,255))
	set_color(original_image, 1, 2, create_color(0,0,100))

	combined_image = combine(image1, image2, image3,)

    # Compare combined example images with expected resulting combined image
	for pixel in original_image:
		x, y, (r, g, b) = pixel
		check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',get_color(original_image, x, y), get_color(combined_image, x, y))



# Main Script
print('----------Testing red_channel----------')
test_red_channel()

print('\n----------Testing green_channel----------')
test_green_channel()

print('\n----------Testing blue_channel----------')
test_blue_channel()

print('\n----------Testing combine----------')
test_combine()

print('Choose an image to pass through red_channel()')
red_image = load_image(choose_file())
red_image = red_channel(red_image)
show(red_image)

print('Choose an image to pass through green_channel()')
green_image = load_image(choose_file())
green_image = green_channel(green_image)
show(green_image)

print('Choose an image to pass through blue_channel()')
blue_image = load_image(choose_file())
blue_image = blue_channel(blue_image)
show(blue_image)

print('Choose a red image to combine')
red_image_combine = load_image(choose_file())

print('Choose a green image to combine')
green_image_combine = load_image(choose_file())

print('Choose a blue image to combine')
blue_image_combine = load_image(choose_file())

print('Showing combined image')
combined_image = combine(red_image_combine, green_image_combine, blue_image_combine)
show(combined_image)

print('\nEND OF SCRIPT')
# END OF SCRIPT