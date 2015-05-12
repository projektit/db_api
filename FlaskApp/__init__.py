# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import request
from flask import render_template

import sqlite3
app = Flask(__name__)

def to_json(result_tuple):
    
    try:
        values = ["id", "name", "latin_name", "type", "soil", "zone_min", "zone_max", "water", "sun", "misc", "swe_name", "img_url"]
        json = "{"

        for i, j in enumerate(result_tuple):
            if i == 9:
                j[0].replace('"', '\\\"')
                j[0].replace(":", "\\\:")
            json += '"{0}" : "{1}",'.format(values[i], j)

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
        
        #decode
        search_string = search_string.replace("[oh]", "Å")
        search_string = search_string.replace("[aeh]", "Ä")
        search_string = search_string.replace("[ueh]", "Ö")
        search_string = search_string.replace("[ohh]", "å")
        search_string = search_string.replace("[aehh]", "ä")
        search_string = search_string.replace("[uehh]", "ö")
        
        if search_string == "":
            return ""

        query = """SELECT * 
FROM plants WHERE 
name LIKE '{0}%' OR
name LIKE '% {0}%' OR
latin_name LIKE '{0}%' OR
latin_name LIKE '% {0}%' OR
swe_name LIKE '{0}%' OR
swe_name LIKE '% {0}%'""".format(search_string)
        
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

@app.route("/")
def home():
    return render_template('hem.html')

@app.route("/omoss")
def aboutus():
    return render_template('omoss.html')
@app.route("/appen")
def appen():
    return render_template('appen.html')

@app.route("/omprojektet")
def aboutproj():
    return render_template('omprojektet.html')

@app.route("/hittaoss")
def findus():
    return render_template('hittaoss.html')

if __name__ == "__main__":
    app.run()
