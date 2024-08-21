"""Module for Door and DoorLock classes"""


class Door:
    """A class representing a door with a lock."""

    def __init__(self, ref2door_lock, base_color):
        """Initialize a Door object.

        Args:
          ref2door_lock (DoorLock): A reference to a DoorLock object.
          base_color (str): The color of the door.
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """Open the door if it's not locked."""
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """Close the door."""
        self._door_is_open = False

    def lock_the_door(self):
        """Lock the door if it's closed."""
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """Unlock the door if it's locked."""
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()

    def test(self):
        """Print the state of the door."""
        print(f'Door color: {self.color}, '
              f'Door open: {self._door_is_open}, '
              f'Door locked: {self._door_is_locked}')

    @property
    def door_is_open(self):
        """Check if the door is open."""
        return self._door_is_open

    @property
    def door_is_locked(self):
        """Check if the door is locked."""
        return self._door_is_locked

    @property
    def color(self):
        """Get the color of the door."""
        return self._color

    @color.setter
    def color(self, new_color):
        """Set a new color for the door."""
        self._color = new_color


class DoorLock:
    """A class representing a door lock."""

    def __init__(self):
        """Initialize a DoorLock object."""
        print("A lock has been created")

    def lock(self):
        """Lock the door.

        Returns:
          bool: True if the door is locked.
        """
        return True

    def unlock(self):
        """Unlock the door.

        Returns:
          bool: False if the door is unlocked.
        """
        return False


if __name__ == "__main__":
    print("Test for Door object")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "green")
    the_door.test()
    print("-- Open the door")
    the_door.open_the_door()
    the_door.test()
