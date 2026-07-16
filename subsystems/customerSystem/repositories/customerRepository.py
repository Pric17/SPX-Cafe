from core.databaseUtility import Database
from subsystems.customerSystem.models.customerModel import Customer

class CustomerRepository:

    def getByUsername(self, username):
        sql = "SELECT username, password, firstName, lastName FROM customers WHERE username = ?"
        rows = Database.dbGet(sql, (username,))
        if not rows:
            return None
        row = rows[0]
        return Customer(row[0], row[1], row[2], row[3])

    def addCustomer(self, customer):
        sql = "INSERT INTO customers (username, password, firstName, lastName) VALUES (?, ?, ?, ?)"
        Database.dbGet(sql, (customer.username, customer.password, customer.firstName, customer.lastName))
