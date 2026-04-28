import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name,price, purchase_date):
    # conn = None

    try:
        conn = mydbconnection.connect(
        database='usersdb',
        user='root',
        password='rootpassword'
        )
        print('🎉Connection Successful')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)VALUES (%s, %s, %s, %s) """
        record = (id, name, price, purchase_date) # putting values in tuple for insertion into query

        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print("Records inserted successfully into Laptop Table")

        print("✅Table Success")
        cursor.close()

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑Database Connection Closed')

# Module if state
if __name__ == '__main__':
    connect(2, 'MacBook pro2', 5000, '2026-01-02')
    connect(3, 'MacBook1', 1500, '2026-01-02')