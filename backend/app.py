from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_todays_date():
    print("This function is called")
    return "Kushal"


app.run(debug=True)