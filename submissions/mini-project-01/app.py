app_running = True
shopping_list = []

while(app_running):
    print("""
Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
    """)
    option = int(input("Enter the number of your choice: "))
    if option == 1:
        item_to_be_added = input("Enter the item you want to add: ")
        shopping_list.append(item_to_be_added)
        print(f"{item_to_be_added} has been added to your shopping list.")
    elif option == 2:
        print("Your shopping list:")
        for item in shopping_list:
            print(item)
    elif option == 3:
        item_to_be_removed = input("Enter the item you want to remove: ")
        if item_to_be_removed in shopping_list:
            shopping_list.remove(item_to_be_removed)
            print(f"{item_to_be_removed} has been removed from your shopping list")
        else:
            print(f"There are no {item_to_be_removed} in your shopping list, please try again")
    elif option == 4:
        print("Goodbye!")
        app_running = False
    else:
        print("Invalid Input, please try again")
        