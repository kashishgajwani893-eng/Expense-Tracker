# Expense Tracker project

expenseList = []  # List of expenses in form of dictionary

while True:
    print("=====MENU======")
    print("1.Add Expenses")
    print("2.View all expenses")
    print("3.View total spending")
    print("4.Exit")

    choice = int(input("Please Enter your choice: "))

    # Add Expenses
    if choice == 1:
        date = input("Enter the expense date: ")  # Expense - Kharcha
        category = input("Enter the expense category (Food, Travel, Makeup, books): ")
        description = input("Enter a brief description: ")  # Aur details do
        amount = float(input("Enter the expense amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenseList.append(expense)
        print("\nExpense added successfully")

    # View all expenses
    elif choice == 2:
        if len(expenseList) == 0:
            print("No expenses added yet. Please add an expense first")
        else:
            print("=====All Expenses=====")
            count = 1
            for eachExpense in expenseList:
                print(
                    f"Expense Number {count} -> {eachExpense['date']}, "
                    f"{eachExpense['category']}, {eachExpense['description']}, "
                    f"{eachExpense['amount']}"
                )
                count += 1

    # View total spending
    elif choice == 3:
        total = 0
        for eachExpenses in expenseList:
            total += eachExpenses['amount']
        print("\nTotal expenses:", total)

    # Exit
    elif choice == 4:
        print("Thank you for using our Expense Tracker")
        break

    else:
        print("Invalid choice. Please Try Again")