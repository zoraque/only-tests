# Python 3.9.2

import mysql.connector
from mysql.connector import Error

def execute_query():
    try:
        # Configuração da conexão
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port='3306',
            database='test',
            user='test',
            password='secret'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            query = '''
            SELECT 
                CONCAT(customers.first_name, ' ', customers.last_name) AS customer, 
                COUNT(events.status) AS failures
            FROM 
                customers
            INNER JOIN 
                campaigns
            ON 
                customers.id = campaigns.customer_id
            INNER JOIN
                events
            ON 
                campaigns.id = events.campaign_id
            WHERE
                events.status = 'failure'
            GROUP BY 
                CONCAT(customers.first_name, ' ', customers.last_name)
            HAVING 
                COUNT(events.status) > 3;
            '''
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            print("Customer | Failures")
            print("-" * 30)
            for row in results:
                print(f"{row[0]} | {row[1]}")
                
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    execute_query()
