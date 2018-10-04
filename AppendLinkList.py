class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class LinkedList:
      def __init__(self):
            self.head=None
      def append(self,data):
            newNode=Node(data)
            if self.head is None:
                  self.head=newNode
                  return
            lastNode=self.head
            while lastNode.next:
                  lastNode=lastNode.next
            lastNode.next=newNode
      def printList(self):
            curNode=self.head
            while curNode:
                  print(curNode.data)
                  curNode=curNode.next
lList=LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")
lList.printList()
