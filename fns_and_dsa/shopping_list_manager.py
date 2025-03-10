def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit\n")
    print("Choose 1, 2, 3 or 4")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and to add an item
            item = input('Enter the item to add: ')
            shopping_list.append(item)
            print (f"added {item} to the list")
            pass
        elif choice == '2':
            # Prompt for and to remove an item
            item = input('Enter the item to remove: ')
            if item in shopping_list:
                shopping_list.remove(item)
                print (f"removed {item} from the list")
            else:
                print(f"{item} not found in shopping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            print("\nShopping list has:")
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
