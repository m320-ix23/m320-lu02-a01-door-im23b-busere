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

