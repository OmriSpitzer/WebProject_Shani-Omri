from flask import Flask, render_template

app = Flask(__name__, static_folder='static')  # static_folder -> media folder to use in app


@app.route('/')  # defining route to web app
def homepage():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5002)
