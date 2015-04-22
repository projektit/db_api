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


@app.route("/")
def hello():
    
    result = list()
   
    try:
        connection = sqlite3.connect("/var/www/FlaskApp/FlaskApp/db_test_large.db")        
        c = connection.cursor()
        search_string = request.args.get("name").lower()
        if search_string == "": return ""

        query = "select * from plants where name like '{0}%' or latin_name like '{0}%' or type like '{0}%' or swe_name like '{0}%'".format(search_string)

        for i in c.execute(query):
            result.append(i)
       
        
 
        final = "["
        for i in result:
            final += to_json(i) + ","
        final = final[:-1] + "]"
        
        if final == "]": return ""
        return final

    except Exception, e: return str(e)


@app.route("/maskros")
def maskros():
    return """ {
    "name": "maskros",
    "latin_name": "maskus rosus",
    "kategori": "ogras",
    "jord": "all",
    "zon": "forsvarszon"
}"""

@app.route("/havstulpan")
def havstulpan():
    return """ {
    "name": "havstulpan",
    "latin_name": "tulpis oceanus",
    "kategori": "sjogras",
    "jord": "nej",
    "zon": "parkeringszon"
}"""

if __name__ == "__main__":
    app.run()
