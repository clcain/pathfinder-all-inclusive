#! /usr/bin/python

from coordinate import Coordinate
from path import Path
from pathfinder import PathFinder

def main():
    main_square = PathFinder.get_all_coordinates_within_bounds(0, 0, 4, 4)
    lower_row = PathFinder.get_all_coordinates_within_bounds(1, -1, 3, -1)
    upper_row = PathFinder.get_all_coordinates_within_bounds(1, 5, 3, 5)
    available_coordinates = main_square + lower_row + upper_row
    duplicate_allowed_coordinates = lower_row + upper_row
    pf = PathFinder(available_coordinates,
                       duplicate_allowed_coordinates,
                       3, True,
                       main_square)
    pf.generate_paths(Coordinate(2, 0), Coordinate(2,4))
    print pf.get_shortest_path()

if __name__: main()
