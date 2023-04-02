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


# function to add PSV data
def addData(registration_no, driver, seats, route_id, owner_id, fare):
    conn = getConnection()
    cur = conn.cursor()

    addDataSQL = f'''
        INSERT INTO psv(
            registration_no, driver, seats, route_id, owner_id, fare)
            VALUES ('{registration_no}', 
                    '{driver}',
                    '{seats}',
                    '{route_id}',
                    '{owner_id}',
                    '{fare}');
    '''

    try:
        cur.execute(addDataSQL)
        # Commit the changes to the database
        conn.commit()
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        cur.close()
        conn.close()


# function to retrieve specific PSV data
def getPSV(psv_id):
    conn = getConnection()
    cur = conn.cursor()

    getSQL = f'''
        SELECT registration_no, driver, seats, route_id, fare 
        FROM psv
        WHERE psv_id = {psv_id};
    '''

    try:
        cur.execute(getSQL)

        # Fetch the rows as a list of tuples
        rows = cur.fetchall()

        # Convert the rows to a list of dictionaries
        results = []
        for row in rows:
            result = {}
            for i, col in enumerate(cur.description):
                result[col.name] = row[i]
            results.append(result)

        return results

    except Exception as err:
        conn.rollback()
        print(f'error! {err}')
    finally:
        cur.close()
        conn.close()


# TODO: fix function to update PSV data
def updatePSV(psv_id, registration_no, driver, seats, route_id, owner_id, fare):
    conn = getConnection()
    cur = conn.cursor()

    updateDataSQL = f'''
            UPDATE psv
            SET registration_no = '{registration_no}',
                driver = '{driver}',
                seats = {seats},
                route_id = {route_id},
                owner_id = {owner_id},
                fare = {fare}
            WHERE id = {psv_id};
    '''

    try:
        cur.execute(updateDataSQL)
        conn.commit()
    except Exception as err:
        conn.rollback()
        print(f"error! {err}")
    finally:
        cur.close()
        conn.close()


# function to delete PSV data
def deletePSV(psv_id):
    conn = getConnection()
    cur = conn.cursor()

    deleteSQL = f'''
        DELETE FROM psv
	    WHERE psv_id = {psv_id};
    '''

    try:
        cur.exectute(deleteSQL)
        # commit changes to DB
        conn.commit()
    except Exception as err:
        conn.rollback()
        print(f"error! {err}")
    finally:
        cur.close()
        conn.close()


# TODO: Add function to retrieve PSV Ownwer data
# TODO: Add function to add PSV Ownwer data
# TODO: Add function to update PSV Ownwer data
# TODO: Add function to delete PSV Ownwer data
