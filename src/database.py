import os
import psycopg2
from dotenv import load_dotenv


# Function to get a database connection
def getConnection():

    conn = psycopg2.connect(
        host=os.environ['POSTGRES_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        port=os.environ["POSTGRES_PORT"],
    )

    return conn


# TODO: Add function to retrieve user data
# TODO: Add function to add user data
# TODO: Add function to update user data
# TODO: Add function to delete user data
# TODO: Add function to retrieve PSV data
# TODO: Add function to add PSV data
# TODO: Add function to update PSV data
# TODO: Add function to delete PSV data
# TODO: Add function to retrieve PSV Ownwer data
# TODO: Add function to add PSV Ownwer data
# TODO: Add function to update PSV Ownwer data
# TODO: Add function to delete PSV Ownwer data
