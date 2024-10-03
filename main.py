from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    today = datetime.date.today()
    year = today.year
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, curr_year=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url="https://api.genderize.io/?name="+name)
    response_age = requests.get(url="https://api.agify.io/?name="+name)

    response.raise_for_status()
    gender = response.json()["gender"]
    print(response.json())
    age = response_age.json()["age"]
    print(age)
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)


