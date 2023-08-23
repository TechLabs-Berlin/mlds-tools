import os

from sqlalchemy import create_engine
from flask import Flask, flash, render_template, request, redirect
import pandas as pd
from psycopg2 import connect, Error
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('base.html')

    # get the form data
    run_text = request.form['query']
    if not run_text:
        run_text = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'"
    try:
        # Connect to an existing database
        connection = connect(
            user="postgres",
            password="docker",
            host="demodb",
            port="5432",
            database="postgres"
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

    return render_template('results.html', records=records)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file_table, file_ext = file.filename.split(".")
        if file_ext.lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(filename)

            df = pd.read_csv(filename, sep=",")
            print(df)
            engine = create_engine('postgresql+psycopg2://postgres:docker@demodb:5432/postgres')
            df.to_sql(file_table, con=engine, if_exists='fail', index=False)
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload Table</title>
    <h1>Upload new CSV File</h1>
    <form method="POST" enctype=multipart/form-data>
      <input type=file name="file"><br/><br/>
      <input type=submit value="Upload">
    </form>
    '''


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
