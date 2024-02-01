from typing import List


class LinkNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = LinkNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while i < index and cur:
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values

if __name__=="__main__":
    llist = LinkedList()
    # ["insertTail", 1, "insertTail", 2, "get", 1, "remove", 1, "insertTail", 2, "get", 1, "get", 0]
    llist.insertTail(1)
    llist.insertTail(2)
    print(llist.get(1))
    print(llist.remove(1))
    llist.insertTail(2)
    print(llist.getValues())
    llist.get(1)
    llist.get(0)

