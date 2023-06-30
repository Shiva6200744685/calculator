print(" 1. Addition \n 2. Substraction \n 3. Multiplicatio\n 4. Division \n 5. percentage")
num=int(input("Enter option for operation :"))

#making function for addition
def Addition():
    n= float (input ("Enter total number to add: "))
    sum=0
    for i in range(n):
          num= float (input ())
          sum =sum+n
    print("the sum of the",n ," numbers is",sum)
#making function for substraction
def substraction():
     num1=float(input("Enter first number(greatest number): "))
     num2= float(input("Enter second number: "))
     sub=num1-num2
     print("Substraction of two number is:",sub)
#making function for multiplication
def multiplication():
     num1=float("Enter first Number")
     num2= float("Enter second Number")
     print("Product of the two number is:", num1*num2)
#making function for division
def division():
     num3= int(input("Enter dividend:"))
     deno=int(input("Enter divisor:"))
     try:
          quotient=(num3/deno)
          remainder=(num3%deno)
          print ("Quotient:", quotient, "Remainder:", remainder)
     except:
          print("Error!! wrong, you have entered zero as a divisor")
#making function for pecentage
def percentage():
     obtain= float(input("Enter obtained value:"))
     total= float(input("Enter Total value:"))
     percent=(obtain/total)*100
     print("Percentage : ",percent,"%")
# calling respective function
if num==1:
     Addition()
elif num==2:
     substraction()
elif num==3:
     multiplication()
elif num==4:
     division()
elif num==5:
     percentage()
else:
      print("Invalid Option Entered ")
