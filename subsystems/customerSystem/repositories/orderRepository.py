from core.databaseUtility import Database

class OrderRepository:

    def saveOrder(self, order):
        # 1. Insert the order header and capture the new orderId (master row)
        headerSql = "INSERT INTO orders (username, orderDate, total) VALUES (?, ?, ?)"
        orderId = Database.dbSet(headerSql, (order.username, order.orderDate, order.total))

        # 2. Insert each basket line, linked to that orderId (detail rows).
        #    priceAtTime is the frozen price stored on the item.
        itemSql = "INSERT INTO orderItems (orderId, mealId, quantity, priceAtTime) VALUES (?, ?, ?, ?)"
        for item in order.items:
            Database.dbSet(itemSql, (orderId, item.meal.mealId, item.quantity, item.priceAtTime))

        return orderId

    def getOrdersByCustomer(self, username):
        # Used by the order-history feature (Step 4). Returns raw rows for now.
        sql = "SELECT orderId, orderDate, total FROM orders WHERE username = ?"
        return Database.dbGet(sql, (username,))
