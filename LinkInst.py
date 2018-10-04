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
      def prepend(self,data):
            newNode=Node(data)
            
            newNode.next=self.head
            self.head=newNode
      def insertAtPosition(self,data,data1):
            newNode=Node(data)
            nextNode=self.head
            while nextNode.data!=data1:
                  nextNode=nextNode.next
            newNode.next=nextNode.next
            nextNode.next=newNode
      def deleteNode(self,key):
            prev=None
            currentNode=self.head
            if currentNode and currentNode.data==key:
                  self.head=currentNode.next
                  currentNode=None
            while(currentNode and currentNode.data!=key):
                  prev=currentNode
                  currentNode=currentNode.next
            if currentNode==None:
                  return
            prev.next=currentNode.next
            currentNode=None
      def deleteAtPosition(self,position):
            current=self.head
            prev=None
            if position==0:
                  self.head=current.next
                  current=None
            c=0
            l=0
            while(current):
                  l+=1
                  current=current.next
            print l
            if position<l:
                  current=self.head
                  while(current):
                        c+=1
                        prev=current
                        current=current.next
                        if position==c:
                              prev.next=current.next
                              current=None
                              break
            else:
                    return
                    
                  
            

      def printList(self):
            curNode=self.head
            l=0
            while curNode:
                  l+=1
                  print(curNode.data)
                  curNode=curNode.next
            #print l
            
            
lList=LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")
#lList.deleteNode("C")
lList.insertAtPosition("1","B")
lList.deleteAtPosition(3)

#lList.append("2")
#lList.prepend("1")
#lList.prepend("5")
lList.printList()
                  
