#PYTHON MODULE :MENULIB(LIBRARY MANAGEMENT SYSTEM)
import Book
import Member
import Issue

def MenuBook():
    while True:
        print("\t\t\t Book Record Management\n")
        print("==============================================================")
        print("1. Add Book Record ")
        print("2. Display Book Records ")
        print("3. Search Book Record ")
        print("4. Delete Book Record ")
        print("5. Update Book Record ")
        print("6. Return to Main Menu ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 5-------> : "))
        if choice==1:
            Book.insertData()
        elif choice==2:
            Book.display()
        elif choice==3:
            Book.SearchBookRec()
        elif choice==4:
            Book.deleteBook()
        elif choice==5:
            Book.UpdateBook()
        elif choice==6:             
            return
        else:
             print("Wrong Choice......Enter Your Choice again")
        #x=input("Enter any key to continue")

#----------------------------------------------------------------------------------------
def MenuMember():
    while True:
        print("\t\t\t Member Record Management\n")
        print("==============================================================")
        print("1. Add Member Record ")
        print("2. Display Member Records ")
        print("3. Search Member Record ")
        print("4. Delete Member Record ")
        print("5. Update Member Record ")
        print("6. Return to Main Menu ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 5-------> : "))
        if choice==1:
            Member.insertMember()
        elif choice==2:
            Member.display()
        elif choice==3:
            Member.SearchMember()
        elif choice==4:
            Member.deleteMember()
        elif choice==5:
            Member.UpdateMember()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
        #x=input("Enter any key to continue")
#----------------------------------------------------------------------------------------

def MenuIssueReturn():
     while True:
        print("\t\t\t Issue Record Management\n")
        print("==============================================================")
        print("1. Issue Book ")
        print("2. Display Issued Book Records ")
        print("3. Return Issued Book ")
        print("4. Return to Main Menu ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 5-------> : "))
        if choice==1:
            Issue.issueBook()
        elif choice==2:
            Issue.ShowIssuedBooks()
        elif choice==3:
            Issue.returnBook()
        elif choice==4:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
        #x=input("Enter any key to continue")