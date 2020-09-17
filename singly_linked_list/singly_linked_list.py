class Node:
    def __init__(self, value = None, next_node = None):
        # value that the node is holding
        self.value = value
        # reference to the next node in the chain
        self.next_node = next_node

    def get_value(self):
        """
        Method to get the value of the node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the Linked List is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the last node's "next_node" to the new node
            self.tail.set_next(new_node) # (last node in chain).next_node = new_node
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    # Check to see if value is in the Linked List
    def contains(self, value):
        if self.head is None and self.tail is None:
            return False

        # Assign current to head
        current = self.head

        # loop until current is not equal to None
        while current != None:
            if current.get_value() == value:
                # value found
                return True

            current = current.get_next()

        # value not found
        return False

    def remove_head(self):
        # there is no item/Node in Linked List
        if self.head is None and self.tail is None:
            return None

        # Only one item/Node in Linked List
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            # set the head and tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        else:
            # store the old head's value
            value = self.head.get_value()
            # set self.head to old head's next
            self.head = self.head.get_next()
            # return the value
            return value

    def get_max(self):
        # check if there is an item in the List
        if self.head is None and self.tail is None:
            return None
        else:
            # set current node as head
            current = self.head
            # get value of current node
            max_value = current.get_value()
            # loop to find max value in list
            while current:
                # if current value is less than max value of next node
                if current.get_value() > max_value:
                    # set max value of that node
                    max_value = current.get_value()
                # look for next node
                current = current.get_next()
            return max_value