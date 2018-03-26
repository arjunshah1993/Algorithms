class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list():

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    return node1


def rev_list():
    node4 = create_linked_list()
    while node4:
        node4 = node4.next


rev_list()
