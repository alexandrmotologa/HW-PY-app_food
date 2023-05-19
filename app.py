from restaurant import *

# contains order data
order = {
    "items":[]
}
###############################
food = loadFood()
while True:
    option = printMenu()
    
    if option == 0: # exit
        break
    if option == 1: # show menu
        printFood(food)
        input("Hit ENTER to continue")
    if option == 2: # order
        selected_i = int(input("Which item: ")) - 1
        name = food[selected_i] ['name']
        print(f"You've selected <<{name}>>")
        
        quantity = int(input("How many: "))
        availability = food[selected_i]['avail']
        
        if  availability > 0:
            currency = food[selected_i] ['price']['currency']
            if quantity <= availability or quantity > availability:
                if quantity > availability:
                    print(f"We only have {availability} products of type <<{name}>>.")
                    quantity = availability
                price_per_item = quantity * food[selected_i]['price']['amount']
                print(f"{name} x {quantity} = {price_per_item:8.2f} {currency}")

            confirm_order = input(f"Please confirm if you want to place an order for {quantity} units of product <<{name}>> ( yes/no ): ")
            if confirm_order == "y":                    
                
                order_item = {
                    "name": name,
                    "quantity": quantity,
                    "total": {
                        "amount": price_per_item,
                        "currency": currency
                    }
                }
                order["items"].append(order_item)
                print(order["items"])
                
        else:
            print(f"Out of stock products of type <<{name}>>")
        
        input("\nHit ENTER to continue")