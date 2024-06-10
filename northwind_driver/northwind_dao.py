import psycopg2
from psycopg2.extensions import AsIs


class orderDAO:

    def __init__(self):
        self.conn_string = "host='localhost' dbname='Trabalho3' user='postgres' password='admin' port='5432'"

    def __start_transaction(self):
        try:
            self.connection = psycopg2.connect(self.conn_string)
            self.connection.autocommit = False  # Desabilita o autocommit
        except psycopg2.Error as error:
            print(f"Error occurred while starting transaction: {error.pgcode} - {error.pgerror}")

    def __commit_transaction(self):
        try:
            if self.connection is not None:
                self.connection.commit()
                self.connection.close()
                self.connection = None
        except psycopg2.Error as error:
            print(f"Error occurred while committing transaction: {error.pgcode} - {error.pgerror}")

    def __rollback_transaction(self):
        try:
            if self.connection is not None:
                self.connection.rollback()
                self.connection.close()
                self.connection = None
        except psycopg2.Error as error:
            print(f"Error occurred while rolling back transaction: {error.pgcode} - {error.pgerror}")

    def search_order(self, orderid):
        query = "SELECT ord.orderid, ord.orderdate, c.contactname, e.firstname, o.productid, o.unitprice, o.quantity FROM northwind.orders ord JOIN northwind.customers c ON ord.customerid = c.customerid JOIN northwind.employees e ON ord.employeeid = e.employeeid JOIN northwind.order_details o ON ord.orderid = o.orderid WHERE ord.orderid = %s;"
        return self.__execute_sql(query, (orderid,))
    
    def insert_order(self, order):
        self.__start_transaction()

        try:
            order_query = "INSERT INTO northwind.orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            self.__execute_sql(order_query, order['order'])

            order_details_query = "INSERT INTO northwind.order_details VALUES (%s, %s, %s, %s, %s);"
            for detail in order['order_details']:
                self.__execute_sql(order_details_query, detail)

            self.__commit_transaction()

        except Exception as e:
            self.__rollback_transaction()
            raise e


    def get_employee_rank(self):
        query = "SELECT e.firstname, e.hiredate, COUNT(ord.orderid), SUM(o.unitprice) FROM northwind.employees e JOIN northwind.orders ord ON e.employeeid = ord.employeeid JOIN northwind.order_details o ON ord.orderid = o.orderid GROUP BY e.hiredate, e.firstname ORDER BY e.hiredate ASC;"
        return self.__execute_sql(query, ())

    def __execute_sql(self, query, values):
        errorcode = None
        affected_rows_count = 0
        registers = []
        cursor = None
        connection = None
        try:
            connection = psycopg2.connect(self.conn_string)
            cursor = connection.cursor()
            cursor.execute(query, values)
            affected_rows_count = cursor.rowcount
            connection.commit()
            try:
                registers = cursor.fetchall()
            except:
                registers = []
        except psycopg2.Error as error:
            errorcode = error.pgcode
            print(f"Error occurred: {error.pgcode} - {error.pgerror}")  # Print the error code and message
            connection.rollback()
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

        return errorcode, affected_rows_count, registers
