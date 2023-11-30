import psycopg2
# Update connection string information 

# !INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
host = "posthunter-server.postgres.database.azure.com"
dbname = "posthunter-database"
user = "ejevcopyxf"
password = "OW30047474Z258R5$"
sslmode = "require"
# Construct connection string

 # host="172.203.128.26",
        # dbname="posthunter-database",
        # user="ejevcopyxf",
        # password="OW30047474Z258R5$",
        # sslmode="require"
        
        
def connect_db():    
    conn = psycopg2.connect(
        host="localhost",
        database="posthunter-db",
        user="postgres",
        password="Puma1cat")
    return conn


def get_data_from_db(conn, where):
    cursor = conn.cursor()
    # # Fetch all rows from table
    select = "SELECT * FROM post_report" + f" WHERE tweet_id = '{where}';"
    print(select)
    cursor.execute(select)
    rows = cursor.fetchall()
    return rows


def add_data(conn, data):
    cursor = conn.cursor()
    print(data['url'])
    insert = f"INSERT INTO post_report(url, twitter_handle, tweet_id, \"timestamp\", type) VALUES ('{data['url']}','{data['tweet_handle']}', '{data['tweet_id']}', '{data['timestamp']}', '{data['type']}');"
    result = cursor.execute(insert)
    print(result)
    conn.commit()

    # print(f"Inserted {result.rowcount} row(s).")
    return cursor.rowcount


# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
# conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
# conn = psycopg2.connect(conn_string) 
# print("Connection established")
# cursor = conn.cursor()
# Drop previous table of same name if one exists

# # [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
# cursor.execute("DROP TABLE IF EXISTS inventory;")
# print("Finished dropping table (if existed)")
# # Create a table

# # [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
# cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
# print("Finished creating table")
# # Insert some data into the table

# # [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
# print("Inserted 3 rows of data")
# Clean up

# [!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]
