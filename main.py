class Library:
    def __init__(self, list,name):
        self.bookslist = list
        self.naem = name
        self.lendDict = {}

    def desplayBooks(self):
        print(f"We have the following books in our library{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.bookslist:
          print("Sorry we do not have this book.")
        elif book in self.lendDict:
         print(f"The book is already being used by {self.lendDict[book]}")
        else:
          self.lendDict[book] = user
        print("Lender-book database has been updated. You can take the book now.")

def addBook(self, book):
    self.booklist.append(book)
    print(f"{book} has been added to the book list.")

def returnBook(self,book):
    if book in self.lendDict:
        del self.lendDict[book]
        print("Book has been returned")
    else:
        print("The book wasn't borrowed from us.")


if __name__ == '__main__':
    books = Library(['python', 'Rich dad Poor dad', 'Harry Pottter', 'C++ Basics', 'Algorithms by CLRS'], "let's upskill")
    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(
            f"/nHello {user_name}, welcome to the {books.name} library.
                Please choose an option:"
        )
        print(
            "1. Display Books/n2. Lend a book/n3. Add a book/n4. Reurn a book/n5. Quit"
        )
        user_choice = input("Enter your choice to continue:")

        if user_name not in ['1', '2,', '3','4','5']:
            print("Pleasee enter a valid option.")
            continue

        if user_choice == '1':
            books.desplayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend:")
            books.LendBook(user_name, book)
        elif user_choice == '3':
            book= input("Enter the name of the book you want to add:")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}.Goodbye")
            break
