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

        while current != None:

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
        new_node = Node(val) 

        #for empty linkedlist
        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node
        new_node.next = None
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        #if index is 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        count = 0
        while(current != None):

            if count == index-1:
                break
            
            current = current.next
            count+=1

        #If the index exceeds then
        if current == None:
            return

        new_node.next = current.next
        current.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:

        #Empty List
        if self.head == None:
            return
        
        #Delete Head
        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        current = prev.next

        count = 0
        while(prev != None and current != None):

            if count == index-1:
                break
            
            prev = prev.next
            current = current.next

            count+=1

        #If index doesn't exits
        if current == None:
            return

        prev.next = current.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)