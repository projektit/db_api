from flask import Flask
from flask import request


import sqlite3
app = Flask(__name__)

def to_json(result_tuple):
    
    try:
        values = ["id", "name", "latin_name", "type", "soil", "zone_min", "zone_max", "water", "sun", "misc", "swe_name"]
        json = "{"

        for i, j in enumerate(result_tuple):
            json += '"{0}" : "{1}",'.decode('utf-8').format(values[i], j)

        json = json[:-1]
        json += "}"
    except Exception, e: return str(e)

    return json


@app.route("/api")
def api():
    
    result = list()
   
    try:
        connection = sqlite3.connect("/var/www/FlaskApp/FlaskApp/plants.db")        
        c = connection.cursor()
        search_string = request.args.get("name").lower()
        if search_string == "":
            return ""

        query = "SELECT * FROM plants WHERE name LIKE '{0}%' OR latin_name LIKE '{0}%' OR type LIKE '{0}%' OR swe_name LIKE '{0}%'".format(search_string)

        for i in c.execute(query):
            result.append(i)     
 
        final = "["
        for i in result:
            final += to_json(i) + ","
        final = final[:-1] + "]"

        # If query returns nothing
        if final == "]":
            return ""

        return final

    except Exception, e: return str(e)

if __name__ == "__main__":
    app.run()
