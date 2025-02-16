# Team: T028
# Authors:
# Jackie Smolkin-Lerner 101184457
# Kaitlyn Myinia 101192031

from Cimpl import *
from T028_user_interface import _run_filter


def batch_ui() -> None:
    """
    Filters and saves copies of images determined by a batch command file
    chosen via user input.

    >>> batch_ui()
    Please enter the name of the batch command file: batch_sample.txt
    Saves filtered images to the folder where batch_ui() is called.

    Team: T028
    Authors:
    Jackie Smolkin-Lerner
    Kaitlyn Myinia
    """

    filename = input("Please enter the name of the batch command file: ")
    command_list = _process_file(filename)

    for image_name, output_name, filters in command_list:
        image = copy(load_image(image_name))

        for image_filter in filters:
            image = _run_filter(image, image_filter)

        save_as(image, output_name)


def _process_file(filename: str) -> list:
    """
    Takes in a file name, filename, and returns a list of commands
    from filename.

    >>> _process_file("batch.txt")
    [['p2-original.png', 'test1.png', ('3', 'X', 'P')], ['p2-original.png', 'test2.png', ('V', 'H')]]

    Team: T028
    Authors:
    Jackie Smolkin-Lerner
    Kaitlyn Myinia
    """

    commands = []
    open_file = open(filename, "r")
    for line in open_file:
        line = line.split()
        commands.append(line[0:2] + [tuple(line[2:])])

    open_file.close()
    return commands


# Main Script
if __name__ == "__main__":
    batch_ui()
