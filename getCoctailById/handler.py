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
        "coctailId" : coctail_data[0],
        "coctailName" : coctail_data[1],
        "instructions" : coctail_data[2],
        "ingredients" : coctail_data[3],
        "measures" : coctail_data[4],
        "imageUrl" : coctail_data[5],
        "category" : coctail_data[6],
        "type" : coctail_data[7],
        "glass" : coctail_data[8]
    }