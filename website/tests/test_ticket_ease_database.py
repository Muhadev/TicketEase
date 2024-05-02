import unittest
import mysql.connector

class TestTicketEaseDatabase(unittest.TestCase):
    def setUp(self):
        try:
            # Connect to the MySQL database
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',  # Replace with your MySQL username
                password='muhammed',  # Replace with your MySQL password
                database='TicketEase'  # Replace with your database name
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print("Error:", err)

    def test_events_table_exists(self):
        # Check if the events table exists
        self.cursor.execute("SHOW TABLES LIKE 'events'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Events table does not exist")

    def test_users_table_exists(self):
        # Check if the users table exists
        self.cursor.execute("SHOW TABLES LIKE 'users'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Users table does not exist")

    def test_tickets_table_exists(self):
        # Check if the tickets table exists
        self.cursor.execute("SHOW TABLES LIKE 'tickets'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Tickets table does not exist")

    def test_orders_table_exists(self):
        # Check if the orders table exists
        self.cursor.execute("SHOW TABLES LIKE 'orders'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Orders table does not exist")

    def test_payments_table_exists(self):
        # Check if the payments table exists
        self.cursor.execute("SHOW TABLES LIKE 'payments'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Payments table does not exist")

    def tearDown(self):
        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
