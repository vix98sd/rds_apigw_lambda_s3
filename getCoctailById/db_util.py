import psycopg2
import os
import json

def makeDatabaseConnection():
    
    db_name = 'edu'
    db_user = 'education'
    db_host = 'edu-1.c5rdbdjns2kx.us-east-1.rds.amazonaws.com'
    db_pass = 'zarko1993'
    
    conn = None
    
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print ("I am unable to connect to the database")
        
    return conn

def get_data(conn, coctailId):
    
    result = None
    
    try:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM coctails WHERE coctail_id = %s', (coctailId,))
      
      result = cursor.fetchone()

      conn.commit()
    
    except (Exception, psycopg2.Error) as error :
        if(conn):
            print("Failed to execute sql", error)
    
    finally:
        #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
            
    return result