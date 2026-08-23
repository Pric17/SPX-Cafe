from core.databaseUtility import Database

class OrderRepository:

    def saveOrder(self, order):
        headerSql = "INSERT INTO orders (username, orderDate, total) VALUES (?, ?, ?)"
        orderId = Database.dbSet(headerSql, (order.username, order.orderDate, order.total))

        itemSql = "INSERT INTO orderItems (orderId, mealId, quantity, priceAtTime) VALUES (?, ?, ?, ?)"
        for item in order.items:
            Database.dbSet(itemSql, (orderId, item.meal.mealId, item.quantity, item.priceAtTime))

        return orderId

    def getOrdersByCustomer(self, username):
        sql = "SELECT orderId, orderDate, total FROM orders WHERE username = ?"
        return Database.dbGet(sql, (username,))

    def getOrderItems(self, orderId):
        sql = """SELECT m.mealName, oi.quantity, oi.priceAtTime
                 FROM orderItems oi JOIN meals m ON oi.mealId = m.mealId
                 WHERE oi.orderId = ?"""
        return Database.dbGet(sql, (orderId,))
