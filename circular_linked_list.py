class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def create_circular_linked_list():

    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    head.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = head
    return head


def check_loop(head):
    temp = head
    while head:
        if head.next:
            head = head.next
            if temp == head:
                print("Loop exists")
                break
            else:
                continue
        else:
            print("Loop does not exist")
            break


head = create_circular_linked_list()


check_loop(head)