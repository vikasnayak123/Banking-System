class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,x,pos):
        temp=ListNode(x)
        temp.next=pos.next
        pos.next=temp

    def delete(self,pos):
        pos.next=pos.next.next

    """def print(self):
        p=self.head.next
        if(p==None):
           print("List is empty")
        while p is not None:
           print(p.value)
           p=p.next
        print()"""

    def insertAtIndex(self,x,i):
        if(i==0):
           self.insert(x,self.head)
           return
        p=self.head
        while (i is not 0 and p is not None):
           p=p.next
           i=i-1
        self.insert(x,p)

    def search(self, x):
        p=self.head.next
        while p is not None :
            if(p.value==x):
                 temp=p
                 return temp
            p=p.next
        return None

    def len(self):
        c=0
        p=self.head
        while p is not None:
           c=c+1
           p=p.next
        return (c-1)

    def isEmpty(self):
        if (self.head.next==None):
            return True
        else:
            return False