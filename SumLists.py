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
      def sumList(self,lList,lList1):
            p=lList.head
            q=lList1.head
            s=0
            s1=0
            s2=0
            while p:
                  s1=s1*10+(p.data)
                  s2=s2*10+(q.data)
                  p=p.next
                  q=q.next

            print s1+s2
            
            
            
      
            
      def printList(self):
            curNode=self.head
            while curNode:
                  print(curNode.data)
                  curNode=curNode.next
lList=LinkedList()
lList.append(1)
lList.append(5)
lList.append(7)
lList.append(9)
lList.printList()
lList1=LinkedList()
lList1.append(2)
lList1.append(3)
lList1.append(4)
lList1.append(6)
lList1.printList()
lList2=LinkedList()
lList2.sumList(lList,lList1)




