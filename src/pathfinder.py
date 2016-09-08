from coordinate import Coordinate
from path import Path

class PathFinder():
    """An object supporting path generation abilities."""

    def __init__(self, available_coordinates=[], duplicate_allowed_coordinates=[],
                 duplicate_allowed_limit=0, must_contain_all_available=False,
                 required_coordinates=[]):
        self.available_coordinates = Path(available_coordinates)
        self.duplicate_allowed_coordinates = Path(duplicate_allowed_coordinates)
        self.duplicate_allowed_limit = duplicate_allowed_limit
        self.must_contain_all_available = must_contain_all_available
        self.required_coordinates = Path(required_coordinates)
        self.paths = []

    def generate_paths(self, start, goal):
        """Begin generation of all paths beginning at the start
           and ending at the goal.

        Args:
            start: The beginning Coordinate.
            goal: The ending Coordinate.
        """

        self.goal = goal
        path = Path()
        path.append(start)
        self._generate_paths(path)

    def _generate_paths(self, path):
        if path.last() == self.goal:
            if self.all_contained(path) or not self.must_contain_all_available:
                self.paths.append(path)
            return

        surrounding = path.last().get_surrounding()
        for coordinate in surrounding:
            if self.valid_coordinate(coordinate) and self.non_duplicate(path, coordinate):
                new_path = path.clone()
                new_path.append(coordinate)
                self._generate_paths(new_path)

    def non_duplicate(self, path, coordinate):
        """Check if addition of a new Coordinate is not constained by prior
           existance in the Path.

        Args:
            path: The current Path.
            coordinate: The prospective Coordinate.

        Returns:
            A boolean indicating whether or not this Coordinate object may be added.
        """
        return ((self.allow_duplicate(coordinate) and
                not (path.count(coordinate) <= self.duplicate_allowed_limit)) or
                not path.contains(coordinate))

    def allow_duplicate(self, coordinate):
        """Check if the Coordinate is allowed to be a duplicate.

        Args:
            coordinate: The Coordinate in question.

        Returns:
            A boolean indicating whether or not this Coordinate object is
            allowed to be a duplicate.
        """
        return self.duplicate_allowed_coordinates.contains(coordinate)

    def valid_coordinate(self, coordinate):
        """Check is the Coordinate has valid coordinates.

        Args:
            coordinate: The Coordinate in question.

        Returns:
            A boolean indicating whether or not the Coordinate
            has valid coordinates.
        """
        return self.available_coordinates.contains(coordinate)

    def all_contained(self, path):
        """Check if the specified path contains all coordinates available
           to this PathFinder

        Args:
            path: The Path in question.

        Returns:
            A boolean indicating whether or not the specified Path
            contains at least one instance all available Coordinate objects.
        """
        for required_coordinate in self.required_coordinates.path:
            if not path.contains(required_coordinate):
                return False
        return True

    def get_all_paths(self):
        return '\n'.join([str(path) for path in self.paths])

    def get_shortest_path(self):
        if not self.paths:
            return None
        shortest_path = self.paths[0]
        shortest_length = shortest_path.length()
        for path in self.paths:
            path_length = path.length()
            if path_length < shortest_length:
                shortest_length = path_length
                shortest_path = path
        return shortest_path

    @staticmethod
    def get_all_coordinates_within_bounds(x_min, y_min, x_max, y_max):
        coordinates = []
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                coordinates.append(Coordinate(x, y))
        return coordinates
