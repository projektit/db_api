from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "{\"Hello\" : \"I am super legit JSON api\"}"

@app.route("/maskros")
def maskros():
    return "{\"name\" : \"maskros\"}"

if __name__ == "__main__":
    app.run()
