import sys
import csv
import turtle

userin = input('اضغط للمواصة,حياك الله')

while userin !=0 :

    print("1 . Print a single record")
    print("2 . Print all record")
    print("3 . Number of record stored")
    print("4 . Add newrecord")
    print("5 . Quit\n")
    
    userin = input("Enter the option number\n")
    if userin == '1' or userin == '2' or userin == '3' or userin == '4' or userin == '5' :
                 ok = False
    else:
                 ok =True
    if ok :
                 print("Enter a valid option please")
   #--------------------              
    if userin == '1':
        
          with open('Employee_data.csv','r')as f:
             ali =csv.reader(f)
             Empname = input("Enter the Employee name to print his/her data:\n")
             print()                
             for r in ali:
               if r[0]==Empname:
                 print("These are the data of :",Empname,"\n")
                 print(r)
                 print()
                 print("Anything else can I do for you?\n")
             else :
                 print("Please enter a vaild name")
                 
   #--------------------                   
    if userin == '2':
        
     subop = input   
    while subop !='d':    
        with open('Employee_data.csv','r')as f:
             ali =csv.reader(f)
             
             print()
             print("option a .Employee Name, Position #, Experience")
             print("option b .Employee name and Position Title")
             print("option c .Employee name and Performance in 2023")
             print("option d . back\n")
             subop = input("Enter the option (a,b,c,d)\n")
             if subop == 'a' or subop == 'b' or subop == 'c' or subop == 'd' :
                 ok = False
             else:
                 ok =True
             if ok :
                 print("Enter a valid option please")
                 
             for r in ali:
                 if subop == 'a':
                  print("Name:",r[0],"\n","Position",r[3],"\n","year of experience",r[4],"\n")
                  
        with open('Employee_data.csv','r')as f:
             ali =csv.reader(f)      
             for r in ali:     
                 if subop == 'b':
                  print("Name:",r[0],"\n","Position Title",r[2],"\n")
                  
        with open('Employee_data.csv','r')as f:
             ali =csv.reader(f)     
             for r in ali:
                 if subop == 'c':
                  print("Name:",r[0],"\n"," Performance in 2023",r[5],"\n")   

   #-------------------- 
    if userin =='3':
     count =0
     with open('Employee_data.csv','r')as f:
             ali =csv.reader(f)
             for r in ali:
                 count=count+1
             print()
             print("Number or records stored in this file =", count,"\n")

 #-------------------- 

    if userin == '4':

        with open('Employee_data.csv','a')as f:
            writer =csv.writer(f)
            name = input("Enter the Employy name")
            gender= input("Enter the gender of employee")
            potitle= input("Enter the position title of employee")
            position= input("Enter the position# of employee")
            exp = input("Enter the experience of employee")
            per= input("Enter the performance of employee")
            
            writer.writerow([name, gender, potitle, position, exp, per])
            print()
            print("THE FILE AFTER WRITE")
            print()
        with open('Employee_data.csv','r')as f:
           ali =csv.reader(f)
           for r in ali:
            print(r)
  #--------------------            
    if userin == '5':

        pen = turtle.Turtle() 
        def curve(): 
            for i in range(200):  
                pen.right(1) 
                pen.forward(1)  
        def heart(): 
            pen.fillcolor('red') 
            pen.begin_fill() 
            pen.left(140) 
            pen.forward(113) 
            curve() 
            pen.left(120)  
            curve()  
            pen.forward(112)  
            pen.end_fill() 
        def txt(): 
            pen.up() 
            pen.setpos(-68, 95) 
            pen.down() 
            pen.color('white') 
            pen.write("thank u", font=(  "Verdana", 12, "bold")) 

        heart() 
        txt()  
        pen.ht()    
    sys.exit()


