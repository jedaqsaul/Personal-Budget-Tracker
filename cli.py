from helpers import add_user

def main_menu():
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add User")
        print("2. Exit")


        choice =input("Choose an option: ")

        if choice=="1":
            name=input("Enter name :")
            email=input("Enter email :")
            password=input("Enter password :")
            budget=input("Enter Monthly budget :")
            currency=input("Enter currency :")

            user=add_user(name, email, password, budget, currency)
            print(f"User {user.name} added successfully! ")
        elif choice =="2":
            print("Goodbye!")
            break

if __name__=="__main__":
    main_menu()