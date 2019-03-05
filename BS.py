from linked_list import LinkedList
from queue import Queue
import datetime
import random
import pickle

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 


stint=0
def h(v):
	return int(v)%23

class hashtable:
    def __init__(self):
        self.T=[None for i in range(0,23)]


    def frmfile(self):
        acc=open("account_no.txt","r")
        pss=open("Password.txt","r")
        na=open("names.txt","r")
        a1=acc.readlines()
        p1=pss.readlines()
        n1=na.readlines()
        a1=[x.strip() for x in a1]
        p1=[x.strip() for x in p1]
        n1=[x.strip() for x in n1]
        #print(a1)
        #print(p1)
        #print(n1)
        count=1
        for i in range (0,len(a1)):
            node=ListNodell(int(a1[i]))
            node.password=p1[i]
            node.name=n1[i]
            t=open("%s.txt" %n1[i],"rb")
            
            while True:
                try:
                    value = pickle.load(t)
                    #print(value)
                    #node.qu.l.append(value)
                    node.balance=int(value[3])
                    #print(node.qu.l)
                except EOFError:
                    #print("Pickle ends")
                    break
            
        
            self.chained_insert(a1[i],node)
            
            

    def chained_insert(self,a,ln):
        k=h(a)

        if(self.T[k]==None):
            self.T[k]=LinkedList()
            self.T[k].head=ln
            #print(self.T[k].head.key)
        else:
            ln.next=self.T[k].head
            self.T[k].head=ln

    def chained_search(self,a):
        k=h(a)
        if(self.T[k]==None):
            print(self.T[k])
            return False
        else:
            p=self.T[k].head
            while(p is not None):
                if(a==p.key):
                    return p
                #print(p.password)
                p=p.next
            return False

    def chained_delete(self,a):
        k=h(a)
        p=self.T[k].head
        a1=self.chained_search(a)
        if a1==False:
            prYellow("***** No account exists with the given A/C number *****")
            return
        if p.next==None:
            self.T[k]=None
        else:
            p.delete(a1)

        #self.show()

        acc=open("account_no.txt","r")
        pss=open("Password.txt","r")
        na=open("names.txt","r")
        a1=acc.readlines()
        p1=pss.readlines()
        n1=na.readlines()
        a1=[x.strip() for x in a1]
        p1=[x.strip() for x in p1]
        n1=[x.strip() for x in n1]

        a2=open("a3.txt","w")
        p2=open("p3.txt","w")
        n2=open("n3.txt","w")



        for i in range(0,len(a1)):

            if(int(a1[i])!=a):
                #print(a1[i])
                a2.write(a1[i])
                a2.write("\n")
                p2.write(p1[i])
                p2.write("\n")
                n2.write(n1[i])
                n2.write("\n")

        a2=open("a3.txt","r")
        p2=open("p3.txt","r")
        n2=open("n3.txt","r")

        acc=open("account_no.txt","w")
        pss=open("Password.txt","w")
        na=open("names.txt","w")

        acc.writelines(a2.readlines())
        pss.writelines(p2.readlines())
        na.writelines(n2.readlines())
        prRed("----------Your A/C is successfully 'Deleted'----------")






        
                

    def createAC(self):
        #global stint
        stint=random.randrange(10000,99999)
        newNode=ListNodell(stint)
        print("Your account number is :  ",stint)
        newNode.name=input("Enter the account holders name : ")
        newNode.Address=input("Enter the Address of the account holder : ")
        newNode.phno=int(input("Enter the phone number account holder : "))

        #writing to file
        acc_no=open("account_no.txt","a+")
        acc_no.write("%d" %stint)
        acc_no.write("\n")

        name=open("names.txt","a+")
        name.write("%s" %newNode.name)
        name.write("\n")

        ph_no=open("phone_no.txt","a+")
        ph_no.write("%d" %newNode.phno)
        ph_no.write("\n")

        addr=open("Address.txt","a+")
        addr.write("%s" %newNode.Address)
        addr.write("\n")

        #trans=open("%s.txt"%newNode.name,"w")
        #trans.write(["0","0","0","0"])
        trans=open("%s.txt"%newNode.name,"wb")
        pickle.dump([0,0,0,0],trans)

        self.chained_insert(stint,newNode)
        self.acc_pass(stint)

       #psswrd=open("Password.txt","a+")
        #psswrd.write("%s \n" %newNode.password)

    def show(self):
        for i in range(0,len(self.T)):
            if self.T[i]!=None:
                self.T[i].print()
                #print(self.T[i].key)

    def transactions(self,k):
        x=int(input("Enter 1 to withdraw and 2 to deposite : "))
        date = datetime.datetime.now()
        date=date.strftime("%Y-%m-%d %H:%M")
        account=self.chained_search(k)
        if x==1 :
            #print("Please deposite amount..!")
            
            a=int(input("Enter the amount to withdraw : "))
            if a>account.balance or account.balance==0:
                prRed("----- Your A/C doesn't have sufficient amount -----")
                return
            account.balance=account.balance-a
            account.qu.enqueue(date,"W",a,account.balance)
            #date=date.strftime("%d-%m-%Y")
            trans=open("%s.txt"%account.name,"ab")
            l=[date,"W",a,account.balance]
            pickle.dump(l,trans)
            
        elif(x==2):
            
            a=int(input("Enter the amount to deposit  : "))
            account.balance=account.balance+a
            nwev=account.balance
            account.qu.enqueue(date,"D",a,nwev)
            #date=date.strftime("%d-%m-%Y")
            trans=open("%s.txt"%account.name,"ab")
            """trans.write("%s "%date)
            trans.write("%s "%D)
            trans.write("%d "%a)
            trans.write("%d "%account.balance)"""
            l=[date,"D",a,account.balance]
            pickle.dump(l,trans)
            


    def passbookdisplay(self,k):
        account1=self.chained_search(k)
        if account1.qu.isEmpty():
            prPurple("-*-*-* No transactions to be printed *-*-*-")
            return
        print('||        DATE    || TRANSACTION || AMOUNT   || BALANCE ||')
        k=account1.qu.dequeue()
        #self.frmfile()

    #def loanIssue(self,K):
    #	person=
    def acc_pass(self,k):
    	#a=h(k)
    	account=self.chained_search(k)
    	if(account.password==None):
            while True:
                q=input("Enter a new password : ")
                l=input("Confirm password : ")
                if(q==l):
                  
                    account.password=q
                    pss=open("Password.txt","a+")
                    pss.write("%s" %account.password)
                    pss.write("\n")
                    break

                else:
                    print("Password didn't match")

    	else:
            while True:
                q=input("Enter your password : ")
                if account.password==q:
                    a=input("Enter a new password : ")
                    b=input("Confirm password : ")
                    if a==b:
                        account.password=a
                        prGreen("[[[Password changhed sucessfully!]]]")
                        return
                else:
                    print("Enter correct password or account no")

    def check_balance(self,k):
        k=self.chained_search(k)
        print("Balance is:",k.balance,end="")

    #def pass_check(self,k):




    def loandetails(self):
        prBlack("Set of people with loan : ")
        print()
        print("||  A/C number  ||  Loan amount  ||  Name  ||")
        for i in range (23):
            if self.T[i]==None:
                continue
            h=self.T[i].head
            while h is not None:
                if(h.loan!=None):
                    print("    ",h.key,"           ",h.loan,"          ",h.name,)
                h=h.next



    			





class ListNodell:
    def __init__(self,k):
        self.key=k
        self.next=None
        self.qu=Queue()
        self.phno=None
        self.balance=0
        self.Address=None
        self.name=None
        self.loan=None
        self.password=None


def main():
    h=hashtable()
    date = datetime.datetime.now()
    date=date.strftime("%Y-%m-%d %H:%M")
    h.frmfile()
    prCyan("*********Welcome to VSMK Bank********")
    #h.show()
    while True:
        prCyan("Enter 1: For Coustomer Access")
        prCyan("Enter 2: To Manager")
        prCyan("Enter : Any other to exit ")
        q=int(input("Enter ur choice : "))
        prYellow("-------------------")
        if(q==1):
            prLightPurple("Enter 1:Login")
            prLightPurple("Enter 2:Create A/C")
            
            z=int(input("Enter your option : "))

            if(z==1):
                ac=int(input("Enter your Acc.No : "))
                passwrd=input("Enter your password : ")
                #if(h.T[accno].password!=passwrd):
                #    print("Wrong account no. or password")#shd go back to first statement
                accno=h.chained_search(ac)
                if(accno==False):
                    prRed("**Account doesn't exist**")
                    main()
                #print(accno.password)
                elif(accno.password!=passwrd):
                    print("Wrong A/c number or password")

                else:
                    while True:
                        prYellow("x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x")
                        prGreen("Enter 1 for transactions")
                        prGreen("Enter 2 for checking balance")
                        prGreen("Enter 3 for printing passbook")
                        prGreen("Enter 4 for Deleting")
                        prGreen("Enter 5 Apply for loan")
                        prGreen("Enter 6 to change password")
                        prGreen("Enter 7 to exit")

                        m=int(input("Enter your option : "))
                        if(m==1):
                            h.transactions(ac)

                        elif(m==2):
                            h.check_balance(ac)
                            print("   as of:",date)

                        elif(m==3):
                            h.passbookdisplay(ac)
                            #prYellow("****Thank you****")
                            main()

                        elif(m==4):
                            h.chained_delete(ac)
                            main()

                        elif(m==5):
                            if(accno.loan!=None):
                                prRed("Loan already Sanctioned :)")
                                break
                            choi=int(input("Enter the Loan amount required : "))
                            if choi>=50000 and choi<=800000:
                                prGreen("Loan amount Sanction successfull")
                                accno.loan=choi
                                date = datetime.datetime.now()
                                date=date.strftime("%Y-%m-%d %H:%M")
                                accno.balance=accno.balance+choi
                                accno.qu.enqueue(date,"L",choi,accno.balance)
                                break
                            else:
                                prRed("Loan amount unable to sanction")
                                break

                        elif(m==6):
                            h.acc_pass(ac)

                            break
                        elif(m==7):
                            break

            elif(z==2):
                h.createAC()
                prGreen("*******Account created sucessfully*******")
                
        elif(q==2):
            str=input("Enter the staff password : ")
            if(str=="manager"):
                prLightPurple("Enter 1 : To access Loan Details")
                prLightPurple("Enter any other choice to return ")
                cho=int(input("Enter your Choice : "))
                if(cho==1):
                    h.loandetails()
                else:
                    main()
            else:
                prRed("\\\\\\\ Wrong Password///////")
                main()
        else:
            prYellow("****Thank you , Visit again****")
            exit()

            





if __name__ == '__main__':
	main()