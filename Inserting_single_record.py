import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
        database='usersdb',
        user='root',
        password='rootpassword'
        )
        print('🎉Connection Successful')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (1, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """
        cursor.execute(mySql_insert_query)
        conn.commit()
        print(cursor.rowcount ,"Records inserted successfully into Laptop Table")

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
    connect()

