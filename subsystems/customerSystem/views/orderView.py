class OrderView:

    def showBasket(self, order):
        if not order or not order.items:
            print("\nYour basket is empty.")
            return
        print("\n----- Your Basket -----")
        for item in order.items:
            print(f" * {item.meal.mealName:<18} x{item.quantity:<3} ${item.subtotal:6.2f}")
        print(f"   {'Total':<22} ${order.total:6.2f}")

    def showSummary(self, order):
        print("\n===== Order Summary =====")
        for item in order.items:
            print(f" * {item.meal.mealName:<18} x{item.quantity:<3} @ ${item.priceAtTime:6.2f} = ${item.subtotal:6.2f}")
        print(f"   {'TOTAL':<22}            ${order.total:6.2f}")

    def needMoreDishes(self, needed, have):
        print(f"\nYou need at least {needed} different dishes to check out. You currently have {have}.")

    def orderSaved(self, orderId, total):
        print(f"\nOrder #{orderId} confirmed! Total: ${total:.2f}. Thank you for your order.")

    def mealAdded(self, meal, quantity):
        print(f"\nAdded {quantity} x {meal.mealName} to your order.")

    def showHistory(self, history):
        if not history:
            print("\nYou have no previous orders yet.")
            return
        print("\n========== YOUR ORDER HISTORY ==========")
        for order in history:
            print(f"\nOrder #{order['orderId']}  -  {order['orderDate']}")
            for item in order["items"]:
                subtotal = item["quantity"] * item["priceAtTime"]
                print(f" * {item['mealName']:<18} x{item['quantity']:<3} @ ${item['priceAtTime']:6.2f} = ${subtotal:6.2f}")
            print(f"   {'TOTAL':<22}            ${order['total']:6.2f}")

    def displayMsg(self, msg):
        print(f"\n[System]: {msg}")
