import psycopg2

def makeDatabaseConnection():
    
    db_name = 'edu'
    db_user = 'education'
    db_host = 'edu-1.cpxvqniywpkp.us-east-1.rds.amazonaws.com'
    db_pass = 'vanja1998'

    conn = None
    
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print ("I am unable to connect to the database")
        
    return conn

def get_data(conn):
    result = None

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM coctails')
        result = cursor.fetchall()

        conn.commit()

    except (Exception, psycopg2.Error) as error:
        if(conn):
            print("Failed to execute sql", error)
    
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    
    return result

def insert_data(conn, coctails):
    try:
        cursor = conn.cursor()

        for coctail in coctails:
            cursor.execute('INSERT INTO coctails (coctailName, category, type, glass, instructions, imageUrl, ingredients, measures) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (coctail[0], coctail[1], coctail[2], coctail[3], coctail[4], coctail[5], coctail[6], coctail[7], ))
            
            conn.commit()
        
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print("Failed to execute sql", error)
    
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")