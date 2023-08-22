import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # get the form data
        run_text = request.form['query']
        # print(run_text)
        return render_template('results.html', run_text=run_text)
    # print("GET Request received")
    return render_template('base.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
