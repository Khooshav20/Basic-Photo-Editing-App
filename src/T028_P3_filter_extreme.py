#T028
#Bundhoo Khooshav Nikhil 101132063


from Cimpl import *

def extreme_contrast(original_image: Image) -> Image:
    """
    Returns a copy of an image in which the contrast between the pixels has been maximised

    >>>extreme_constrast(image1)
    returns a copy of image1 in which the RGB components of each pixel is set to their minimum or maximum values to maximuse the contrast
    
    
    #T028
    #Author: Bundhoo Khooshav Nikhil 
    #101132063
    
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

#Main Script
if __name__ == "__main__":
    #original_image = load_image(input('Enter the name of an image to pass through extreme_contrast(): '))

    print('Choose an image to pass through extreme_contrast()')
    original_image = load_image(choose_file())

    extreme_contrast_image  = extreme_contrast(original_image)
    show(extreme_contrast_image)

