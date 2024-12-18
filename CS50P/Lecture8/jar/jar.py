class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if capacity < 0 or capacity.is_integer() == False:
            raise ValueError("Invalid Capacity")
        self._size = 0

    def __str__(self):
        if self._size > 0:
            return "🍪" * self._size
        else:
            return ""

    def deposit(self, n):
        if n + self._size > self.capacity:
            raise ValueError("Deposit Overflow")
        elif n < 0:
            raise ValueError("Deposit Underflow")
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Withdraw Underflow")
        elif n > self._size:
            raise ValueError("Withdraw Overflow")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or capacity.is_integer() == False:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def setter(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("Invalid Size")
        self._size = size

