# Importing necessary modules
from flask import Flask, render_template, request
import pandas as pd

# Creating a Flask application
app = Flask(__name__)


# Defining a class for barcode reader
class BarcodeReader:
    def __init__(self, csv_file_path):
        # Initializing the barcode reader by reading the CSV file
        self.barcodereader_df = pd.read_csv(csv_file_path)

    def search_by_code(self, code):
        # Searching for the given code in the barcode reader dataframe
        # and returning the matching results
        return self.barcodereader_df[self.barcodereader_df["code"] == code]


# Route for the home page
@app.route("/")
def index():
    # Rendering the index.html template
    return render_template("index.html")


# Route for the search functionality
@app.route("/search", methods=["POST"])
def search():
    # Retrieving the code from the form data submitted via POST method
    code = request.form["code"]

    # Creating an instance of the BarcodeReader class and providing
    # the path to the CSV file
    reader = BarcodeReader("openfoodfacts_smaller_database.csv")

    # Searching for the given code in the barcode reader and getting
    # the search results
    search_results = reader.search_by_code(code)

    # Rendering the search.html template with the search results
    return render_template("search.html", search_results=search_results)


# Running the Flask application
if __name__ == "__main__":
    # Starting the Flask application in debug mode
    app.run(debug=True)
