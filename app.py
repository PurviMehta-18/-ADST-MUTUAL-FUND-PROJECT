from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("model/mutual_fund_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    date = request.form["date"]

    date = pd.to_datetime(date)

    date_number = date.toordinal()

    prediction = model.predict([[date_number]])

    predicted_nav = round(prediction[0], 2)

    return render_template(
        "index.html",
        prediction=predicted_nav,
        selected_date=date.strftime("%Y-%m-%d")
    )


if __name__ == "__main__":
    app.run(debug=True)