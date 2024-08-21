class Door:
    def __init__(self, ref2door_lock, base_color):
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        self._door_is_open = False

    def lock_the_door(self):
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()

    def test(self):
        print(f'Door color: {self.color}, '
              f'Door open: {self._door_is_open}, '
              f'Door locked: {self._door_is_locked}')

    @property
    def door_is_open(self):
        return self._door_is_open

    @property
    def door_is_locked(self):
        return self._door_is_locked

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color


class DoorLock:
    def __init__(self):
        print("A lock has been created")

    def lock(self):
        return True

    def unlock(self):
        return False


if __name__ == "__main__":
    print("Test for Door object")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "green")
    the_door.test()
    print("-- Open the door")
    the_door.open_the_door()
    the_door.test()