import json

from db_util import makeDatabaseConnection, get_data

def lambda_handler(event, context):
    
    print(event['coctailId'])

    conn = makeDatabaseConnection()
    
    try:
        coctailId = event['coctailId']
    except:
        coctailId = None
    
    if conn != None:
       coctail_data = get_data(conn, coctailId)
    else:
          raise Exception ( json.dumps({
            "statusCode": 400, 
            "body" : {
                "error": "Connection to database failed"
            }
        }))
    
    return {
        "coctailId" : user_data[0],
        "coctailName" : user_data[1],
        "instructions" : user_data[2],
        "ingredients" : user_data[3],
        "ingredients" : user_data[4],
        "measures" : user_data[5],
        "imageUrl" : user_data[6],
        "category" : user_data[7],
        "type" : user_data[8],
        "glass" : user_data[9]
    }