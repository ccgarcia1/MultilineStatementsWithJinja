from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

def current_year():
    today = datetime.date.today()
    year = today.year
    return year
@app.route('/')
def home():

    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, curr_year=current_year())


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

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts, curr_year=current_year())

if __name__ == "__main__":
    app.run(debug=True)


