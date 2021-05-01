import psycopg2
from string import ascii_lowercase

from db_util import makeDatabaseConnection, get_data, insert_data
from api_util import get_json_coctail_by_first_letter

def main():
    conn = makeDatabaseConnection()

    if conn != None:
        coctail_data = get_data(conn)
        #print(coctail_data)
    
    coctails_for_db = []

    for ch in ascii_lowercase:
        coctails = get_json_coctail_by_first_letter(ch)
        if(coctails):
            for c in coctails:
                coctail = []
                coctail.append(c["strDrink"])
                coctail.append(c["strCategory"])
                coctail.append(c["strAlcoholic"])
                coctail.append(c["strGlass"])
                coctail.append(c["strInstructions"])
                coctail.append(c["strDrinkThumb"])

                ingredients = ""
                if(c["strIngredient1"] != None):
                    ingredients = ingredients + c["strIngredient1"]
                for i in range(2,16):
                    index = "strIngredient" + str(i)
                    if(c[index] != None):
                        ingredients = ingredients + ";" + c[index]

                coctail.append(ingredients)

                measures = ""
                if(c["strMeasure1"] != None):
                    measures = measures + c["strMeasure1"]
                for i in range(2,16):
                    index = "strMeasure" + str(i)
                    if(c[index] != None):
                        measures = measures + ";" + c[index]
                
                coctail.append(measures)
                
                coctails_for_db.append(coctail)
    
    # for c in coctails_for_db:
    #     print(c)
    
    print(len(coctails_for_db))
    
    conn = makeDatabaseConnection()

    if conn != None:
        insert_data(conn, coctails_for_db)
            
            
            
            
            
            

main()