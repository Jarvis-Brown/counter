from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "counter_project"


@app.route('/')
def index():
    if "count_num" not in session:
        session["count_num"] = 0
    return render_template("index.html")

@app.route("/increase")
def increase():
    session["count_num"] += 1
    return redirect('/')

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True,port=5001)
