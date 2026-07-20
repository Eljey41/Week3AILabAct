def check_borrowing(overdue_books, status):
    if overdue_books <= 0 and status == "active":
        return "Borrowing Allowed"
    elif overdue_books >= 0:
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Not allowed to borrow any books"


student_list = []
borrowed_books_list = []

while True:
    student_input = input("Enter your name or 'exit' to stop: ").strip().lower()
    
    if student_input == "exit":
        break

    has_overdue_books = input("Do you have overdue books (yes/no): ").strip().lower()
    status = input("What is your status? (active/suspended): ").strip().lower()
    number_of_books_borrow = int(input("How many books they want to borrow"))

    result = check_borrowing(student_input, has_overdue_books, status, number_of_books_borrow)

    if result == "Succesfully allowed to borrow books":
        if status == "Active":
            student_list.append(student_list)
        print(student_input + ": ")


