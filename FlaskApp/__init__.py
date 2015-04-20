from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "{\"Hello\" : \"I am super legit JSON api\"}"

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
