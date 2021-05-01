import json

from db_util import makeDatabaseConnection, get_data

def lambda_handler(event, context):

    conn = makeDatabaseConnection()
    
    if conn != None:
       coctail_data = get_data(conn, )
    else:
          raise Exception ( json.dumps({
            "statusCode": 400, 
            "body" : {
                "error": "Connection to database failed"
            }
        }))
    
    return coctail_data