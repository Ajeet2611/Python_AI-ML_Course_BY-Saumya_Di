#Expense Tracker project
expensesList = []#List of all expenses in form of dictionary
print("Welcome to Expense Tracker :  Kharcha kam kiya karo")

while True :
    print("===MENU===")
    print("1. Add Expenses")
    print("2. View All Expenses ")
    print("3. View Total Kharcha ")
    print("4. Exit ")

    choice = int(input("Please Enter your Choice : "))
    #Add Expenses
    if(choice ==1):
        date = input("Please enter your Expenses Date (DD/MM/YYYY): ")
        category = input("kis type ka kharcha kiya hai (Food,Travel,Makeup...e.t.c): ")
        description =input("Aur detail dedo: ")
        amount = float(input("Enter the amount: "))

        expense ={
            "date": date,
            "category":category,
            "description": description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n Done bro Expenses is added succesfully ")

#2. VIEW ALL EXPENSES

    elif(choice ==2):
            if(len(expensesList)==0):
                print("No Expenses Added . Jao pahle kharcha karo. ")

            else:
                print("====Ye  yah aapka sara expense====")
                count = 1
                for eachKharcha in expensesList:
                    print(f'Kharcha Number {count}->, {eachKharcha["date"]},{eachKharcha["category"]},{eachKharcha["description"]},{eachKharcha["amount"]}')
                    count+=1

#3. View Total Spending

    elif(choice==3):
         total = 0
         for eachKharcha in expensesList :
              total =total +eachKharcha["amount"]

         print("\n Total Kharcha = ",total)
    
#4. Exit
    elif(choice==4):
         
         print("Dhanyawad aapne humara system use kiya ! ")
         break
    

    else:
         print("INVALID CHOICE (Please try again and choose any one -->(1,2,3,4 ) !")



              
     
