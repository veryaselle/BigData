import psycopg2
from configFile import host, user, password, db_name # eigene Zugangsdaten hinzufuegen


# DB wird connected
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # Cursor
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        "SELECT version();"
    #    )
    #    print(f"Server version: {cursor.fetchone()}")

    
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Server version: {cursor.fetchone()[0]}")

    # SQL data file open
#    with open('spotifydbdumpschemashare.sql', 'r') as file:
        # Execute the SQL statements
#        cursor.execute(file.read())
 #       print("File has been uploaded")
     
    with open('spotifydbdumpschemashare.sql', 'r') as file:
        # sql statements lesen
        sql_commands = file.read()



        # modified SQL statements lesen
        cursor.execute(sql_commands)
        print("File has been uploaded")
        

    cursor = connection.cursor()


except Exception as _exx:
    print("Error while working with PostgreSQL", _exx)

finally:

    if connection:
        connection.close()
        print("PostgreSQL connection closed")

#Commit the changes
#connection.commit()

# Close the cursor and connection
#cursor.close()
#conn.close()