from coordinate import Coordinate

class Path():
    """An object wrapper for an array of Coordinate objects."""

    def __init__(self, path=[]):
        self.path = path

    def append(self, coordinate):
        """Append the Coordinate object to this path object.

        Args:
            coordinate: The object to be appended.
        """
        self.path.append(coordinate)

    def clone(self):
        """Make a cone of this Path object."""
        return Path(list(self.path))

    def last(self):
        """Get the Coordinate object that was last added.

        Returns:
            The last added Coordinate object.
        """
        return self.path[-1]

    def length(self):
        """Get the length of this Path object.

        Returns:
            The length of this Path object.
        """
        return len(self.path)

    def contains(self, coordinate):
        """Append the coordinate to this path object.

        Args:
            coordinate: The object to be appended.
        """
        for path_coordinate in self.path:
            if path_coordinate == coordinate:
                return True
        return False

    def count(self, coordinate):
        """Get the number of times the specified Coordinate object exists in this
           array.

        Args:
            coordinate: The Coordinate object.

        Returns:
            The number of times the Coordinate exists in this Path.
        """
        count = 0
        for path_coordinate in self.path:
            if path_coordinate == coordinate:
                count += 1
        return count

    def __str__(self):
        return '[{0}]'.format(' '.join([str(coordinate) for coordinate in self.path]))
