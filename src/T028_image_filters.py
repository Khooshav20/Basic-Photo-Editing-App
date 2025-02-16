# T028 
# Milestone 2 
# Submitted March 29th 2021

from Cimpl import Image, Color, ImageViewer, create_color, distance, \
     choose_file, show, set_color, get_color, get_height, get_width, \
     copy, create_image, load_image
from simple_Cimpl_filters import grayscale
from point_manipulation import get_x_y_lists, sort_points
from numpy import polyval, polyfit


# Function 1
def three_tone(original_image: Image, dark_tone: str, 
    grey_tone: str, light_tone: str) -> Image:
    """
    Return a copy of original_image with its shadows, midtones, and 
    highlights replaced with three selected colors: dark_tone, grey_tone, 
    and light_tone, respectively.

    >>> test_image = load_image(choose_file())
    >>> three_tone(test_image, 'black' ,'white', 'blood')
    Returns a copy of original_image with black, white, and blood colors.

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    tones = [dark_tone, grey_tone, light_tone]

    # Create list of name and color tuples
    COLOURS = [("black", (0, 0, 0)),
            ("white", (255, 255, 255)),
            ("blood", (255, 0, 0)),
            ("green", (0, 255, 0)),
            ("blue", (0, 0, 255)),
            ("lemon", (255, 255, 0)),
            ("aqua", (0, 255, 255)),
            ("pink", (255, 0, 255)),
            ("gray", (128, 128, 128))]

    # Duplicate original image
    new_image = copy(original_image)

    # Convert tone names to RGB values
    for num in range(len(tones)):
        for colour_name, colour in COLOURS:
            if tones[num] == colour_name:
                tones[num] = colour

    # Modify pixels of copied image
    for x, y, (r, g, b) in new_image:

        if (r + g + b) / 3 < 85:
            r, g, b = tones[0]

        elif (r + g + b) / 3 < 171:
            r, g, b = tones[1]

        else:
            r, g, b = tones[2]

        set_color(new_image, x, y, create_color(r, g, b))
        
    return new_image


# Function 2
def extreme_contrast(original_image: Image) -> Image:
    """
    Returns a copy of an image in which the contrast 
    between the pixels has been maximised.

    >>> extreme_constrast(image1)
    returns a copy of image1 in which the RGB components of each pixel 
    is set to their minimum or maximum values to maximuse the contrast.
    
    
    # Team: T028
    # Author: Bundhoo Khooshav Nikhil 101132063 
    """

    new_image = copy(original_image)  

    for pixel in original_image:
        x, y, (r, g, b) = pixel

        if r <= 127:
            r = 0
        else:
            r = 255
        
        if g <= 127:
            g = 0
        else:
            g = 255
        
        if b <= 127:
            b = 0
        else:
            b = 255

        new_colour = create_color(r, g, b)
        set_color (new_image, x, y, new_colour)        

    return new_image


# Function 3
def sepia(image: Image) -> Image:
    """
    Takes an image for an argument, the applies the grayscale function to it
    After the grayscale is applied the r and b values for each pixel are 
    modified based on their brightness, since we want a sepia filter, it
    increases the red and decreases the blue values based on the brightness 
    of the pixel.
    
    >>>sepia(image1)
    returns a near grayscale image witht the red values increased and blue decreased. 
    
    Team: T028
    Author: Keldan Simos
    """

    # creates a new image with the greyscale filter applied 
    new_image = grayscale(image)
    # creates changed versions of the red and blue values for each pixel at a time
    for x, y, (r, g, b) in new_image:
        if r<63:
            sep = create_color(r*1.1, g, b*0.9)
        elif r>=63 and r<=191:
            sep = create_color(r*1.15, g, b*0.85)
        else:
            sep = create_color(r*1.08, g, b*0.93)
        # this new colour that was created is then applied to the pixel
        set_color(new_image, x, y, sep)     

    return new_image
    
     
# Function 4
def _adjust_component(val: int) -> int: #a function to be used in posterize function
    """
    Determines the quadrant that the value of the RGB component lies in, and returns
    the midpoint of said quadrant.
    
    >>>_adjust_component(50)
    31
    >>>_adjust_component(115)
    95
    >>>_adjust_component(130)
    159
    >>>_adjust_component(255)
    233
    
    Team: T028
    Author: Kaitlyn Myinia
    """

    if(val <= 63): #if the value is between 0 to 63, then it is changed to 31 - Quadrant 1
        return 31
    elif(val >= 64 and val <= 127): #if the value is between 64 to 127, then it is changed to 95 - Quadrant 2
        return 95
    elif(val >= 128 and val <= 191): #if the value is between 128 to 191, then it is changed to 159 - Quadrant 3
        return 159
    else: #if the value is between 192 to 255, then it is changed to 223 - Quadrant 4
        return 223


def posterize(original_img: Image) -> Image:
    """
    Returns a copy of the inputed image that has a smaller number of colours than
    the original. 
    
    >>> posterize(image_1)
    Returns a copy of image_1 with a smaller number of colours.
    
    Team: T028
    Author: Kaitlyn Myinia
    """

    new_pic = copy(original_img) #creates a copy of original image so as to not destroy it

    for pixel in original_img: #goes through every pixel in the image and applies filter
        x, y, (r, g, b) = pixel
        #changes every RGB value to the midpoint of its quadrant
        new_c = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)) 
        set_color(new_pic, x, y, new_c) #applies filter to specific pixel
    
    return new_pic


# Function 5
def _average(pixel: list) -> float:
    """
    Returns the average of the RGB values.
    
    >>> average(10+10+10)/3
    10.0
    
    Team: T028
    Author: Bundhoo Khooshav Nikhil 10113206
    """

    (r,g,b) = pixel
    return (r + g + b)/3


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
            bottom_color = image.get_color(x, y + 1)
            
            top_brightness = _average(top_color)
            bottom_brightness = _average(bottom_color)
            
            if abs(top_brightness - bottom_brightness) > threshold:
                new_image.set_color(x, y, black_color)
            else:
                new_image.set_color(x, y, white_color)

    for x in range(width):          # Set the color of each pixel in the bottom row to white
        new_image.set_color(x, bottom_row, white_color)

    return new_image


# Function 6
def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    """
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.

    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    EPSILON = 1
    step = EPSILON ** 2
    x = 0.0

    while x <= max_x and abs(polyval(polycoeff, x) - val) >= EPSILON:
        x += step

    if x > max_x:
        return None

    return round(x)


def _interpolation(point_list: list) -> list:
    """
    Returns a list containing the three coefficients of a polynomial
    function based on point_list. If there is one point, nothing will be 
    returned. If there are two points, the coefficients will be of a first 
    degree polynomial going through the points. If there are three or more 
    points, the coefficients will be for a second degree polynomial.

    >>> _interpolation([(1, 2), (3, 5), (2,4)])
    [-0.5, 3.5, -1]
    >>> _interpolation([(0, 0), (100, 100)])
    [0, 1, 0]
    >>> _interpolation([(22, 44), (81, 12), (100, 0) ,(0, 118)])
    [0, -1.021912424455897, 95.36205554113674]

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    x_list, y_list = get_x_y_lists(point_list)

    if len(point_list) < 3:
        return list(polyfit(x_list, y_list, 1))

    else:
        return list(polyfit(x_list, y_list, 2))


def _image_border_finding(image_size: list, coeffs: list):
    """
    Returns all points where f(x) intersects with the border of an image.
    The coefficients of f are given by coeffs, and the dimensions of the
    image are image_size.

    >>> _image_border_finding([680, 480], [1, 0])
    [(0, 0), (479, 479)]
    >>> _image_border_finding([680, 480],
     [-0.0012500000000000028, 1.2500000000000016, 0.0])
    [(0, 0), (679, 272)]
    >>> _image_border_finding([100, 100],
     [0.9999999999999996, 6.7974126728396205e-15])
    [(0, 0), (99, 99)]

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    intercepts = []
    max_x = image_size[0] - 1
    max_y = image_size[1] - 1

    y = polyval(coeffs, 0)
    if y is not None and (0 <= y <= max_y):
        left_border = (0, round(y))
        intercepts.append(left_border)

    y = polyval(coeffs, max_x)
    if y is not None and (0 <= y <= max_y):
        right_border = (max_x, round(y))
        intercepts.append(right_border)

    x = _exhaustive_search(max_x, coeffs, 0)
    if x is not None and (0 <= x <= max_x):
        top_border = (round(x), 0)
        intercepts.append(top_border)

    x = _exhaustive_search(max_x, coeffs, max_y)
    if x is not None and (0 <= x <= max_x):
        bottom_border = (round(x), max_y)
        intercepts.append(bottom_border)
    
    return sorted(list(set(intercepts)))


def draw_curve(image: Image, draw_colour: str, point_list: list = None) -> tuple:
    """
    Draws a curve on an image, image, of the colour, draw_colour. If a
    set of points isn't given with the optional parameter, point_list, the 
    user will be asked to input points. If two points are entered, a straight 
    line through the points will be drawn. If three points are entered, a 
    parabola through the points will be drawn. If four or more points are
    entered, a quadratic regression parabola of best fit through the points 
    will be drawn. The function returns the image and the points where the curve
    intersect with the border.

    >>> test_image = load_image("p2-original.png")

    >>> draw_curve(test_image, "cyan", [(0, 200), (400, 200)])
    The image is 640 pixels wide, and 480 pixels tall.
    Returns "p2-original.png" with a straight cyan line across the image.
    intercepts: [(0, 200), (639, 200)]

    >>> draw_curve(test_image, "blood", [(0, 0), (640, 0), (320, 200)])
    The image is 640 pixels wide, and 480 pixels tall.
    Returns "p2-original.png" with a red parabola across the image.
    intercepts: [(0, 0), (639, 1)]

    >>> draw_curve(test_image, "green", [(10, 10), (400, 200), (90, 90), (100, 400)])
    The image is 640 pixels wide, and 480 pixels tall.
    Returns "p2-original.png" with a green parabola across the image.
    intercepts: [(11, 0)]

    Team: T028
    Author: Jackie Smolkin-Lerner
    """

    COLOURS = [("black", (0, 0, 0)),
               ("white", (255, 255, 255)),
               ("blood", (255, 0, 0)),
               ("green", (0, 255, 0)),
               ("blue", (0, 0, 255)),
               ("lemon", (255, 255, 0)),
               ("aqua", (0, 255, 255)),
               ("pink", (255, 0, 255)),
               ("gray", (128, 128, 128))
               ]

    width = get_width(image)
    height = get_height(image)

    copied_image = copy(image)

    # Turn draw_colour into colour
    for colour_name, colour_values in COLOURS:
        if draw_colour == colour_name:
            r, g, b = colour_values
            colour = create_color(r, g, b)

    print("The image is", width, "pixels wide, and", height, "pixels tall.\n")

    # Get points from user
    while point_list is None or len(point_list) < 2:
        points = int(input("How many points would you like? " + \
                           "(Please pick at least 2 points)\n"))

        if points >= 2:
            for num in range(points):
                x = (int(input("Enter the x value of point " + str(num + 1) + "\n")))
                y = (int(input("Enter the y value of point " + str(num + 1) + "\n")))
                point_list.append((x, y))

    point_list = sort_points(point_list)

    # Create coefficients based off point_list
    coeffs = _interpolation(point_list)

    # Draw curve on image
    for x in range(width):
        y = round(polyval(coeffs, x))
        for num in range(-2, 3):
            if 0 <= (y + num) < get_height(copied_image):
                set_color(copied_image, x, y + num, colour)

    # Find border intercepts
    intercepts = _image_border_finding([width, height], coeffs)

    return copied_image, intercepts


# Function 7
def flip_horizontal(original_img: Image) -> Image:
    """
    Returns a copy of the inputed image that has a been flipped horizontaly, 
    along a verticle axis.
    
    >>> flip_horizontal(image_1)
    Returns a copy of image_1 flipped horizontally.
    
    Team: T028
    Author: Kaitlyn Myinia
    """

    new_pic = copy(original_img) # creates a copy of original image so as to not destroy it
    
    for pixel in original_img: # goes through every pixel in the image and applies a filter
        x, y, (r, g, b) = pixel
        rgb = create_color(r,g,b)
        # flips the image horizontaly by inverting x positions of the pixels
        set_color(new_pic, -x-1, y, rgb) 
    
    return new_pic    

    
# Function 8
def flip_vertical(original_img: Image) -> Image:
    """
    Takes an image and returns it with a vertical flip applied.
    Uses roll-over to move pixels from the top to the bottom, and vice versa.
    Goes through each line of pixels and puts it on the new images opposite line.
    
    >>> flip_vertical(image_1)
    Returns a copy of image_1 flipped vertically
    
    Team: T028
    Author: Keldan Simos
    """
    new_image = copy(original_img) # Copies the original image.
    
    for pixel in original_img: # Creates a pixel with RGB values for each pixel.
        x,y,(r,g,b)=pixel
        fl = create_color(r,g,b) # Creates a colour with the same rgb values as the selected pixel.
        # Applies to the same x component of the coordinate but the opposite y.
        set_color(new_image,x,-y - 1,fl)
          
    return new_image
