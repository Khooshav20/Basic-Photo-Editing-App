# Team: T028
# Authors:
# Khooshav Nikhil Bundhoo 101132063
# Keldan Simos 101184312

from Cimpl import save_as
from T028_user_interface import _run_filter
from T028_image_filters import *


def interactive_ui() -> None:
    """
    Takes user inputs and which corresponds to the appropriate filter
    Filters can be layered on top of one another
    Image needs to be loaded before an image can be passed through a filter
    Final image can be saved to computer
    
    >>>text_based()
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>3 
    no image selected
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>L 
    #prompts user to chose file on computer in pop-up
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>K
    no such command
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>V 
    #shows vertically flipped image 
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>X 
    #shows vertically image with extreme contrast filter
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>S 
    #Prompts user to chose a location to save the file 
    
    L)oad image  S)ave-as 
    3)-tone  X)treme contrast  T)int sepia  P)osterize 
    E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip
    Q)uit
    >>>q
    Quitting
    #ends program 

    Team: T028
    Authors:
    Khooshav Nikhil Bundhoo
    Keldan Simos
    """

    command, img = None, None

    while command != "Q":
        command = input("L)oad image  S)ave-as \n3)-tone  X)treme contrast  "
                        + "T)int sepia  P)osterize \nE)dge detect  D)raw curve  "
                        + "V)ertical flip  H)orizontal flip\nQ)uit\n\n: "
                        )
        command = command.upper()
        if command != "Q":
            if command in ("L", "S", "3", "X", "T", "P", "E", "D", "V", "H"):
                if command == "L":
                    img = load_image(choose_file())

                elif command == "S":
                    save_as(img)

                elif img:
                    if command == "E":
                        threshold = int(input("Threshold?: "))
                        img = detect_edges(img, threshold)
                        show(img)

                    elif command == "D":
                        img = draw_curve(img, "lemon")[0]
                        show(img)

                    else:
                        img = _run_filter(img, command)
                        show(img)

                else:
                    print("No image selected\n")

            else:
                print("No such command\n")
        
        else:
            print("Qutting")

# Main Script
if __name__ == "__main__":
    interactive_ui()
