from flask import Flask

from model import forecaster, pd, db

app = Flask(__name__)


@app.route('/')
def predict_static():
    # read static timesheets
    df = pd.read_csv("data/superhero_timesheets.csv")
    df["date"] = pd.to_datetime(df["date"])

    pred = forecaster.forecast(steps=1).astype(int).iloc[0]
    print(pred)

    today = pd.Timestamp.now().floor("D")
    roster = df[df.date >= today].reset_index()
    actives = ", ".join(roster[roster.active_on_duty == 1].superhero.unique().tolist())
    n_result = roster.active_on_duty.sum()
    print(today)
    print(roster)

    screwed_perc =  float(pred - n_result)/pred * 100 if pred > n_result else 0
    return f"<h3>Hello, NYC is {screwed_perc}% screwed today!</h3><br/>{actives} are on the job."


def predict_backend():
    pred = forecaster.forecast(steps=1).astype(int).iloc[0]
    print(pred)

    # fetch results/timesheets from back-end
    today = pd.Timestamp.now().date()
    roster = pd.DataFrame([
        doc.to_dict() for doc in db.collection(u"superhero_timesheets").where(u"date", u">=", str(today)).stream()
    ])

    actives = ", ".join(roster[roster.active_on_duty == 1].superhero.unique().tolist())
    n_result = roster.active_on_duty.sum()
    print(today)
    print(roster)

    screwed_perc =  float(pred - n_result)/pred * 100 if pred > n_result else 0
    return f"<h3>Hello, NYC is {screwed_perc}% screwed today!</h3><br/>{actives} are on the job."


if __name__ == "__main__":
    app.run()
