import datetime

#Declaring Dictionary variable to store Car and Bokking data
cardict={}
bookingdict={}

#Class Car to initialize a car object when adding a new car
class Car:
    def init(self, id, name, desc, cost):
        Car.__carid=self.id
        Car.__carname=self.carname
        Car.__cardesc=self.desc
        Car.__carcost=self.cost
    #It cotains Getters & Setters    
    def setcarid(self, var):
        self.__carid=var
        
    def getcarid(self):
        return self.__carid
        
    def setcarname(self, var):
        self.__carname=var
        
    def getcarname(self):
        return self.__carname
        
    def setcardesc(self, var):
        self.__cardesc=var
        
    def getcardesc(self):
        return self.__cardesc
        
    def setcarcost(self, var):
        self.__carcost=var
        
    def getcarcost(self):
        return self.__carcost

#Class Booking to initialize a booking object when booking a new car
class Booking:
    def init(self, id, flag, bookedfrom, bookedto, carid, custid, amount):
        self.__bookingid=id
        self.__bookingstatus=flag
        self.__bookedfrom=bookedfrom
        self.__bookedto=bookedto
        self.__carid=carid
        self.__custid=custid
        self.__bookingamount=amount
        
    def setbookingid(self, var):
        self.__bookingid=var
        
    def getbookingid(self):
        return self.__bookingid
        
    def setbookingstatus(self, var):
        self.__bookingstatus=var
        
    def getbookingstatus(self):
        return self.__bookingstatus
        
    def setbookedfrom(self, var):
        self.__bookedfrom=var
        
    def getbookedfrom(self):
        return self.__bookedfrom
        
    def setbookedto(self, var):
        self.__bookedto=var
        
    def getbookedto(self):
        return self.__bookedto
        
    def setcarid(self, var):
        self.__carid=var
        
    def getcarid(self):
        return self.__carid
        
    def setcustid(self, var):
        self.__custid=var
        
    def getcustid(self):
        return self.__custid
        
    def setbookingamount(self, var):
        self.__bookingamount=var
        
    def getbookingamount(self):
        return self.__bookingamount    

#This function will Add car, it will take Car related input from user and add the data in the car dictionary variable.        
def addcar():
    carobj=Car()
    carid=str(input("Kindly Enter the Car ID: "))
    carobj.setcarid(carid)
    if carobj.getcarid() in cardict.keys():
        print("Entered Car ID is already exist, please enter unique Car ID")
        return False
    carname=str(input("Kindly Enter the Car name: "))
    cardesc=str(input("Please Provide the Car description: "))
    carcost=str(input("Kindly Enter the Car Cost: "))
    carobj.setcarname(carname)
    carobj.setcardesc(cardesc)
    carobj.setcarcost(carcost)
    cardict[carobj.getcarid()]=[carobj.getcarname(), carobj.getcardesc(), carobj.getcarcost()]
    return True

#This function will Delete the car, it will take Car ID from user and validated and then delete the data in the car dictionary variable.
def deletecar():
    carid=str(input("Kindly Enter the Car ID which do you want Delete: "))
    if carid in cardict.keys():
        del cardict[carid]
        return True
    else:
        print("Kindly enter the correct Car ID, this Car ID does not exist")
        return False

#This function provides booking information, it will take Car ID from user and show all the available bookings of the given Car ID.
def bookinginfo():
    carid=str(input("Kindly Enter the Car ID, for which you to see booking(s): "))
    count=0
    for key, value in bookingdict.items():
        if value[3]==carid:
            print("Booking ID "+ key+" ,Car ID "+value[3]+" is booked from "+value[1]+" to "+value[2]+" in the name of "+value[4])
            count+=1
    if count==0:
        print("No booking is available for "+carid)
    return True

#This function provides Car information, it will take Car ID from user and show all the available information of the given Car ID from the car dictionary variable.
def carinfo():
    print("Kindly Enter the Car ID among below total available cars, for which you to see the details: ")
    l=[]
    for key in cardict.keys():
        l.append(key)
    print(l)
    a=str(input())
    if a not in l:
        print(a+" is not available in the Car's list, please enter the valid Car ID")
    else:
        print(cardict[a])
    return True

#This function will help the admin to assign/unassign the car, first it will check all the available booking and repond accordingly. If car is assigned it will delete the booking and if no booking is available then it will book the car.
def ass_uncar():
    print("Kindly Enter the Car ID among below total available cars, for which you to Assign/Unassign the booking: ")
    l=[]
    for key in cardict.keys():
        l.append(key)
    print(l)
    carid=str(input())
    if carid not in l:
        print(carid+" is not available in the Car's list, please enter the valid Car ID")
    else:
        count=0
        varlist=[]
        for key, value in bookingdict.items():
            if value[3]==carid:
                varlist.append(key)
                count+=1
        if count==0:
            print("No current booking is available for "+carid)
            print("For assigning a Car, kindly book the car")
            searchavail()
        else:
            print(varlist)
            bid=str(input("Kindly enter the Booking ID from the above available bookings: "))
            if bid not in varlist:
                print(bid+" is not available in the Booking list, please enter the valid Booking ID")
            vl=bookingdict[bid]
            if vl[0]=='Assigned':
                del bookingdict[bid]
                print("Car Booking has been unassigned successfully!")
        
    return True

#This function will confirm the booking, it will take dates input from the user and then provide the list of all the available cars then user can book from the available cars.
def searchavail():
    bookedfrom=str(input("Kindly Enter date(DDMMYYYY format) from when do you want to book the car: "))
    bookedto=str(input("Kindly Enter end date(DDMMYYYY format): "))
    fromdate = datetime.datetime.strptime(bookedfrom,'%d%m%Y')
    todate = datetime.datetime.strptime(bookedto,'%d%m%Y')
        
    availl=[]
    for keys in cardict.keys():
        count=0
        for key, value in bookingdict.items():
            if value[3]==keys:
                fromdateboooked = datetime.datetime.strptime(value[1],'%d%m%Y')
                todatebooked = datetime.datetime.strptime(value[2],'%d%m%Y')
                if (fromdate>=fromdateboooked and fromdate<=todatebooked) or (todate>=fromdateboooked and todate<=todatebooked):
                    count+=1
                elif fromdate<=fromdateboooked and todate>=todatebooked:
                    count+=1
                else:
                    count+=0
        if count==0:
            availl.append(keys)
    if len(availl)==0:
        print("Sorry! No Car is available for the specific dates")
    else:
        print("Below are the available Car(s) for your respective dates!")
        for i in availl:
            print("Car ID: "+i+"  ["+cardict[i][0]+"  "+cardict[i][1]+"  "+cardict[i][2]+"]")
        cid=str(input("Kindly enter the Car ID, which do you want to book: "))
        cust=str(input("Kindly enter your name: "))
        nod=(todate-fromdate).days
        amt=int(cardict[cid][2])*nod
        bookingobj=Booking()
        bidd=str(len(bookingdict.keys())+101)
        bookingobj.setbookingid(bidd)
        bookingobj.setbookingstatus('Assigned')
        bookingobj.setbookedfrom(bookedfrom)
        bookingobj.setbookedto(bookedto)
        bookingobj.setcarid(cid)
        bookingobj.setcustid(cust)
        bookingobj.setbookingamount(str(amt))
        bookingdict[bookingobj.getbookingid()]=[bookingobj.getbookingstatus(), bookingobj.getbookedfrom(), bookingobj.getbookedto(), bookingobj.getcarid(), bookingobj.getcustid(), bookingobj.getbookingamount()]
        print("Your booking has been confirmed!!!")
        print("Yor booking id is "+bookingobj.getbookingid()+"  , kindly save it for future reference")
        print(bookingdict[bookingobj.getbookingid()])
        
    return True

#This function allows the user to cancel the booking, it will take Booking ID from the user.
    bid=str(input("Kindly Enter the Booking ID which do you want Cancel: "))
    if bid in bookingdict.keys():
        del bookingdict[bid]
        return True
    else:
        print("Kindly enter the correct Booking ID, this Booking ID does not exist.")
        return False

#This function is used to return in the main menu after performing every action.
def returnadminmenu():
    adminmenu()

#This function provides all the Admin actions, user will select the desired action and on the basis of that it will call the specific function.
def adminmenu():
    op=int(input("Please enter which opertion do you want to perform.\n1. Add Car\n2. Delete Car\n3. View Car Information\n4. Assign/Unassign Car\n5. View Booking Information\n6. Customer menu\n"))
    if op==1:
        s=addcar()
        if s:
            print("Car has been added successfully!")
            returnadminmenu()
        else:
            print("Car has not been added, please try again!")
            returnadminmenu()
    if op==2:
        s=deletecar()
        if s:
            print("Car has been deleted successfully!")
            returnadminmenu()
        else:
            print("Car has not been deleted, please try again!")
            returnadminmenu()
    if op==3:
        carinfo()
        returnadminmenu()
    
    if op==4:
        ass_uncar()
        returnadminmenu()

    if op==5:
        bookinginfo()
        returnadminmenu()
    if op==6:
        custmenu()

#This function is used to return in the main menu after performing every action.
def returncustmenu():
    custmenu()

#This function provides all the Customer actions, user will select the desired action and on the basis of that it will call the specific function.
def custmenu():
    op=int(input("Please enter which opertion do you want to perform.\n1. Serach Availibility\n2. Cancel Booking\n"))
    if op==1:
        s=searchavail()
        returncustmenu()
            
    if op==2:
        s=cancelbooking()
        if s:
            print("Booking has been canceled successfully!")
            returncustmenu()
        else:
            print("Booking has not been deleted, please try again!")
            returncustmenu()

#Declaring Admin variable, to check the admin mode
admin='False'   
print("\n\n********Welcome to the Car Rental Service********\n\n")
print("To enable Admin Mode enter y, otherwise press N for Customer")
*Will ask user if he/she wants to enable the Admin mode or will continue with the Customer role
authflag=input()
if authflag=='y':
    print("Please Enter the Password: ")
    pwd=str(input())
    if pwd=='admin':
        admin='True'
        print("You are logged in as an Admin Successfully!")
        adminmenu()   
    else:
        print("Please enter the correct password")
        
else:
    print("You are logged in as a customer!")
    custmenu()

    
        


