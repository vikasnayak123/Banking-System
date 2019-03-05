from ll import LinkedList
class ListNode:
	def __init__(self,k):
		self.date
		self.particulars
		self.cheqno
		self.withdrawal
		self.deposit
		self.next


class Queue:
	
	def __init__(self):
		self.front=None
		self.rear=None
		self.l=[]

	"""def toFile(self,date,parti,trans,amt,bal):
		file=open("Bank.txt","w")
		file.write("\n Date:")
		file.write("date")
		file.write("\n Particulars :")
		file.write("parti")
		if trans=="deposite":
			file.write("\n Deposite :")
			file.write("amt")
		else:
			file.write("\n withdrawal :")
			file.write("amt")

		file.write("\n Balance:")
		file.write("bal")"""

	def enqueue(self,date,parti,trans,bal):

		list sam=[date,parti,trans,bal]
		if self.front==self.rear:
			self.front=0
			self.rear=0
			self.l[self.front]=sam
			#l[front+1]=[" "]
			self.front=self.front+1
		


	def dequeue(self):
		if self.isEmpty==True:
			#empty transcation

		else:
			while self.rare!=len(self.l)+1:
				print(self.l[rear])
				self.rear=self.rare+1

			self.front=None
			self.rare=None

	def isEmpty(self):
		if self.front =None and self.rare=None:
			return True-

		

	
