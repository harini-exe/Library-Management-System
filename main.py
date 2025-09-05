import csv
from datetime import date,timedelta

def login(role):
    userid=input("Enter user ID: ")
    pwd= input("Enter password: ")
    with open('members.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["MemberID"]==userid and row["Password"]==pwd and row["Role"]==role:
                print("Login Successful")
                return userid 
            
    print("Wrong Credentials,try again")
    return None




def main():
    while True:
        print("====LIBRARIAN MANAGEMENT SYSTEM====")
        print("1.Librarian login")
        print("2.Member login")
        print("3.Exit")
        choice=input("enter choice: ")
        if choice=="1":
             userid=login("Librarian")
             if userid:
                 print("Welcome Librarian!")
                 print("1.Add a new book")
                 print("2.Add a new Member")
                 print("3.Issue a book")
                 print("4.Return a book")
                 action=input("Enter Action: ")
                 if action=="1":
                     addbook()
                 if action=="2":
                     addmember()
                 if action=="3":
                     issuebook()
                 if action=="4":
                     returnbook()
        elif choice=="2":
            userid=login("Member")
            if userid:
                print("Welcome Member")
                print("1.Check dues")
                print("2.Look for a book")
                action=input("enter choice: ")
                if action=="1":
                    checkdues(userid)
                elif action=="2":
                    lookforbook()
        elif choice=="3":
            break
#####################################
                
def addbook():
    with open('books.csv','a',newline='') as file:
        bookwriter=csv.writer(file)
        isbn=input("Enter ISBN:")
        title=input("Enter Title: ")
        author=input("Enter Author: ")
        total=input("enter total copies: ")
        available=total
        bookwriter.writerow([isbn,title,author,total,available])
        print("book added!")

###########################################
def addmember():
    with open('members.csv','r',newline='') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
        if len(rows)==0:
            newid=5000
        else:
            lastrow=rows[-1]
            lastid=int(lastrow["MemberID"])
            newid=lastid+1
    name=input("Enter Name: ")
    email=input("Enter email: ")
    password=input("Enter password: ")
    role="Member"
    with open('members.csv','a',newline="") as file:
        memwriter=csv.writer(file)
        memwriter.writerow([newid, name, email, password, role])
        print(f"Added member successfully with ID={newid}")

############################
def issuebook():
    isbn=input("Enter ISBN: ")
    memberid=input("Enter memberID: ")
    membername=""
    with open('members.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["MemberID"] == memberid:
                membername = row["Name"]
                break
    if membername == "":
        print("Invalid Member ID.")
        return

    with open('books.csv','r') as file:
        bookreader=csv.DictReader(file)
        books=list(bookreader)
        found=False
        for book in books:
            if book["ISBN"]==isbn:
                found=True
                if int(book["CopiesAvailable"])>0:
                    print("Book available, issuing now...")
                    book["CopiesAvailable"]=str(int(book["CopiesAvailable"])-1)

                    with open('loans.csv','a',newline='') as loanfile:

                        loanwriter = csv.writer(loanfile)
                        issue_date = date.today().isoformat()
                        due_date = (date.today() + timedelta(days=14)).isoformat()
                        loanwriter.writerow([memberid, membername, isbn, issue_date, due_date, ""])
                    print(f"Book {isbn} is issued to Member {memberid}")
                else:
                    print("no copies available.")
        if not found:
            print("book not found")
    
    with open('books.csv', 'w', newline='') as file:
        fieldnames = ["ISBN", "Title", "Author", "CopiesTotal", "CopiesAvailable"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

def returnbook():
    isbn=input("Enter isbn of the book returned: ")
    memberid=input("Enter member ID: ")
    today=date.today().isoformat()
    loans=[]
    found=False
    with open('loans.csv','r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["MemberID"]==memberid and row["ISBN"]==isbn and row["ReturnDate"]=="":
                row["ReturnDate"]=today
                found=True 
            loans.append(row)
    if not found:
        print("no active loan found for this user. ")
        return 
    with open('loans.csv','w',newline = "") as f:
        writer=csv.DictWriter(f,fieldnames=loans[0].keys())
        writer.writeheader()
        writer.writerows(loans)
    books=[]
    with open('books.csv','r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["ISBN"]==isbn:
                row["CopiesAvailable"]=str(int(row["CopiesAvailable"])+1)
            books.append(row)
    with open("books.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        writer.writerows(books)

    print("Book returned successfully.")
                

        


def checkdues(userid):
    with open('loans.csv','r') as file:
        loanreader=csv.DictReader(file)
        for row in loanreader:
            if row["MemberID"]==userid and row["ReturnDate"]=="":
                print(f"Book {row['ISBN']} due on {row['DueDate']} (not returned yet)")
            else:
                print("No dues.")
def lookforbook():
    title = input("Enter title to search: ").lower()
    with open('books.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if title in row["Title"].lower():
                print(f"{row['ISBN']} - {row['Title']} by {row['Author']} (Available: {row['CopiesAvailable']})")

if __name__ == "__main__":
    main()
            
             
    


