from helpers import add_user, get_user_by_email

def main_menu():
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add User")
        print("2. View User by email")
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
        elif choice =="0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again. ")

if __name__=="__main__":
    main_menu()