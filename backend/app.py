from flask import Flask
from file_reader.url import PDFReader as urlPdfReader

app = Flask(__name__)

@app.route('/')
def print_todays_date():
    print("This function is called")
    return "Kushal"


app.run(debug=True)