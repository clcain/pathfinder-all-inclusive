class Coordinate():
    """An object wrapper for a 2D coordinate tuple."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def north(self):
        """Get the Coordinate object that would be North of this object.

        Returns:
            The North Coordinate object.
        """
        return Coordinate(self.x, self.y + 1)

    def south(self):
        """Get the Coordinate object that would be South of this object.

        Returns:
            The South Coordinate object.
        """
        return Coordinate(self.x, self.y - 1)

    def east(self):
        """Get the Coordinate object that would be East of this object.

        Returns:
            The East Coordinate object.
        """
        return Coordinate(self.x + 1, self.y)

    def west(self):
        """Get the Coordinate object that would be West of this object.

        Returns:
            The West Coordinate object.
        """
        return Coordinate(self.x - 1, self.y)

    def get_surrounding(self):
        """Get all surrounding Coordinate objects.

        Returns:
            A list of surrounding Coordinate objects.
        """
        return [self.north(), self.south(), self.east(), self.west()]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)

class PathFinder():
    """An object supporting path generation abilities."""

    def __init__(self):
        self.paths = []
        self.available_coordinates = []
        self.duplicate_allowed_coordinates = []
        self.duplicate_allowed_limit = 0
        self.must_contain_all_available = False

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

        surrounding = path.last.get_surrounding()
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
        return ((self.allow_duplicate(coordinate) and not
                (path.count(coordinate) < self.duplicate_allowed_limit)) or not
                path.contains(coordinate))

    def allow_duplicate(self, coordinate):
        """Check if the Coordinate is allowed to be a duplicate.

        Args:
            coordinate: The Coordinate in question.

        Returns:
            A boolean indicating whether or not this Coordinate object is
            allowed to be a duplicate.
        """
        return self.duplicate_allowed.contains(coordinate)

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
           to this PathFinder.

        Args:
            path: The Path in question.

        Returns:
            A boolean indicating whether or not the specified Path
            contains at least one instance all available Coordinate objects.
        """
        for available_coordinate in self.available_coordinates:
            if not path.contains(available_coordinate):
                return False
        return True

    def __str__(self):
        return '\n'.join([str(path) for path in self.paths])
