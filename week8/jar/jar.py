class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.count = 0

    def __str__(self):
        return "🍪" * self.count

    def deposit(self, n):
        if self.capacity < self.count + n:
            raise ValueError
        self.count = self.count + n

    def withdraw(self, n):
        if self.count < n:
            raise ValueError
        self.count = self.count - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.count
