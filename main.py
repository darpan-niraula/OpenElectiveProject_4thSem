from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trial")
def trial():
    return render_template("trial.html")

@app.route("/about_content")
def about_content():
    return render_template("about_content.html")

@app.route("/recent-trips")
def recent_trips():
    return render_template("recent_trips.html")

if __name__ == "__main__":
    app.run(debug=True)