# Team: T028
# Authors:
# Khooshav Nikhil Bundhoo 101132063
# Keldan Simos 101184312
# Jackie Smolkin-Lerner 101184457
# Kaitlyn Myinia 101192031

from T028_image_filters import *


def _run_filter(image: Image, filter_key: str) -> Image:
    """
    Returns image with a filter applied to it determined by filter_key.
    The filter keys are: 3 for three_tone, X for extreme_contrast,
    T for sepia, P for posterize, E for detect_edges, V for flip_vertical,
    H for flip_horizontal


    >>> _run_filter(test_image, "T")
    Returns test_image with the sepia filter applied to it.
    >>> _run_filter(test_image, "P")
    Returns test_image with the posturize filter applied to it.
    >>> _run_filter(test_image, "V")
    Returns test_image with the flip_vertical filter applied to it.

    Team: T028
    Authors:
    Jackie Smolkin-Lerner
    Kaitlyn Myinia
    """

    FILTERS = {"3": three_tone,
               "X": extreme_contrast,
               "T": sepia,
               'P': posterize,
               'E': detect_edges,
               "V": flip_vertical,
               "H": flip_horizontal
               }

    if filter_key == "3":
        filter_function = FILTERS[filter_key]
        return filter_function(image, "aqua", "blood", "lemon")

    elif filter_key == "E":
        filter_function = FILTERS[filter_key]
        return filter_function(image, 15)

    elif filter_key in FILTERS.keys():
        filter_function = FILTERS[filter_key]
        return filter_function(image)
