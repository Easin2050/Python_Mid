class Library:
    book_list=[]
    @classmethod
    def entry_book(self,book):
        self.book_list.append(book)

class book:
    def __init__(self,book_id,title,author,availability=True)->None:
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability
        Library.entry_book(self)
    def get_book(self):
        return self.__book_id
    def borrow_book(self):
        if self.__availability:
            self.__availability=False
            print(f"Book { self.__title} is borrowed successfully")
        else:
            print(f"Book { self.__title} is already borrowed")
        
    
    def view_book_info(self):
        if self.__availability:
            book_is_there="Available"
        else:
            book_is_there="Not available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Avaiability: {book_is_there}")
    
    def return_book(self):
        if self.__availability==False:
            self.__availability=True
            print(f"Book '{self.__title}' is return successfully")
        else:
            print(f"Book '{self.__title}' is not returned")

book1=book(1,'1984','George Orwell')
book2=book(2,'The catcher in the Rye','J.D. Salinger')
book3=book(3,'To kill a Mockingbird','Harper Lee')
book4=book(4,'A golden Age','Thamima Anam')
book5=book(5,'Brick Lane','Monica Ali')
book6=book(6,'The Good Muslims','Thamima Anam')
book7=book(7,'The Strom','Arif Anwar')
book8=book(8,'The Bones of grace','Thamima Anam')

def manu_System():
    while True:
        print('<--Welcome to the Libraray Menu-->')
        print('1. View All Books')
        print('2. Borrow Book')
        print('3.Return Book')
        print('4.Exit')
        choice=input('Enter your choice:')
        if choice=='1':
            for book in Library.book_list:
                book.view_book_info()
        elif choice=='2':
            try:
                book_id=int(input("Enter the book id for borrow: "))
                found=False
                for book in Library.book_list:
                    if book.get_book()==book_id:
                        book.borrow_book()
                        found=True
                        break
                if not found:
                    print("Sorry The book is not in the library")
            except ValueError:
                print("Invalid input. Enter Number")
        elif choice=='3':
            try:
                book_id=int(input("Enter the return book id:"))
                found=False
                for book in Library.book_list:
                    if book.get_book()==book_id:
                        book.return_book()
                        found=True
                        break
                if not found:
                    print("Sorry the book in not in library")
            except ValueError:
                print("Invalid input. Enter Number")
        elif choice=='4':
            print("Existing,Thanks for visiting the library")
        else:
            print("Please enter a number between 1 to 4")
manu_System()