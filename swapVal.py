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
      def swap(self,key1,key2):
            p=self.head
            q=self.head
            prev1=None
            prev2=None
            while p and p.data!=key1:
                  prev1=p
                  p=p.next
            while q and q.data!=key2:
                  prev2=q
                  q=q.next
                  
            if not p or not q:
                 return
            if prev1:
                 prev1.next=q
            else:
                 self.head=q
            if prev2:
                 prev2.next=p
            else:
                 self.head=p
            p.next,q.next=q.next,p.next
           
            
            
            
                  
lList=LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")
lList.printList()
lList.swap("B","C")
lList.printList()
