import csv 

with open('books.csv','w') as bookfile:
    bookwrite= csv.writer(bookfile)
    bookwrite.writerow(["ISBN","Title","Author","CopiesTotal","CopiesAvailable"])
    bookwrite.writerow(["979002310","Programming in C","Vinodh Mishra","5","5"])
    bookwrite.writerow(["979082310","OOPS in Python","Devendra Singh","5","2"])
    bookwrite.writerow(["9890023191","4.50 From Paddington","Agatha Christie","5","5"])
    bookwrite.writerow(["9022392101","The silent patient","Alex Michales","5","3"])

with open('members.csv','w') as memfile:
    memwrite=csv.writer(memfile)
    memwrite.writerow(["MemberID","Name","Email","Password","Role"])
    memwrite.writerow(["1000","Harini","harini05@yahoo.com","lib123","Librarian"])
    memwrite.writerow(["5001","Manasa","manzz25@outlook.com","man123","Member"])
    memwrite.writerow(["5002","Khenisha","khenu123@gmail.com","khen05","Member"])
    memwrite.writerow(["5003","Nikitha","niki123@gmail.com","niki123","Member"])


with open('loans.csv','w') as loanfile:
    loanwrite=csv.writer(loanfile)
    loanwrite.writerow(["MemberID","Name","ISBN","IssueDate","DueDate","ReturnDate"])