from helpers import add_user, get_user_by_email, update_user_budget, delete_user,get_all_users,get_all_categories, add_category

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
        




        elif choice =="0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again. ")

if __name__=="__main__":
    main_menu()