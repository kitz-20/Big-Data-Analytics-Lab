

import pymongo

#Creating a pymongo client
try:
    conn = pymongo.MongoClient(host="localhost", port=27017)
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

#Verification
print("List of databases existing :")
print(conn.list_database_names())

# database name: mydatabase
db = conn.employee
  
# Created or Switched to collection names: myTable
coll = db.emp

def insert():
    try:
        employeeId = int(input('Enter Employee id :'))
        employeeDept = input('Enter Department :')
        employeeName = input('Enter Name :')
        print("Employee's Address -")
        employeeStreet=input('Enter Street :')
        employeeCity=input('Enter City :')
        employeePin=int(input('Enter Pin :'))
        employeeAge = int(input('Enter Age :'))
        employeeSalary = int(input('Enter Salary :'))
        
        coll.insert(
            {
                "Eid":employeeId,"Deptname":employeeDept,"Ename":employeeName,
                "Address":{"street":employeeStreet,"city":employeeCity, "pincode":employeePin}, 
                "age":employeeAge, "salary":employeeSalary
        })
        print('\nInserted data successfully\n')
    
    except Exception as e:
        print(str(e))

def read():
    try:
        empCol = coll.find()
        print('\n All records from Employee Database \n')
        for emp in empCol:
            print(emp)

    except Exception as e:
        print(str(e))

def update():
    try:
        criteria = int(input('\nEnter id to update\n'))
        select = int(input('\nDo you wish to update name? - press 1 for yes\n'))
        if select == 1:
            name = input('\nEnter name to update\n')
            coll.update_one(
                {"Eid": criteria},
                {
                    "$set": {
                        "Ename":name
                    }
                }
            )
        select = int(input('\nDo you wish to update Department? - press 1 for yes\n'))
        if select == 1:
            dept = input('\nEnter name to update\n')
            coll.update_one(
                {"Eid": criteria},
                {
                    "$set": {
                        "Deptname":dept
                    }
                }
            )

        select = int(input('\nDo you wish to Address? - press 1 for yes\n'))
        if select == 1:
            astreet = input('\nEnter street to update\n')
            acity = input('\nEnter city to update\n')
            apin = input('\nEnter pincode to update\n')
            coll.update_one(
                {"Eid": criteria},
                {
                    "$set": {
                        "Address.street":astreet,
                        "Address.city":acity,
                        "Address.apin":apin
                    }
                }
            )

        select = int(input('\nDo you wish to update Age? - press 1 for yes\n'))
        if select == 1:
            age = int(input('\nEnter age to update\n'))
            coll.update_one(
                {"Eid": criteria},
                {
                    "$set": {
                        "age":age
                    }
                }
            )
        
        select = int(input('\nDo you wish to update Salary? - press 1 for yes\n'))
        if select == 1:
            sal = int(input('\nEnter salary to update\n'))
            coll.update_one(
                {"Eid": criteria},
                {
                    "$set": {
                        "salary":sal
                    }
                }
            )

        print("\n---Records updated successfully---\n")   
    
    except Exception as e:
        print(str(e))

def delete():
    try:
        criteria = int(input('\nEnter employee id to delete\n'))
        coll.delete_many({"Eid":criteria})
        print('\nDeletion successful\n')
    except Exception as e:
        print(str(e))

def main():

    while(1):
    # chossing option to do CRUD operations
        selection = int(input('\nSelect :\n 1) insert\n 2) update\n 3) read\n 4) delete\n 5) exit\nSelection :'))
    
        if selection == 1:
            insert()
        elif selection == 2:
            update()
        elif selection == 3:
            read()
        elif selection == 4:
            delete()
        elif selection == 5:
            break
        else:
            print('\n INVALID SELECTION \n')

main()
