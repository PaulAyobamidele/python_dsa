class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class dll(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def iter(self):

        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def reverse_iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.prev
            yield val

    def print_forward(self):

        for node in self.iter():
            print(node)

    def delete(self, data):
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False

        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = current.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count += 1


list = dll()
list.append("I")
list.append("Love")
list.append("Python")
list.print_forward()
