import getpass
from datetime import datetime, timedelta

class LibraryManagementSystem:
    def __init__(self):
        self.admins = {"Osama": "1234"}  
        self.logged_in_admin = None
        self.books = {}
        self.issued_books = {}

    def login(self):
        admin_id = input("Enter admin ID: ")
        admin_password = getpass.getpass("Enter password: ")
        if admin_id in self.admins and self.admins[admin_id] == admin_password:
            self.logged_in_admin = admin_id
            print(f"Welcome, {self.logged_in_admin}!")
        else:
            print("Invalid credentials. Please try again.")

    def change_password(self):
        if self.logged_in_admin:
            new_password = getpass.getpass("Enter new password: ")
            self.admins[self.logged_in_admin] = new_password
            print("Password changed successfully.")
        else:
            print("You need to log in first.")

    def display_dashboard(self):
        if self.logged_in_admin:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nDashboard\nLogged-in Admin: {self.logged_in_admin}\nCurrent Time: {current_time}")

    def add_book(self):
        if self.logged_in_admin:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            quantity = int(input("Enter the quantity of the book: "))
            self.books[isbn] = {"Title": title, "Author": author, "Quantity": quantity}
            print(f"Book '{title}' added to the store.")
        else:
            print("You need to log in first.")

    def issue_book(self):
        if self.logged_in_admin:
            isbn = input("Enter the ISBN of the book to issue: ")
            if isbn in self.books and self.books[isbn]["Quantity"] > 0:
                if self.logged_in_admin not in self.issued_books:
                    self.issued_books[self.logged_in_admin] = []
                if len(self.issued_books[self.logged_in_admin]) < 3:
                    self.issued_books[self.logged_in_admin].append((isbn, datetime.now()))
                    self.books[isbn]["Quantity"] -= 1
                    print(f"Book with ISBN {isbn} issued successfully.")
                else:
                    print("You have reached the maximum limit of issued books (3).")
            else:
                print("Book not available or out of stock.")
        else:
            print("You need to log in first.")

    def return_book(self):
        if self.logged_in_admin:
            isbn = input("Enter the ISBN of the book to return: ")
            if self.logged_in_admin in self.issued_books:
                for book in self.issued_books[self.logged_in_admin]:
                    if book[0] == isbn:
                        return_date = datetime.now()
                        days_issued = (return_date - book[1]).days
                        fine = max(0, days_issued - 7) * 5  # Fine of $5 per day after 7 days
                        self.books[isbn]["Quantity"] += 1
                        self.issued_books[self.logged_in_admin].remove(book)
                        print(f"Book with ISBN {isbn} returned successfully.")
                        if fine > 0:
                            print(f"Fine charged: ${fine}")
                        return
            print("Book not issued to the logged-in admin.")
        else:
            print("You need to log in first.")

    def edit_book(self):
        if self.logged_in_admin:
            isbn = input("Enter the ISBN of the book to edit: ")
            if isbn in self.books:
                print(f"Current details of the book with ISBN {isbn}:")
                print(self.books[isbn])
                new_title = input("Enter the new title (leave blank to keep the current title): ") or self.books[isbn]["Title"]
                new_author = input("Enter the new author (leave blank to keep the current author): ") or self.books[isbn]["Author"]
                new_quantity = int(input("Enter the new quantity (leave blank to keep the current quantity): ") or self.books[isbn]["Quantity"])
                self.books[isbn] = {"Title": new_title, "Author": new_author, "Quantity": new_quantity}
                print(f"Book with ISBN {isbn} edited successfully.")
            else:
                print("Book not found.")
        else:
            print("You need to log in first.")

    def delete_book(self):
        if self.logged_in_admin:
            isbn = input("Enter the ISBN of the book to delete: ")
            if isbn in self.books:
                del self.books[isbn]
                print(f"Book with ISBN {isbn} deleted successfully.")
            else:
                print("Book not found.")
        else:
            print("You need to log in first.")

    def search_books(self):
        if self.logged_in_admin:
            isbn = input("Enter the ISBN of the book to search: ")
            if isbn in self.books:
                print(f"Details of the book with ISBN {isbn}:")
                print(self.books[isbn])
            else:
                print("Book not found.")
        else:
            print("You need to log in first.")

    def show_books(self):
        if self.logged_in_admin:
            print("Books in the store:")
            for isbn, details in self.books.items():
                print(f"ISBN: {isbn}, Title: {details['Title']}, Author: {details['Author']}, Quantity: {details['Quantity']}")
        else:
            print("You need to log in first.")

    def logout(self):
        self.logged_in_admin = None
        print("Logged out successfully.")

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Login")
            print("2. Change Password")
            print("3. Add Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Edit Book")
            print("7. Delete Book")
            print("8. Search Books")
            print("9. Show Books")
            print("10. Logout")

            choice = input("Enter your choice (1-10): ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.change_password()
            elif choice == '3':
                self.add_book()
            elif choice == '4':
                self.issue_book()
            elif choice == '5':
                self.return_book()
            elif choice == '6':
                self.edit_book()
            elif choice == '7':
                self.delete_book()
            elif choice == '8':
                self.search_books()
            elif choice == '9':
                self.show_books()
            elif choice == '10':
                self.logout()
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.run()
