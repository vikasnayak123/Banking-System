def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
class Queue:
	
	def __init__(self):
		self.front=-1
		self.rear=-1
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
	def show(self):
		print(self.l)

	def enqueue(self,date,trans,amt,bal):

		sam=[date,trans,amt,bal]
		#print(sam)
		if self.front==-1 and self.rear==-1:
			self.rear=0
		self.l.append(sam)
			#l[front+1]=[" "]
		self.front=self.front+1


	def dequeue(self):
		if self.isEmpty==True:
			prPurple("*****No transactions to print*****")
			return self.balance
		k=(self.l[self.front-1][3])
		while self.rear!=-1:
			if self.front==self.rear:
				self.front=-1
				self.rear=-1
			else:
				self.rear=self.rear+1
			print(self.l[self.rear][0],"     ",self.l[self.rear][1],"        ",self.l[self.rear][2],"      ",self.l[self.rear][3])
		return k

	def isEmpty(self):
		if self.front ==-1 and self.rear==-1:
			return True
		return False

def main():
	print("hi")
	q=Queue()
	q.enqueue(1,2,3,4)
	q.enqueue(11,22,33,44)
	q.enqueue(111,222,333,444)
	#print(q.l)
	print(q.dequeue())
	#print("!!!!")

if __name__ == '__main__':
	main()