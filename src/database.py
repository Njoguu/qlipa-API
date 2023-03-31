import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def getConnection():
    conn = psycopg2.connect(
        host=os.environ['POSTGRES_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        port=os.environ["POSTGRES_PORT"]
    )

    return conn


# TODO: Add function to retrieve user data
# TODO: Add function to add user data
# TODO: Add function to update user data
# TODO: Add function to delete user data
# TODO: Add function to retrieve PSV data
def getData():
    conn = getConnection()
    cur = conn.cursor()

    try:
        # Execute a SELECT statement
        cur.execute("SELECT * FROM psv")

        # Fetch the rows as a list of tuples
        rows = cur.fetchall()

        # Convert the rows to a list of dictionaries
        results = []
        for row in rows:
            result = {}
            for i, col in enumerate(cur.description):
                result[col.name] = row[i]
            results.append(result)

        # Close the database connection and cursor
        cur.close()
        conn.close()

        return results
    except Exception as err:
        print(f"Error! {err}")

# TODO: Add function to add PSV data
def addData():
    ...
    
# TODO: Add function to update PSV data
# TODO: Add function to delete PSV data
# TODO: Add function to retrieve PSV Ownwer data
# TODO: Add function to add PSV Ownwer data
# TODO: Add function to update PSV Ownwer data
# TODO: Add function to delete PSV Ownwer data
