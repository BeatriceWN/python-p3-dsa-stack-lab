class Stack:
    def __init__(self, items=None, limit=100):
        """Create a new stack with optional initial items and optional limit."""
        self.items = list(items) if items else []
        self.limit = limit

    def isEmpty(self):
        """Return True if stack is empty, False otherwise."""
        return len(self.items) == 0

    def push(self, item):
        """Add item to top of stack. Raise error if stack is full."""
        if self.full():
            return 
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Return None if stack is empty."""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Return None if empty."""
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """Return number of items currently in the stack."""
        return len(self.items)

    def full(self):
        """Return True if stack has reached its limit, False otherwise."""
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Return distance from top of stack to target.
        Top element has distance 1. Return -1 if not found.
        """
        try:
            return len(self.items) - self.items.index(target) - 1 
        except ValueError:
            return -1