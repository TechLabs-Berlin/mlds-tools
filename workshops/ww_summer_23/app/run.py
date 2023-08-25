import os

from sqlalchemy import create_engine
from flask import Flask, flash, render_template, request, redirect
import pandas as pd
from psycopg2 import connect, Error
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("base.html")

    # get the form data
    run_text = request.form["query"]
    try:
        # Connect to an existing database
        connection = connect(
            user="postgres", password="docker", host="demodb", port="5432", database="postgres"
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute(run_text)
        col_names = (desc[0] for desc in cursor.description)
        records = cursor.fetchmany(10)
        records.insert(0, col_names)

    except (Exception, Error) as error:
        records = [("ERROR", error)]
        print(records)

    finally:
        # print(connection)
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")

    return render_template("results.html", records=records)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=True, host="0.0.0.0", port=port)
