import requests
import json

def get_coctail_by_first_letter(letter):
    return requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + letter)

def get_json_coctail_by_first_letter(letter):
    return json.loads(get_coctail_by_first_letter(letter).text)["drinks"]

