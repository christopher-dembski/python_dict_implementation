class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class _LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def __iter__(self):
        return _LinkedListIterator(self.head)

    def __repr__(self):
        result = 'LinkedList('
        current = self.head
        while current is not None:
            result += f'{current.value}'
            if current.next is not None:
                result += ' -> '
            current = current.next
        result += ')'
        return result


if __name__ == '__main__':
    ll = LinkedList()
    ll.add('a')
    ll.add('b')
    ll.add('c')
    print(ll)
    for item in ll:
        print(item)
