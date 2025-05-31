from helpers import add_user, get_user_by_email, update_user_budget

def main_menu():
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add User")
        print("2. View User by email")
        print("3. Insert user ID to update: ")
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



        elif choice =="0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again. ")

if __name__=="__main__":
    main_menu()