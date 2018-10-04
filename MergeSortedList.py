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
      def deletelastNode(self):
            current=self.head
            while current.next.next:
                  current=current.next
            current.next=None
            
      def merge(self,lList,lList1):
            p=lList.head
            q=lList1.head
            while p:
                  p=p.next
            
            lList.append(11010000000087)
            while q:
                  q=q.next
            
            lList1.append(11010000000076587)
            p=lList.head
            q=lList1.head
            
            while p and q:
                  if p.data<q.data:
                        lList2.append(p.data)
                        p=p.next
                  else:
                        lList2.append(q.data)
                        q=q.next
            lList2.deletelastNode()
                       
lList=LinkedList()
lList.append(1)
lList.append(5)
lList.append(7)
lList.append(9)
lList.append(10)
print"First list"
lList.printList()
lList1=LinkedList()
lList1.append(2)
lList1.append(3)
lList1.append(4)
lList1.append(6)
lList1.append(8)
print"Second List"
lList1.printList()
print"After Merging"
lList2=LinkedList()
lList2.merge(lList,lList1)
lList2.printList()



