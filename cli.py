from helpers import add_user, get_user_by_email, update_user_budget, delete_user,get_all_users,get_all_categories, add_category,add_transaction,get_transaction_by_user

from datetime import datetime
def main_menu():
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add User")
        print("2. View User by email")
        print("3. Update User budget: ")
        print("4. Delete User: ")
        print("5. List all Users: ")
        print("6. View all categories: ")
        print("7. Add a new category: ")
        print("8. Add Transaction: ")
        print("9. Get a single user transaction: ")
        print("0. Exit")


        choice =input("Choose an option: ")

        if choice=="1":
            name=input("Enter name :")
            email=input("Enter email :")
            password=input("Enter password :")
            budget=input("Enter Monthly budget :")
            currency=input("Enter currency :")

            user=add_user(name, email, password, budget, currency)
            print(f"User {user.name} added successfully! ")



        elif choice=="2":
            email=input("Enter user email: ")
            user=get_user_by_email(email)
            if user:
                print(f"User: {user.name}, Budget: {user.monthly_budget} {user.currency}")
            else:
                print("User not found. ")


        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            new_budget = float(input("Enter new budget amount: "))
            user_data = update_user_budget(user_id, new_budget)
            if user_data:
                print(f"User {user_data['name']}'s budget updated to {user_data['monthly_budget']} {user_data['currency']}")
            else:
                 print("User not found or update failed.")



        elif choice=="4":
            user_id=int(input("Enter user Id to delete: "))
            if delete_user(user_id):
                print("User deleted successfully. ")
            else:
                print("User not found. ")

        elif choice =="5":
            users=get_all_users()
            if users:
                print("\nAll Users: ")
                for user in users:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Budget: {user.monthly_budget} {user.currency}")
            else:
                print("No users found. ")
        elif choice=="6":
            categories=get_all_categories()
            if categories:
                print("\nAvailable Categories: ")
                for cat in categories:
                    print(f"- {cat.name}")
            else:
                print("No categories found. ")


        elif choice=="7":
            name =input("Enter new category name: ")
            category=add_category(name)
            print(f"Category '{category.name}' added successfully. ")
        

        elif choice=="8":
            try:
                user_id=int(input("Enter User ID: "))
                category_id=int(input("Enter Category ID: "))
                amount=float(input("Enter amount: "))
                type = input("Enter type ('income' or 'expense'): ").strip().lower()

                if type not in ['income', 'expense']:
                     print("Invalid type. Please enter 'income' or 'expense'.")
                else:
                    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

                if date_input:
                    from datetime import datetime
                    date = datetime.strptime(date_input, "%Y-%m-%d")
                else:
                    date=None

                transaction=add_transaction(user_id, category_id, amount, date, type)
                print(f"Transaction added: {transaction.amount} on {transaction.date} as {transaction.type}")
            except Exception as e:
                print(f"Error adding transaction: {e}")

        elif choice == "9":
            try:
                user_id = int(input("Enter User ID to view transactions: "))
                transactions = get_transaction_by_user(user_id)

                if not transactions:
                    print("No transactions found for this user.")
                else:
                    print("\nTransactions:")
                    for t in transactions:
                        print(f"ID: {t.id} | Amount: {t.amount} | Type: {t.type} | Date: {t.date.date()} | Category ID: {t.category_id}")
            except Exception as e:
                print(f"Error retrieving transactions: {e}")
                    





        elif choice =="0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again. ")

if __name__=="__main__":
    main_menu()