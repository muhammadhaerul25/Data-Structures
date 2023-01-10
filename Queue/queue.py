class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

# Create a queue object
queue = Queue()

# Enqueue items onto the queue
queue.enqueue('item1')
queue.enqueue('item2')
queue.enqueue('item3')

# Print the queue
print(queue.items)  # Output: ['item1', 'item2', 'item3']

# Dequeue an item from the front of the queue
item = queue.dequeue()
print(item)  # Output: 'item1'
print(queue.items)  # Output: ['item2', 'item3']
