def check_borrowing(overdue_books, status):
    if overdue_books == "no" and status == "active":   
        return "Borrowing Allowed"
    elif overdue_books == "yes":
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Invalid status or overdue book information"


student_list = []
total_borrowed_books = 0
students_successfully_borrowed = 0



while True:
    student_input = input("Enter your name or 'exit' to stop: ").strip().lower()
    
    if student_input == "exit":
        break

    has_overdue_books = input("Do you have overdue books (yes/no): ").strip()
    status = input("What is your status? (active/suspended): ").strip().lower()
    number_of_books_borrow = int(input("How many books you want to borrow: "))
    


    result = check_borrowing(has_overdue_books, status)

    if result == "Borrowing Allowed":

        if has_overdue_books == "no" and status == "active" and number_of_books_borrow <= 3:
            student_list.append(student_input)
            total_borrowed_books += number_of_books_borrow
            students_successfully_borrowed += 1
        if number_of_books_borrow > 3:
            print(student_input, ": Not Allowed: You've reached the limit of 3 books.")
            continue

        print(student_input, ": Succesfully allowed to borrow books")
    




        
    elif result == "Not allowed: overdue books":
        if has_overdue_books == "yes":
            print(student_input + ": Not allowed: You must return the books first.")



    elif result == "Not allowed: suspended account":
        if status == "suspended":
            print(student_input + ": Not allowed: suspended account")


    else:
        print(student_input + ": Invalid status or overdue book information")
    print()

print("Student List: ", student_list)
print("Borrowed Books List: ", total_borrowed_books)
print("Count of successfully borrowed books: ", students_successfully_borrowed)

        


