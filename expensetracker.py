import csv
import sys
def saveExpenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Date", "Description"])

        for expense in l:
            writer.writerow([
                expense["Amount"],
                expense["Category"],
                expense["Date"],
                expense["Description"]
            ])

def loadExpenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["Amount"] = int(row["Amount"])
                l.append(row)

    except FileNotFoundError:
        pass
l=[]
loadExpenses()
def addExpense():
    d={}
    try:
       amount=int(input("Enter the Amount: "))
    except:
        print("Amount should be a number and greater than zero!")
    try:
      category=input("Enter the Category: ")
    except:
        print("Category should be string and shouldn't be empty!")
    try:
      date=input("Enter the Date: ")
    except:
      print("Date shouldn't be empty!")
    try:
      description=input("Enter the Description: ")
    except:
      print("Description shouldn't be empty!")
    d["Amount"]=amount
    d["Category"]=category
    d["Date"]=date
    d["Description"]=description
    l.append(d)
    print("Expense is added successfully!")
def viewExpenses():
    count=1
    for i in l:
        print("Expense ",count)
        print("Amount     : ",i["Amount"])
        print("Category   : ",i["Category"])
        print("Date       : ",i["Date"])
        print("Description: ",i["Description"])
        count+=1
def searchExpensebycategory():
    found=False
    category=input("Enter Category of Expense you want: ")
    for i in l:
        if i["Category"]==category:
            found=True
            print("Amount     : ",i["Amount"])
            print("Category   : ",i["Category"])
            print("Date       : ",i["Date"])
            print("Description: ",i["Description"])
    if found==False:
        print("No Expenses found under this category")
def searchbyDate():
    found=False
    date=input("Enter date of Expense you want to see: ")
    for i in l:
        if i["Date"]==date:
            found=True
            print("Amount     : ",i["Amount"])
            print("Category   : ",i["Category"])
            print("Date       : ",i["Date"])
            print("Description: ",i["Description"])
    if found==False:
        print("No Expenses found under this date")
    
def totalExpenses():
    total=0
    for expense in l:
        total+=expense["Amount"]
    print("Total Expenses is: ",total)
def monthlyExpensereport():
    month=input("Enter month: ")
    year=input("Enter year: ")
    total=0
    found=False
    for expense in l:
        part=expense["Date"].split("-")
        if part[1]==month:
            if part[2]==year:
              found=True
              total+=expense["Amount"]
    print("Monthly Expense is: ",total)
    if found==False:
        print("Monthly Expense of the month is not found")
            
            
            
def deleteExpense():
    count=1
    for i in l:
        print("Expense ",count)
        print("Amount     : ",i["Amount"])
        print("Category   : ",i["Category"])
        print("Date       : ",i["Date"])
        print("Description: ",i["Description"])
        count+=1
    d=int(input("Enter Expense number you want to delete: "))
    l.pop(d-1)
    print("Expense deleted Successfully!")
def updateExpense():
    count=1
    for i in l:
        print("Expense ",count)
        print("Amount     : ",i["Amount"])
        print("Category   : ",i["Category"])
        print("Date       : ",i["Date"])
        print("Description: ",i["Description"])
        count+=1
    num=int(input("Enter Expense number you want to update: "))
    l[num-1]["Amount"]=int(input("Enter the amount to update: "))
    l[num-1]["Category"]=input("Enter the Category to update: ")
    l[num-1]["Date"]=input("Enter the date to update: ")
    l[num-1]["Description"]=input("Enter the description to update: ")
    print("Expense updated Successfully!")

def categorywiseTotal():
    s=input("Enter Category for which you need total: ")
    found=False
    t=0
    for expense in l:
        if expense["Category"]==s:
            found=True
            t+=expense["Amount"]
    print("Total Expenses under this category is: ",t)
    if found==False:
        print("No Expenses found under this category")
while(True):
    print("============ Expense Tracker ============")
    print("1.Add Expense")
    print("2.View all Expenses")
    print("3.Search Expense by Category")
    print("4.Search Expense by date")
    print("5.Calculate Total Expenses")
    print("6.Monthly Expenses Report")
    print("7.Delete an Expense")
    print("8.Update an Expense")
    print("9.Category wise total")
    print("10.Exit")
    n=int(input("Enter your choice: "))
    print("\n")
    print("Your choice is: ",n)
    if n==1:
        addExpense()
        saveExpenses()
    elif n==2:
        viewExpenses()
    elif n==3:
        searchExpensebycategory()
    elif n==4:
        searchbyDate()
    elif n==5:
        totalExpenses()
    elif n==6:
        monthlyExpensereport()
    elif n==7:
        deleteExpense()
        saveExpenses()
    elif n==8:
        updateExpense()
        saveExpenses()
    elif n==9:
        categorywiseTotal()
    elif n==10:
        print("Thank you for using Expense Tracker!")
        sys.exit()
        
    else:
        print("Invalid input")
        
    
