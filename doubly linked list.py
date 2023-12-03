if __name__ == "__main__":
    pass

#Programmer: Jack Flickinger
#Date: 2/3/2022
#Doubly Link List

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newprevious):
        self.previous = newprevious


class doublyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        if self.head == None:
            n = Node(item)
            n.setNext(n)
            n.setPrevious(n)
            self.head = n
        else:
            current = self.head
            n = Node(item)
            n.setPrevious(current)
            current.setPrevious(n)
            n.setNext(current)
            self.head = n
        self.len += 1

    def size(self):
        return self.len

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if current == self:
            self.head = None
            self.len = 0
        else:
            current.getPrevious().setNext(current.getNext())
            current.getNext().setPrevious(current.getPrevious())
            self.len -= 1


    def append(self, item):
        n = Node(item)
        current = self.head
        n.setPrevious(current.getPrevious())
        current.getPrevious().setNext(n)
        current.setPrevious(n)
        n.setNext(current)
        self.head = current
        self.len += 1

    # inserts item at position pos
    def insert(self, pos, item):
        n = Node(item)
        current = self.head
        i = pos
        while i > 0:
            current = current.getNext()
            i -= 1
        n.setPrevious(current.getPrevious())
        current.getPrevious().setNext(n)
        current.setPrevious(n)
        n.setNext(current)
        self.len += 1

    # returns a string representation of all items in the list
    def __str__(self):
        string = "["
        current = self.head
        check = 0
        while check != self.len:
            if check + 1 == self.len:
                string = string + str(current.getData())
                check +=1
            else:
                string = string + str(current.getData()) + ","
                check+=1
            current = current.getNext()
        string = string + "]"
        return string

    # returns the index or position of item, assume item is in list
    def index(self, item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count += 1
                current = current.getNext()

        print(count)

    # removes and returns the last item on the list
    def pop(self):
        current = self.head
        previous = current.getPrevious()
        current.getPrevious().getPrevious().setNext(current)
        current.setPrevious(current.getPrevious().getPrevious())
        self.len -= 1
        return previous.getData()

    def popPos(self, pos):
        current = self.head
        i = pos
        while i > 0:
            current = current.getNext()
            i -= 1

        current.getPrevious().setNext(current.getNext())
        current.getNext().setPrevious(current.getPrevious())
        self.len -= 1
        return current.getData()

