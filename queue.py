


class Queue:
    def __init__(self, mode='FIFO'):
        assert mode in ['FIFO', 'LIFO', 'PRIO'], "Mode must be 'FIFO', 'LIFO', or 'PRIO'"
        self.mode = mode
        self.items = []

    def push(self, item):
        if self.mode in ['FIFO', 'LIFO']:
            self.items.append(item)
        elif self.mode == 'PRIO':
            self.items.append(item)
            self.items.sort(key=lambda x: x.value)

    def pop(self):
        if self.is_empty():
            return None
        if self.mode == 'FIFO':
            return self.items.pop(0)
        elif self.mode == 'LIFO':
            return self.items.pop()
        elif self.mode == 'PRIO':
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0