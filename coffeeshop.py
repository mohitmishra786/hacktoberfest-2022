import time
def pos(Menu,orders,Coffe_name,Coffee_size,quantity):
    file1=open('D:\pro1234.txt','w')
    prz1cal=[]
    cofnam=[]
    custqua=[]
    ttlam=[]
    for i in range(orders):
        for key,val in Menu.items():
            if key==Coffee_name:
                if Coffee_size=='full cup':
                    amount=quantity*val
                    GST_amount=(amount*13)/100
                    netprice=(amount+GST_amount)
                elif Coffee_size=='small cup':
                    amount=c*val
                    GST_amount=(amount*13)/100
                    netprice=(amount+GST_amount)
        prz1cal.append(netprice)
        cofnam.append(Coffee_name)
        custqua.append(quantity)
        ttlam.append(amount)
        
    finalprice=sum(prz1cal)
    ttlam1=sum(ttlam)
    cstaq=sum(custqua)
    a2=str(finalprice)
    file1.write(a2)
    
    
    Option3=int(input("ENTER 3 FOR GENERATE A SLIP"))
    if Option3==3:
          costumer_name=input("Enter contumer name")
          print()
          print('''''''  <<--------->> DESIRE DRINKS <<--------->>    ''''''')
          print('__________')
          print(time.strftime('%A %b/%d/%y %I:%M %p')) 
          print()
          print('--------------------------------------------------------------------------------')
          print("YOUR NAME:","\t", costumer_name)
          print()
          print("COFFEE Name:","\t", cofnam)
          print()
          print("COFFEE QUANTITY","\t",Coffee_size)
          print()
          print("QUANTITY:","\t", cstaq)
          print()
          print("AMOUNT: ","\t", ttlam1)
          print()
          print("GST 13% :","\t", GST_amount)
          print()
          print("TOTAL AMOUNT:","\t", finalprice)
          print('__________')
          file1.close()
 
#drivers code
print('''''  
      1.Menu
      2.Select Items
      3.Generate Slip''''')
Option1=int(input("ENTER 1 FOR GO TO MENU"))
if Option1==1:
    print('''''    Here's Our MENU   ''''')
    file1=open('D:\pro123.txt','w')
    Menu={'expresso':300,'cappiciano':300,'latte':200,'mocha':200,'flat white':400}
    Menu1=str(Menu)
    file1.write(Menu1)
    print(Menu)print('HOW MANY COFFEES DO YOU WANT??')
orders=int(input('ENTER ORDER NO'))
ask='yes'

while ask=='yes':
    Option2=int(input("ENTER 2 FOR SELECT ITEMS"))
    if Option2==2:
        Coffee_name=input("Enter a Coffee Name: ")
        Coffee_size=(input("DO YOU WANT FULL CUP OR SMALL?: "))
        quantity=int(input("Enter a quantity:"))
        ask=input("DO YOU WANT TO ENTER MORE ITEMS(YESorNO)")
