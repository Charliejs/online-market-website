from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)


@app.route('/')
def my_index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        username = data["user_name"]
        password = data["pwd"]
        email = data["email"]
        csv_writer = csv.writer(database, delimiter=',', newline='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([username, password, email])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to.dict()
        write_to_csv(data)
        return 'Registered'
    else:
        return 'something is wrong'
