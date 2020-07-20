from flask import Flask, redirect, url_for, render_template, request
import webbrowser
from multiprocessing import Process

app = Flask(__name__)



@app.route("/")
def home():

    return render_template("home.html")

@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":

        item = request.form["item"]
        submit = request.form["value"]

        from Main import start
        start(item)
        return redirect(url_for('result'))
    else:
        return render_template("basic.html")

@app.route("/results")
def result():

    return render_template("results.html")

@app.route("/additional")
def additional():

    return render_template("additional.html")


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



