from flask import Flask, request, jsonify

from model import forecaster, pd

app = Flask(__name__)

@app.route('/')
def predict_static():
    # read static timesheets
    df = pd.read_csv("data/superhero_timesheets.csv")
    df["date"] = pd.to_datetime(df["date"])

    pred = forecaster.forecast(steps=1).astype(int).iloc[0]
    print(pred)

    today = pd.Timestamp.now().floor("D")
    roster = df[df.date < today]
    actives = ", ".join(roster.superhero.unique().tolist())
    n_result = roster.active_on_duty.sum()
    print(today)

    screwed_perc =  float(pred - n_result)/pred * 100 if pred > n_result else 0
    return f"<h3>Hello, NYC is {screwed_perc}% screwed today!</h3><br/>{actives} are on the job."


if __name__ == "__main__":
    app.run()
