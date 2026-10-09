class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:

        current = self.head

        count = 0

        while(current != None):
            if count == index:
                return current.value
            count += 1
            current = current.next

        return -1


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        current = self.head
        new_node = Node(val)

        if current == None:
            self.head = new_node
            return 

        while(current.next != None):
            current = current.next

        current.next = new_node
        new_node.next = None

    def addAtIndex(self, index: int, val: int) -> None:

        current = self.head

        count = 0
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        while(current != None):
            if count == index-1:
                break
            current = current.next
            count += 1

        if current == None:
            return 

        new_node.next = current.next
        current.next = new_node   

    def deleteAtIndex(self, index: int) -> None:
        current = self.head

        if current == None:
            return

        count = 0

        if index == 0:
            self.head = current.next
            return

        while(current != None):
            if count == index-1:
                break
            current = current.next
            count += 1

        if current == None:
            return
        if current.next == None:
            return  

        current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)