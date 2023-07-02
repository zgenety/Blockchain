from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

amount = 0
address = ""


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/sending', methods=['POST', 'GET'])
def send():
    global amount, address
    if request.method == "POST":
        address = request.form["address"]
        amount = request.form["amount"]
        return redirect(url_for('submit'), 301)
    else:

        return render_template("send.html")


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    return render_template("submit.html", amount=amount, address=address)


if __name__ == "__main__":
    app.run(debug=True)
