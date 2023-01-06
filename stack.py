class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# Create a stack object
stack = Stack()

# Push characters onto the stack
stack.push('a')
stack.push('b')
stack.push('c')

# Print the stack
print(stack.items)  # Output: ['a', 'b', 'c']

# Pop a character from the stack
item = stack.pop()
print(item)  # Output: 'c'
print(stack.items)  # Output: ['a', 'b']
