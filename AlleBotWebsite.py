from flask import Flask, redirect, url_for, render_template, session
import webbrowser
import os
from forms import Items
from multiprocessing import Process

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/find", methods=["POST", "GET"])
def find():

    form = Items()
    if form.validate_on_submit():
        price_min = form.price_min.data
        price_max = form.price_max.data
        from Main import start
        item_count = start(form.item.data, price_min, price_max)
        session["item_count"] = item_count
        return redirect(url_for('result'))

    return render_template("find.html", form = form)

@app.route("/results")
def result():

    return render_template("results.html", item_count= session["item_count"])

@app.route("/about")
def additional():

    return render_template("about.html")


def start_server():
    print("START SERVER")
    app.run(debug=False)

def start_browser(url):
    webbrowser.open_new("{url}".format(url=url))

if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/'
    p1 = Process(target=start_server)
    p1.start()
    p2 = Process(target=start_browser, args=(url,))
    p2.start()



