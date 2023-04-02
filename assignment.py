class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.data=next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head= node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr=self.head
        llstr = ''

        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    ll.print()