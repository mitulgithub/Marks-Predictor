from flask import Flask,render_template, redirect, request 
import linear_regression_training_

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods = ['POST'])
def marks_prediction():
    if request.method == 'POST':
        f = float(request.form['marks'])
        ans = linear_regression_training_.predict_marks(f)

    return render_template("index.html", marks = ans)


if __name__ == '__main__':
    app.run(debug=True)