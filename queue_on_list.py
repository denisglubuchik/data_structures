class Node(object):
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Queue(object):
    def __init__(self) -> None:
        self.size = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.head.next == self.tail:
            return
        
        elem = self.tail.prev
        
        elem.prev.next = self.tail
        self.tail.prev = elem.prev
        elem.next = None
        elem.prev = None
        self.size -= 1

        return elem.data
    
    def print_queue(self):
        curr = self.tail.prev
        while curr.prev:
            print(curr.data, end = ' ')
            curr = curr.prev
        print()

a = Queue()
a.push(2)
a.push(1)
a.push(5)
a.push(7)
a.push(3)
a.print_queue()
a.pop()
a.pop()
a.print_queue()
a.push(9)
a.print_queue()
