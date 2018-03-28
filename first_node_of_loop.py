class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def create_circular_linked_list():

    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    return head


def check_loop(head):
    slow = head.next
    fast = slow.next
    while head:
        if slow == fast:
            print("Loop exists")
            return fast
        elif slow is None or fast is None:
            print("Loop does not exist")
            break
        else:
            slow = slow.next
            fast = fast.next.next


def get_first_node_of_loop(start, mid):
    while start:
        if start == mid:
            print("The data of the first node of the loop is " + str(mid.data))
            break
        else:
            start = start.next
            mid = mid.next


head = create_circular_linked_list()

a = check_loop(head)

get_first_node_of_loop(head, a)
