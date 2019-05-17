class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       current=self.head
       c=0
       while current!=None:
           c=c+1
           current=current.getNextNode()
       return c

   def addNodeB(self,data):
       newNode = Node(data,self.head)
       self.head = newNode

   def addNodeEnd(self,data):
      temp=Node(data)
      if self.head is None:
         self.head=temp
      else:
         curr=self.head
         while curr.nextNode!= None:
            curr=curr.getNextNode()
         curr.setNextNode(temp)
      myList.printNode()

   def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNextNode()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNextNode()
        else:
            previous.setNextNode(current.getNextNode())

            
   def deleteb(self):
       temp=self.head
       self.head=temp.getNextNode()
       temp=None

   def deleteEnd(self):
       current=self.head
       while current.nextNode!=None:
           previous=current
           current=current.getNextNode()
       previous.setNextNode(None)
       
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.getData(), end=' ')
           curr=curr.getNextNode()
       print("None")

myList = LinkedList()
n=0
while n!=8:
   print("\t\t LINK LIST IMPLEMENTATION\t\t\n1.Insertion at Begining\n2.Insertion at End\n3.Insertion at Middle\n4.Display the List\n5.Delete at Begining\n6.Deletion at Middle\n7.Deletion at End\n8.Quit\n")
   n=int(input())
   if n==1:
      print("Enter value to be inserted")
      val=input()
      myList.addNodeB(val)
      myList.printNode()
   elif n==2:
      print("Enter value to be inserted")
      val=input()
      myList.addNodeEnd(val)
      myList.printNode
   elif n==4:
      myList.printNode()
   elif n==5:
      myList.deleteb()
      myList.printNode()
   elif n==6:
      print("Enter the value to be Deleted")
      val=input()
      myList.delete(val)
      myList.printNode()
   elif n==7:
      myList.deleteEnd()
      myList.printNode()
   else:
      break
   
   
      



'''print("Inserting")
myList.addNode(int(input()))
myList.addNode(15)
myList.addNode(25)
myList.addNode(10)
myList.printNode()
myList.delete(15)
myList.printNode()
myList.deleteb()
myList.printNode()
myList.deleteEnd()
myList.printNode()
print("\nSize")
print(myList.getSize())'''
